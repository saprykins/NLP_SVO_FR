# KEEP ONLY SUBJ, VERB, OBJ, CONG
# KEEP THE WHOLE CHUNKS (united kingdom, not kingdom)
# GET LEMMAS

# COPY OF THE FILE WITH BASIC (NOT LG CONTENT IS IN COLAB)

import spacy
import fr_core_news_lg

nlp = fr_core_news_lg.load()


doc = nlp("La Grande Bretagne quitte l'Union Europeenne.")
# doc = nlp("Il est alors l'un des dirigeants les plus en vue de l'Union pour un mouvement populaire (UMP), qu'il préside de 2004 à 2007.")
# doc = nlp("La Grande Bretagne qui ne fais pas partie de l'Union Europeenne a des problemes.")

'''
# GET SENTENCE SCHEME

for token in doc:
    print(f"{token.text:10}", f"{token.lemma_:10}", f"{token.pos_:10}", f"{token.tag_:10}", f"{token.dep_:10}",
            f"{token.shape_:10}", f"{token.is_alpha:10}", f"{token.is_stop:10}", f"{token.morph:10}")

'''            
            
# go through all words
for token in doc:
  # if the word is subj
  if token.dep_ == "nsubj":
    # check if it is a part of entities
    for i in range(len(doc.ents)):
      important_part = token
      if important_part.text in str(doc.ents[i]):
        # print(important_part.text)
        print(doc.ents[i])
        # leave the cycle (United gives one, Kingdome gives two)
        break
      else: 
        print(token.text)
        break

  elif token.dep_ == "obj":
    for i in range(len(doc.ents)):
      important_part = token
      if important_part.text in str(doc.ents[i]):
        # print(important_part.text)
        print(doc.ents[i])
        break
      else: 
        print(token.text)
        break

  elif token.dep_ == "conj":
    for i in range(len(doc.ents)):
      important_part = token
      if important_part.text in str(doc.ents[i]):
        # print(important_part.text)
        print(doc.ents[i])
        break
      else: 
        print(token.text)
        break

  if token.dep_ == "advmod" or token.dep_ == "ROOT":
    print(token.lemma_)
