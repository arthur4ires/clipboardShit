import pyperclip
import re 

oldClip = pyperclip.paste()
regexUrl = r"https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()@:%_\+.~#?&//=]*(png|jpg))"
urlParsed = ''

while True:
	
	try:

		if oldClip != pyperclip.paste() and pyperclip.paste() != "":
			
			oldClip = pyperclip.paste()

			newClip = oldClip.replace('\n',' ').replace('\r',' ').replace('⫹','').replace('- ','').replace('⫺','-')

			matches = re.finditer(regexUrl, newClip, re.MULTILINE)
			
			for a in enumerate(matches):
				
				urlParsed = a[1].group() 

			if urlParsed != newClip.replace(' ',''):
			
				pyperclip.copy(newClip)
			
			else:
			
				pyperclip.copy('![image]({})'.format(newClip))


	except AttributeError as e:
		print('Error: {}'.format(e))
		exit()
