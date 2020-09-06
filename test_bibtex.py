import bibtexparser
import unittest

class TestBibtexFiles(unittest.TestCase):
  def test_tanbih(self):
    with open('tanbih.bib') as bibtex_file:
      bib_database = bibtexparser.load(bibtex_file)

  def test_alt(self):
    with open('alt.bib') as bibtex_file:
      bib_database = bibtexparser.load(bibtex_file)
      self.assertFalse(self.has_doubles(bib_database))

  def has_doubles(self, elements):
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

if __name__ == '__main__':
  unittest.main()

