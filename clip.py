import pyperclip

oldClip = pyperclip.paste()

while True:

	if oldClip != pyperclip.paste() and pyperclip.paste() != "":
		
		oldClip = pyperclip.paste()
		pyperclip.copy(oldClip.replace('\n',' ').replace('\r',' '))
