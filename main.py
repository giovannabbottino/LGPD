# cnpj
# (\d{2}(?:.?\d{3}){2}/?\d{4}-?\d{2})
# cpf
# ((?:\d{3}.?){3}-?\d{2})
# data de nascimento
# ((?:\d{1,2}(?:/|-)){2}\d{2,4})
# rg sao paulo e df
# (\d{1,2}.?(?:\d{3}.?){2}-?\d{0,1})
# todas
# (\d{2}(?:.?\d{3}){2}/?\d{4}-?\d{2})|((?:\d{3}.?){3}-?\d{2})|((?:\d{1,2}(?:/|-)){2}\d{2,4})|(\d{1,2}.?(?:\d{3}.?){2}-?\d{0,1})
from controller_verificadora import Verifica
import PyPDF2
import re

REGEX = r"(\d{5}.\d{6}/\d{4}-\d{2})|(\d{2}(?:.?\d{3}){2}/?\d{4}-?\d{2})|((?:\d{3}.?){3}-?\d{2})|((?:\d{1,2}(?:/|-)){2}\d{2,4})|(\d{1,2}.?(?:\d{3}.?){2}-?\d{0,1})" 

def my_replace(match):
  if match.group(1) != None:
    return match.group(1)
  
  # verificacao cnpj
  if match.group(2) != None:
    if (verifica.cnpj(match.group(2))):
      return match.group(2).replace(match.group(2), "-Dados pessoais diretos-")
    return match.group(2)
  
  # verificacao cpf
  if match.group(3) != None:
    if (verifica.cpf(match.group(3))):
      return match.group(3).replace(match.group(3), "-Dados pessoais diretos-")
    return match.group(3)
  
  # verifica restante
  for i in range(4, 6):
    if match.group(i) != None:
      return match.group(i).replace(match.group(i), "-Dados pessoais diretos-")

def procuraRegex(*args):
  return_args = []
  for arg in args:
    result = re.search(REGEX, arg)
    if result != None:
      arg_replace = re.sub(REGEX, my_replace, arg)
      if arg_replace != arg:
        return_args.append(arg_replace) 
  return return_args

def leArquivo(*args):
  for arg in args:
    pdf_file = open(arg, 'rb')
    read_pdf = PyPDF2.PdfFileReader(pdf_file)
    number_of_pages = read_pdf.getNumPages()

    page_content = ''
    for i in range(0, number_of_pages):
      page = read_pdf.getPage(i)
      page_content += page.extractText()
    
    parsed = ''.join(page_content)
    parsed = re.sub('\n', '', parsed)
    print(parsed)
    print(procuraRegex(parsed))

if __name__ == "__main__":
  verifica = Verifica()
  texto = "11111111111 Lorem ipsum dolor sit amet, consectetur adipiscing elit."
  texto_com = "Lorem 44.444.444/4444-44 21.001.474/0001-28 ipsum dolor processo nº 00058.049824/2020-74 sit amet, 11111111111  03422107185 consectetur adipiscing 10-6-99 2967972" 
  print(procuraRegex(texto, texto_com))
  # mude o nome se necessario
  # arquivo = "DA2021-0348.pdf"
  # arquivo2 = "DA2021-0345.pdf"
  # arquivo3 = "SEI_00065.018603_2018_41.pdf"
  # leArquivo(arquivo2)