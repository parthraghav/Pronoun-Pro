# Load your usual SpaCy model (one of SpaCy English models)
import spacy
nlp = spacy.load('en')

# Add neural coref to SpaCy's pipe
import neuralcoref
neuralcoref.add_to_pipe(nlp)


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
            begin_index += 1
    while end_index <= len(resolved_list) - 1:
        val = resolved_list[end_index].strip()
        if val in end_of_sentence_punctuation:
            break
        else:
            end_index += 1
    return resolved_list[begin_index + 1:end_index + 1], begin_index + 1


def coref_distance():
    """Returns a distance between a co-refering mention from the main mention.
    """
    pass


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
        u'''During Destiny's Child's hiatus, Beyoncé made her theatrical film debut with a role in the US box-office number-one Austin Powers in Goldmember (2002) and began her solo music career. She became the first music act to debut at number one with their first six solo studio albums on the Billboard 200.[7] Her debut album Dangerously in Love (2003) featured four Billboard Hot 100 top five songs, including the number-one singles "Crazy in Love" featuring rapper Jay-Z and "Baby Boy" featuring singer-rapper Sean Paul. Following the disbandment of Destiny's Child in 2006, she released her second solo album, B'Day, which contained her first US number-one solo single "Irreplaceable", and "Beautiful Liar", which topped the charts in most countries. Beyoncé continued her acting career with starring roles in The Pink Panther (2006), Dreamgirls (2006), and Obsessed (2009). Her marriage to Jay-Z and her portrayal of Etta James in Cadillac Records (2008) influenced her third album, I Am... Sasha Fierce (2008), which earned a record-setting six Grammy Awards in 2010. It spawned the UK number-one single "If I Were a Boy", the US number-one single "Single Ladies (Put a Ring on It)" and the top five single "Halo".'''
    )
    neutralise(doc)