A = input('File name: ')
if A.endswith('.gif'):
   print('image/gif')
elif A.endswith('.jpg') or A.endswith('.jpeg'):
   print('image/jpeg')
elif A.endswith('.png'):
   print('image/png')
elif A.endswith('.pdf'):
   print('application/pdf')
elif A.endswith('.txt'):
   print('text/plain')
elif A.endswith('.zip'):
   print('application/zip')
else:
   print('application/octet-stream')
