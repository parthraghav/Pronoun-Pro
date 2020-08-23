# Load your usual SpaCy model (one of SpaCy English models)
import spacy
nlp = spacy.load('en')

# Add neural coref to SpaCy's pipe
import neuralcoref
neuralcoref.add_to_pipe(nlp)

SECOND_PERSONAL_PRONOUNS = ['he', 'she', 'they']
SECOND_OBJECTIVE_PRONOUNS = ['him', 'her', 'them']
SECOND_PROMINAL_PRONOUNS = ['his', 'her', 'their']
SECOND_POSSESSIVE_PRONOUNS = ['his', 'hers', 'theirs']

PRONOUN_LIST = [
    *SECOND_PERSONAL_PRONOUNS,
    *SECOND_OBJECTIVE_PRONOUNS,
    *SECOND_PROMINAL_PRONOUNS,
    *SECOND_POSSESSIVE_PRONOUNS,
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


def coref_distance(coref, main):
    """Returns a distance between a co-refering mention from the main mention.
    """
    return abs(coref.start - main.end)


def get_offset_to_verb_and_aux(sentence):
    """Returns offset to vern and auxiliary"""
    pass


def _neutralise(doc, clusters):
    """Neutralise gendered coreferences in a text block.
    """
    resolved = [tok.text_with_ws for tok in doc]
    lines = []
    for cluster in clusters:
        for coref in cluster:
            coref_text = coref.text.lower()
            cluster_main_text = cluster.main.text.lower()

            _isSingleToken = len(coref_text.split()) == 1
            _isNotMainMention = coref_text != cluster_main_text
            _isIdentifiablePronoun = coref_text in PRONOUN_LIST

            if _isSingleToken and _isNotMainMention and _isIdentifiablePronoun:
                # Token is pronoun!

                original_sentence, start_index = get_sentence_at_index(
                    coref.start, resolved)
                processed_sentence = ''.join(original_sentence).lower()

                # Check if the current token isn't a proper noun. We don't wanna change them, because they aren't pronouns!!!!
                if resolved[coref.start] != ' '.join(
                        cluster_main_text.strip().split()):

                    # The main mention does not occur in this sentence as a word
                    if coref_distance(coref, cluster.main) > 500:
                        # Resolve co-referring mention with the main mention
                        resolved[coref.start] = cluster.main.text + doc[
                            coref.end - 1].whitespace_
                        # Capitalise the first letter of the name
                        if start_index == coref.start:
                            resolved[coref.start] = resolved[
                                coref.start].capitalize()
                    else:
                        # Neutralise the co-referring mention
                        pronoun = resolved[coref.start].strip().lower()
                        token = doc[coref.start]
                        if token.tag_ == 'PRP' and 'subj' in token.dep_:
                            detected_pronoun_set = SECOND_PERSONAL_PRONOUNS
                        elif token.tag_ == 'PRP' and 'obj' in token.dep_:
                            detected_pronoun_set = SECOND_OBJECTIVE_PRONOUNS
                        elif token.tag_ == 'PRP$' and token.dep_ in [
                                'poss', 'nmod'
                        ]:
                            detected_pronoun_set = SECOND_PROMINAL_PRONOUNS
                        elif token.tag_ == 'NNS' and token.dep_ == 'attr':
                            detected_pronoun_set = SECOND_POSSESSIVE_PRONOUNS
                        else:
                            print("fuck", pronoun, token.tag_, token.dep_,
                                  ''.join(original_sentence))

                        resolved[coref.start] = detected_pronoun_set[-1] + doc[
                            coref.end - 1].whitespace_
                        # Capitalise the first letter of the pronoun
                        if start_index == coref.start:
                            resolved[coref.start] = resolved[
                                coref.start].capitalize()
                        # Neutralise the corresponding verb
                        verb_candidate1 = doc[coref.start + 1]
                        if verb_candidate1.pos_ == 'VERB':
                            resolved[coref.start +
                                     1] = verb_candidate1.lemma_ + doc[
                                         coref.end - 1].whitespace_
                            if verb_candidate1.text == 'is':
                                resolved[coref.start +
                                         1] = 'are' + doc[coref.end -
                                                          1].whitespace_
                            if verb_candidate1.text == 'was':
                                resolved[coref.start +
                                         1] = 'were' + doc[coref.end -
                                                           1].whitespace_

                        # print(doc[coref.start + 1].pos_)

                        original_sentence = [
                            resolved[coref.start]
                            if word == coref.text else word
                            for word in original_sentence
                        ]
                    final_sentence = ''.join(original_sentence)
    return ''.join(resolved)


def neutralise(txt):
    doc = nlp(u'''{txt}'''.format(txt=txt))
    clusters = doc._.coref_clusters
    return _neutralise(doc, clusters)


if __name__ == '__main__':
    # You're done. You can now use NeuralCoref as you usually manipulate a SpaCy document annotations.
    with open('demo.txt', 'r') as file:
        text = file.read().replace('\n', '')
        neutralised_text = neutralise(text)
        print(neutralised_text)
        file.close()
