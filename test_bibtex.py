import bibtexparser

def test_tanbih():
  with open('tanbih.bib') as bibtex_file:
    bib_database = bibtexparser.load(bibtex_file)

def test_alt():
  with open('alt.bib') as bibtex_file:
    bib_database = bibtexparser.load(bibtex_file)
    return not has_doubles(bib_database)

def has_doubles(elements):
  """
  check if two or more different objects have the same pdf-file 
  """
  elements = elements.get_entry_list()
  final_list = []
  has_duplicate = False; 
  for elem in elements: 
    if elem not in final_list: 
        final_list.append(elem) 
    else: 
      print(elem) 
      has_duplicate = True
  return has_duplicate