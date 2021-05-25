def pre_process(text):
  #Make lowercase
  text = text.strip().lower()

  #Remove punctuation
  filters = '!"\'#$%&()*+,-./:;<=>?@[\\]^_`{|}~\t\n'
  translate_dict = dict((c, " ") for c in filters)
  translate_map = str.maketrans(translate_dict)
  text = text.translate(translate_map)

  return text