import webbrowser
import random
import requests
from lxml import html

pageisgood = False

print('If at any point you would like to exit, simply type exit\n\n\n')

wikipedia = 'https://en.wikipedia.org/wiki?curid='

while True:
    pageisgood = False
    while pageisgood == False:
    
        articlenum = random.randint(10,10000000)
        article = wikipedia + str(articlenum)
    
        page = requests.get(article)
        tree = html.fromstring(page.content)
        
        title = tree.xpath('//*[@id="firstHeading"]/text()')
        
        if title[0] == 'Bad title' or ':' in title[0]:
            pageisgood = False
            
        else:
            pageisgood = True
            
    
            
    print('would you like to read about',title[0],'? \n\nIf yes, type yes\n if no, press enter\n\n')        
            
    decision = input()
    
    if decision == 'yes':
        
        webbrowser.open(article)
        
    if decision == 'exit':
        break
        
        
