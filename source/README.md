# REVEL — Digital Studio
Wspólna strona Patryka Wojnara i Ignacego Żurawskiego. HTML/CSS/JavaScript, bez kompilacji frontendu.

## Uruchomienie
Opublikuj zawartość dist/ na hostingu statycznym. index.html ma być w katalogu głównym publikacji. Projekty mają oddzielne adresy /prace/forma/, /prace/offgrid/, /prace/tempo/, /prace/nexus/, /prace/pulse/, /prace/studio/, /prace/flow/, /prace/atlas/.

## Generowanie
python3 build.py — główne strony, na podstawie revel-content.json oraz tekstów w generatorze.
python3 expand.py — opcjonalnie odtwarza pięć nowszych demonstracji; uruchamia rozszerzenie Automation Lab i branding.
python3 brand-projects.py — ujednolica podpisy projektów pod REVEL.
python3 package-projects.py — słownik PL/EN i osobne paczki demonstracji.
Źródłami dla pozostałych aplikacji są ich pliki w dist/prace/. Nie usuwaj dist przed generowaniem.

## Kontakt
Aktywny kontakt: kontakt.revel.studio@gmail.com, +48 502 317 200 (Patryk).
Propozycja firmowego adresu: hello@revel.studio. Nie sprawdzono dostępności domeny; adres nie został utworzony. Nie zastępuj kontaktu, zanim skrzynka nie działa.
Nowa nazwa konta GitHub: np. revel-studio, jeśli dostępna. Repozytorium strony użytkownika musi mieć nazwę dokładnie LOGIN.github.io. Nie ma potrzeby instalowania pakietów.
Dane rejestrowe i forma prawna spółki nie zostały podane. Strona używa REVEL jako marki; nie wymyśla numerów KRS/NIP ani oznaczenia sp. z o.o.

## Funkcjonalność
Projekty demonstracyjne, nie zamówienia ani płatności. Dane aplikacji pozostają w localStorage. Zachowano klucze pw-* dla kompatybilności.
Nexus Automation Lab: reguły PL/EN oraz opcjonalny model przeglądarki przez Prompt API, tylko EN, na zgodnym komputerze. AI nie działa na każdym telefonie. Podstawowy proces regułowy pozostaje dostępny. Nic nie jest wysyłane automatycznie.
Telefon Tempo to interaktywny prototyp web, nie emulator ani natywna aplikacja iOS.

## Kontrola jakości
Kontrola składni JS, lokalnych linków, ID i testy obliczeń. Mobilny CSS: widoki 320px+, menu, formularze 16px, przyciski 44px, siatki responsywne, ograniczenie ruchu. Przeglądarka do testu wizualnego nie była dostępna; nie potwierdzono działania na fizycznym iPhone/Android. Model AI nie był testowany na rzeczywistym urządzeniu.
