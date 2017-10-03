alphabet = ['a', 'b', 'c', 'd', 'e', 'f']
code = [ ]
print('Code input type')
default = input()
if default == 'default':
  code = ['1', '2']
else:
  for letter in alphabet:
    print(letter + ':')
    num = input()
    code+= num
print(code)
lettercode = dict(zip(alphabet, code))
print(lettercode)
print('type secret message:')
message = input()
message = list(message.lower())
nummessage = [ ]
print(message)
for character in message:
  print(message[character - 1])
