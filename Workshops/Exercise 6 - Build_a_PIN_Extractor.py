# The nth digit of the pin is hidden as the length of the nth word in the nth line
def pin_extractor(poem):
  secret_code = ''
  lines = poem.split('\n')
  for line in lines:
    print(line)
    words = lines.split()
    print(words)

poem = '''Stars and the moon
shine in the sky
white and bright
until the end of the night'''

pin_extractor(poem)
