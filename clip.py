import pyperclip
import re 
from plyer import notification

def notifyUser(linkClip):
    
     notification.notify(
            title = 'Link Inválido',
            message = 'O link {} ainda é inválido, espere o imgur finalizar o upload.'.format(linkClip),
            timeout  = 5
        )
     
def main():
    
    oldClip = pyperclip.paste()
    regexUrl = r"https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()@:%_\+.~#?&//=]*(png|jpg))"
    urlParsed = ''
    
    while True:
        try:
            
            if 'blob:' in pyperclip.paste() and pyperclip.paste() != "":
                
                notifyUser(pyperclip.paste())
                
                continue
            
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

if __name__ == '__main__':
    main()