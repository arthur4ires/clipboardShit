import pyperclip

oldClip = pyperclip.paste()

while True:

	if oldClip != pyperclip.paste():

		print(oldClip)

		oldClip = pyperclip.paste()
		pyperclip.copy(oldClip.replace('\n','').replace('\r',''))
