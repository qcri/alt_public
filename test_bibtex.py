import bibtexparser

def test_tanbih():
  with open('tanbih.bib') as bibtex_file:
    bib_database = bibtexparser.load(bibtex_file)

def test_alt():
  with open('alt.bib') as bibtex_file:
    bib_database = bibtexparser.load(bibtex_file)
