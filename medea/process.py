import re

def dashrepl(matchobj):
    return '<label for="'+matchobj.group(1)+'" class="margin-toggle sidenote-number"></label><input type="checkbox" id="'+matchobj.group(1)+'" class="margin-toggle"/><span class="sidenote">'+notes_dict[matchobj.group(1)]+'</span>'
    
with open('medea.html') as file:
       lines = [line for line in file]

cpt=0

while True:
    if 'footnote-back' in lines[cpt]:
        break
    cpt+=1
    if cpt > 10000:
        raise ValueError("Infinite loop")

ll = "".join(lines[cpt:]).replace('\n', ' ')
ll2 = re.sub(r'<li id="(fn.*?)"><p>', '#\\1#', ll)
ll3 = re.sub('<a.+?li>', '', ll2)
ll4 = re.sub('(.*)</ol>.*','\\1', ll3)  # note the lack of ? - we remove the last </ol> and anything after it

notes = ll4.split('#')[1:]
keyz = [x for x in notes[::2]]
valz = notes[1::2]

notes_dict = dict(zip(keyz, valz))

ll = "".join(lines[:cpt]).replace('\n', '@@')
ll2 = ll.replace('class="footnote-ref"', '')
ll3 = re.sub(r'id="fnref.*?"', '', ll2)
ll4 = re.sub(r'role="doc-noteref"><sup>.*?</sup></a>', '', ll3).replace('<a@@href', '<a href')
ll5 = re.sub(r'<section id="footnotes".*','', ll4)
#ll6 = ll5.replace('<a','').replace('<h2', '<br/><br/><h2').replace('SUMMARIUM', '<br/><br/>SUMMARIUM')
ll6 = ll5.replace('<h2', '<br/><br/><h2').replace('SUMMARIUM', '<br/><br/>SUMMARIUM')

ll6 = re.sub(r'<p>zz.*?zz</p>', 'zzzz', ll6)
ll6 = ll6.replace('zzzz','<figure><center><h1><small>L. ANNAEI SENECAE</small><br/>MEDEA</h1><p class="subtitle">CUM NOTIS MINIMIS AD INTELLIGENDUM SUFFICIENTIBUS</p></center></figure><br/>').replace('<h3', '<br/><h3')

ll7 = re.sub('<a href="#(.*?)"', dashrepl, ll6).replace(' <label', '<label').replace('@@<label', '<label').split('@@')



header = '''<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8"/>
    <title>Medea</title>
    <link rel="stylesheet" href="tufte.css"/>
    <meta name="viewport" content="width=device-width, initial-scale=1">
  </head>

  <body>
    <article>
    <section>
    '''
n1 = '<label for="fn1" class="margin-toggle sidenote-number"></label><input type="checkbox" id="fn1" class="margin-toggle"/><span class="sidenote">Dei</span>'

print(header)
for l in ll7:
    print(l)
print('</section></article></body>')
