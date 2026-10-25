from pathlib import Path
import json,zipfile
base=Path(__file__).parent
root=base/'dist'
d={}
for line in (base/'translations.tsv').read_text().splitlines():
 if '|' in line:
  a,b=line.rsplit('|',1);d[a.strip()]=b.strip()
(root/'prace/shared/translations.js').write_text('window.TRANSLATIONS='+json.dumps(d,ensure_ascii=False)+';\n')
(root/'downloads').mkdir(exist_ok=True)
url='https://patryk-wojnar-portfolio-m8q2.violetfly3.chatgpt.site'
features={'forma':'Katalog, wyszukiwanie, filtrowanie, sortowanie, ulubione, szczegóły produktu, koszyk z ilościami, kod FORMA10, wybór dostawy, symulacja podsumowania, eksport TXT.','flow':'Tablica Kanban i lista zadań, tworzenie/edycja/usuwanie, statusy, priorytety, terminy, wyszukiwanie, statystyki, notatnik z autozapisem, timer 15/25/50 minut, eksport JSON.','atlas':'Podróż na 1–14 dni, daty i liczba osób, plan godzinowy, edycja punktów, oznaczanie wykonania, wydatki, budżet i koszt na osobę, pakowanie, eksport JSON.'}
features.update({'offgrid':'Sklep odzieżowy: katalog, rozmiary, ulubione, koszyk i eksport podsumowania.','tempo':'Rezerwacje: telefon, terminy bez kolizji, anulowanie i plik ICS.','nexus':'CRM i Automation Lab: analiza wiadomości, zatwierdzanie, historia, eksport, reguły oraz opcjonalne AI przeglądarki.','studio':'Strona studia fryzjerskiego połączona z rezerwacjami Tempo.','pulse':'Landing sprzedażowy z przełączanym cennikiem i podglądem planów.'})
for slug in features:
 with zipfile.ZipFile(root/'downloads'/f'{slug.title()}-PL-EN.zip','w',zipfile.ZIP_DEFLATED) as z:
  for p in (root/'prace'/slug).rglob('*'):
   if p.is_file():
    data=p.read_bytes()
    if p.suffix in ['.html','.js','.css']:data=p.read_text().replace('../shared/','shared/').replace('../../projekty.html',url+'/projekty.html').replace('../../kontakt.html',url+'/kontakt.html').replace('../../prywatnosc.html',url+'/prywatnosc.html')
    if p.suffix in ['.html','.js','.css']:
     for other in features:data=data.replace('../'+other+'/index.html',url+'/prace/'+other+'/index.html')
     data=data.encode()
    z.writestr(str(p.relative_to(root/'prace'/slug)),data)
  for p in (root/'prace/shared').rglob('*'):
   if p.is_file():
    if 'media' in p.parts and p.name not in {'forma':['store-hero.png','lamp.png','vase.png','table.png'],'atlas':['travel-hero.png'],'offgrid':['fashion.png','clothes.png']}.get(slug,[]):continue
    z.write(p,'shared/'+str(p.relative_to(root/'prace/shared')))
  z.writestr('README.md',f'''# {slug.title()} — REVEL\n\n{features[slug]}\n\nNowe projekty są demonstracjami lokalnymi. Nexus: tryb regułowy i opcjonalny model AI przeglądarki (Prompt API, EN, zgodny komputer). Tempo nie dokonuje rzeczywistych rezerwacji. Off/Grid nie przyjmuje zamówień. Łącza między projektami wymagają pełnej paczki portfolio.\n\n## Uruchomienie\nOtwórz index.html. Dla przewidywalnego zapisu localStorage uruchom przez lokalny serwer HTTP lub hosting statyczny (na file:// zachowanie pamięci zależy od przeglądarki). Nie wymaga instalacji pakietów ani kompilacji.\n\nPL/EN: przełącznik zapisuje wybór języka lokalnie. Treści wpisane przez użytkownika nie są automatycznie tłumaczone.\n\nDane aplikacji pozostają w localStorage tej przeglądarki. Nie ma kont, synchronizacji między urządzeniami ani serwera. Eksport JSON to kopia danych; aplikacja nie ma funkcji importu. Reset usuwa bieżące dane po potwierdzeniu. Timer Flow nie jest odtwarzany po odświeżeniu.\n\nSklep Forma jest demonstracją: bez prawdziwych zamówień, płatności, dostępności magazynowej i wysyłki. Produkty, ilustracje i ceny są przykładowe. Atlas nie dokonuje rezerwacji i nie podaje aktualnych rekomendacji podróżnych.\n\nKod: HTML, CSS, JavaScript. Wizualizacje produktów i krajobraz zostały wygenerowane do projektu. Brak zewnętrznych fontów i trackerów.\n\nSprawdzono składnię JavaScript, odnośniki, pokrycie tłumaczeń i testy obliczeń. Test w przeglądarce pozostał niedostępny z powodu infrastruktury podglądu — wykonaj go przed docelową publikacją.\n\n© 2026 REVEL.\n''')
print('8 standalone ZIPs created')
