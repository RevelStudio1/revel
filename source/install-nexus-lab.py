from pathlib import Path
d=Path(__file__).parent/'dist/prace/nexus'
p=d/'index.html';s=p.read_text()
if 'id="intake"' not in s:
 s=s.replace('<section class="crm-intro wrap">',Path(__file__).with_name('nexus-intake-section.html').read_text()+'<section class="crm-intro wrap">')
 s=s.replace('<script src="app.js" defer></script>','<script src="app.js" defer></script><script src="intake-core.js" defer></script><script src="intake.js" defer></script>')
 s=s.replace('<link rel="stylesheet" href="style.css">','<link rel="stylesheet" href="style.css"><link rel="stylesheet" href="intake.css">')
 s=s.replace('<a href="#automatyzacja">Automatyzacja</a>','<a href="#intake">Automation Lab</a>')
p.write_text(s)
p=d/'app.js';s=p.read_text()
if 'nexus-intake-saved' not in s:
 s+="\nwindow.addEventListener('nexus-intake-saved',()=>{leads=App.read('pw-nexus-v1',leads);render()});\nif(App.read('pw-nexus-v1',null)===null)App.save('pw-nexus-v1',leads);\n"
p.write_text(s)
