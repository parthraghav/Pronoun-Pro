# Load your usual SpaCy model (one of SpaCy English models)
import spacy
nlp = spacy.load('en')

# Add neural coref to SpaCy's pipe
import neuralcoref
neuralcoref.add_to_pipe(nlp)

pronoun_list = [
    'he', 'she', 'it', 'they', 'them', 'him', 'her', 'his', 'hers', 'its',
    'we', 'us'
]


def get_sentence_at_index(index, resolved_list):
    """Returns the sentence beginning at the index
    """
    end_of_sentence_punctuation = ['.', '!', '?']
    begin_index = index
    end_index = index
    while begin_index >= 0:
        val = resolved_list[begin_index].strip()
        if val in end_of_sentence_punctuation:
            break
        else:
            begin_index -= 1
    while end_index <= len(resolved_list) - 1:
        val = resolved_list[end_index].strip()
        if val in end_of_sentence_punctuation:
            break
        else:
            end_index += 1
    return resolved_list[begin_index + 1:end_index + 1], begin_index + 1


def get_resolved(doc, clusters):
    """Returns list of utterances text where the co-refering mentions are resolved to their closest main mention
    """
    resolved = [tok.text_with_ws for tok in doc]
    lines = []
    for cluster in clusters:
        for coref in cluster:
            coref_text = coref.text.lower()
            cluster_main_text = cluster.main.text.lower()

            _isSingleToken = len(coref_text.split()) == 1
            _isNotMainMention = coref_text != cluster_main_text
            _isIdentifiablePronoun = coref_text in pronoun_list

            if _isSingleToken and _isNotMainMention and _isIdentifiablePronoun:
                # Token is pronoun!
                original_sentence, start_index = get_sentence_at_index(
                    coref.start, resolved)
                processed_sentence = ''.join(original_sentence).lower()

                if ' '.join(cluster_main_text.strip().split()
                            ) not in processed_sentence:
                    # The main mention does not occur in this sentence as a word
                    # Resolve co-referring mention with the main mention
                    resolved[coref.start] = cluster.main.text + doc[
                        coref.end - 1].whitespace_
                    # Capitalise the first letter of the name
                    if start_index == coref.start:
                        resolved[coref.start] = resolved[
                            coref.start].capitalize()
                    final_sentence = ''.join(original_sentence)

                    if len(final_sentence) > 0:
                        lines.append([
                            final_sentence, coref.text, resolved[coref.start]
                        ])


def neutralise(doc):
    """Neutralise gendered coreferences in a text block.
    """
    plural_lemma_tags = {"NNS", "NNPS"}
    for token in doc:
        lemma = token.text
        if token.tag_ in plural_lemma_tags:
            # Token is plural
            print(lemma)
            pass


if __name__ == '__main__':
    # You're done. You can now use NeuralCoref as you usually manipulate a SpaCy document annotations.
    doc = nlp(
        u'''During Destiny's Child's hiatus, Beyoncé made her theatrical film debut with a role in the US box-office number-one Austin Powers in Goldmember (2002) and began her solo music career. She became the first music act to debut at number one with their first six solo studio albums on the Billboard 200.[7] Her debut album Dangerously in Love (2003) featured four Billboard Hot 100 top five songs, including the number-one singles "Crazy in Love" featuring rapper Jay-Z and "Baby Boy" featuring singer-rapper Sean Paul. She married Jay-Z. He cheated on him. Following the disbandment of Destiny's Child in 2006, she released her second solo album, B'Day, which contained her first US number-one solo single "Irreplaceable", and "Beautiful Liar", which topped the charts in most countries. Beyoncé continued her acting career with starring roles in The Pink Panther (2006), Dreamgirls (2006), and Obsessed (2009). Her marriage to Jay-Z and her portrayal of Etta James in Cadillac Records (2008) influenced her third album, I Am... Sasha Fierce (2008), which earned a record-setting six Grammy Awards in 2010. It spawned the UK number-one single "If I Were a Boy", the US number-one single "Single Ladies (Put a Ring on It)" and the top five single "Halo".'''
    )
    clusters = doc._.coref_clusters
    # neutralise(doc)
    get_resolved(doc, clusters)