# Load your usual SpaCy model (one of SpaCy English models)
import spacy
nlp = spacy.load('en')

# Add neural coref to SpaCy's pipe
import neuralcoref
neuralcoref.add_to_pipe(nlp)

# You're done. You can now use NeuralCoref as you usually manipulate a SpaCy document annotations.
doc = nlp(u'''
During Destiny's Child's hiatus, Beyoncé made her theatrical film debut with a role in the US box-office number-one Austin Powers in Goldmember (2002) and began her solo music career. She became the first music act to debut at number one with their first six solo studio albums on the Billboard 200.[7] Her debut album Dangerously in Love (2003) featured four Billboard Hot 100 top five songs, including the number-one singles "Crazy in Love" featuring rapper Jay-Z and "Baby Boy" featuring singer-rapper Sean Paul. Following the disbandment of Destiny's Child in 2006, she released her second solo album, B'Day, which contained her first US number-one solo single "Irreplaceable", and "Beautiful Liar", which topped the charts in most countries. Beyoncé continued her acting career with starring roles in The Pink Panther (2006), Dreamgirls (2006), and Obsessed (2009). Her marriage to Jay-Z and her portrayal of Etta James in Cadillac Records (2008) influenced her third album, I Am... Sasha Fierce (2008), which earned a record-setting six Grammy Awards in 2010. It spawned the UK number-one single "If I Were a Boy", the US number-one single "Single Ladies (Put a Ring on It)" and the top five single "Halo".
''')

for cluster in doc._.coref_clusters:
    print(cluster, end="\n\n")

# print(doc._.coref_clusters)
# doc._.coref_clusters[1].mentions
# doc._.coref_clusters[1].mentions[-1]
# doc._.coref_clusters[1].mentions[-1]._.coref_cluster.main

# token = doc[-1]
# token._.in_coref
# token._.coref_clusters

# span = doc[-1:]
# span._.is_coref
# span._.coref_cluster.main
# span._.coref_cluster.main._.coref_cluster