import shutil, re

potential_contacts = 'assets/potential-contacts.txt'
assets_path = 'assets/'

def get_ph_numbers(potential_contacts, assets_path):
  with open(potential_contacts, 'r') as f:
    contents = f.read()
    # print(contents)
  phone_number_regex = r'[(]?\d{3}[)]?\S?\d{3}\S?\d{4}|\d{3}\S?\d{4}'
  phone_numbers = list(re.findall(phone_number_regex, contents))
  phone_numbers = [char.replace(r'[.-/()]', '') for char in phone_numbers]
  normalized_numbers = list()
  for number in phone_numbers:
    number = (re.sub(r'[.\-()]', '', number))
    if len(number) < 10:
      number = '206' + number
    normalized_numbers.append(number)
  normalized_numbers.sort()
  normalized_numbers = list(set(normalized_numbers))

  print(len(normalized_numbers))
  print(normalized_numbers)

  with open(assets_path+"phone.txt", 'w') as f:
    for num in normalized_numbers:
      f.write(num)
      f.write("\n")

get_ph_numbers(potential_contacts, assets_path)