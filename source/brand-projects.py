from pathlib import Path
root=Path(__file__).parent
pairs=[('Interaktywny projekt demonstracyjny — Patryk Wojnar','Interaktywny projekt demonstracyjny — REVEL'),('← Moje portfolio','← REVEL'),('Projekt demonstracyjny Patryka Wojnara','Projekt demonstracyjny REVEL'),('projekt Patryka Wojnara','projekt REVEL'),('Projekt: Patryk Wojnar','Projekt: REVEL'),('© 2026 Patryk Wojnar','© 2026 REVEL'),('Pozdrawiam,\\nPatryk Wojnar','Pozdrawiam,\\nZespół REVEL'),('Best regards,\\nPatryk Wojnar','Best regards,\\nREVEL Team'),('-//Patryk Wojnar//','-//REVEL//')]
for p in (root/'dist/prace').rglob('*'):
 if p.suffix not in ['.html','.js']:continue
 if p.name=='translations.js':continue
 s=p.read_text()
 for a,b in pairs:s=s.replace(a,b)
 p.write_text(s)
for name in ['expand.py','nexus-intake-section.html','install-nexus-lab.py']:
 p=root/name;s=p.read_text()
 for a,b in pairs:s=s.replace(a,b)
 p.write_text(s)
p=root/'dist/assets/app.js';s=p.read_text().replace('Hi Patryk!','Hello REVEL!').replace('Cześć Patryk!','Cześć REVEL!');p.write_text(s)
p=root/'package-projects.py';s=p.read_text().replace('— Patryk Wojnar','— REVEL').replace('© 2026 Patryk Wojnar','© 2026 REVEL');p.write_text(s)
