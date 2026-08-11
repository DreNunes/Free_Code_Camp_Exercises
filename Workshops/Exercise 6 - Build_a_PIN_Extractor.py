# The nth digit of the pin is hidden as the length of the nth word in the nth line
def pin_extractor(poem):
  secret_code = ''
  lines = poem.split('\n')
  for line_index, line in enumerate(lines):
    print(line_index, line)
    words = lines.split()
    print(words)

poem = '''Stars and the moon
shine in the sky
white and bright
until the end of the night'''

pin_extractor(poem)
