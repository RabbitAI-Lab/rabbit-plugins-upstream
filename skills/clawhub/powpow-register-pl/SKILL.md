---
name: powpow-register
description: Pomaga użytkownikowi dokończyć w rozmowie rejestrację PowPow (Bańka), aktywację subskrypcji Alipay lub PayPal i logowanie jednym kliknięciem. Agent wypełnia formularz w jego imieniu (łącznie z wgrywaniem avatara), wysyła kod weryfikacyjny e-mailem, tworzy zamówienie płatności i śledzi księgowanie; użytkownik podaje tylko podstawowe dane, raz zagląda do skrzynki po kod i płaci w kasie Alipay lub PayPal — bez wychodzenia z rozmowy. Wyzwalane zdaniami „zarejestruj Bańkę", „załóż konto powpow", „jak się rejestruje w Bańce", „pomóż mi założyć konto powpow", „sign up powwow"; obsługuje też utknięcie rejestracji (kod nie dochodzi, nazwa użytkownika/e-mail zajęte) i problemy z aktywacją (login mówi „konto nieaktywne" / pending_payment, jak opłacić subskrypcję). Wymaga Node ≥ 18; przy braku automatycznie przechodzi w tryb czystych wskazówek. Nie obejmuje publikowania postów/tworzenia cyfrowych ludzi (to robota powpow-simple) ani developmentu kodu.
version: 2.1.0
metadata:
  openclaw:
    emoji: "\U0001F4DD"
    homepage: https://global.powpow.online
---

# PowPow Register (asystent rejestracji w Bańce)

Przeprowadzamy nowego użytkownika od „nie wiem, czym jest Bańka" do „konto aktywne, logowanie jednym kliknięciem, można zaczynać" — w całości w rozmowie. Użytkownik tylko dwa razy musi na chwilę wyjść z rozmowy: **wejść do skrzynki e-mail po kod weryfikacyjny** i **zapłacić w kasie** (Alipay lub PayPal — agent sam otworzy stronę kasy).

**Wersja 2.1.0** · 2026-10-11 (od v2 tryb agenta działającego w imieniu użytkownika: kontrakt skryptu i pełna sekwencja w `references/agent-flow.md`; reguły pól, limity i rozwiązywanie błędów w `references/registration-flow.md`; kanały płatności w `references/payment-and-activation.md`; lista zrzutów ekranu produktu w `references/screenshots.md`. Od v2.1.0 subskrypcje PayPal też może obsługiwać agent, jako opcję obok Alipay)

## Środowisko uruchomieniowe

- Skrypt główny `scripts/powpow-register.mjs`: **zero zależności**, wymaga **Node ≥ 18**. Przed startem uruchom raz `node scripts/powpow-register.mjs status`, żeby potwierdzić, że środowisko działa.
- Wszystkie zapytania skryptu idą wyłącznie do oficjalnej domeny `https://global.powpow.online`.
- **Brak Node'a / błąd skryptu**: automatyczny powrót do trybu czystych wskazówek — daj użytkownikowi stronę rejestracji https://global.powpow.online/register i stronę subskrypcji https://global.powpow.online/subscription i prowadź go według `references/registration-flow.md`. Nie ponawiaj na siłę kolejnych prób skryptu.
- Wznowienie po przerwaniu rozmowy: najpierw `status`, żeby zobaczyć, na którym kroku utknęło, potem idź dalej.

## Trigger Conditions

- Zamiar rejestracji: „zarejestruj Bańkę", „załóż konto powpow", „jak się rejestruje w Bańce", „sign up powpow"
- Rejestracja utknęła: „kod weryfikacyjny nie dochodzi", „mówi, że nazwa użytkownika już istnieje", „hasło ciągle odrzucane"
- Problemy po rejestracji: „przy logowaniu mówi, że konto nieaktywne", „403 pending_payment", „jak zapłacić/wykupić subskrypcję w Bańce"

**Nie wyzwala się dla**: publikowania postów/tworzenia cyfrowych ludzi (→ powpow-simple); developmentu kodu po stronie Web (osobny skill deweloperski). Gdy użytkownik chce się rejestrować i od razu publikować: najpierw dokończ ten skill, po aktywacji przekaż do powpow-simple.

## Przegląd procesu

| Krok | Co robi agent | Co robi użytkownik |
|---|---|---|
| 1 Prezentacja produktu | Przedstawia + wysyła zrzuty | Rzuca okiem |
| 2 Potwierdzenie danych | Proaktywnie proponuje nazwę użytkownika/pseudonim, hasło z dwóch wariantów, pyta o e-mail | Potwierdza, podaje dane |
| 3 Wysyłka kodu | `send-code` | —— |
| 4 Odczyt kodu | —— | Wchodzi do skrzynki, odczytuje 6-cyfrowy kod, odsyła go |
| 5 Zgłoszenie rejestracji | `register` (z bezpośrednim wgraniem avatara), błędy obsługuje automatycznie | —— |
| 6 Półzalogowanie + płatność | `login-link(pending)` → `create-order --provider alipay|paypal` → otwiera kasę → odpytuje `query` | Klika link, płaci |
| 7 Pełne logowanie | `refresh-login` → `login-link(home)` | Klika link i wchodzi na stronę główną |
| 8 Zamknięcie | `cleanup` + przekazanie danych konta + wprowadzenie do zabawy + polecenie wtyczki | Zaczyna zabawę |

## Krok 1: prezentacja produktu + zrzuty ekranu (nie pomijać)

Większość użytkowników nigdy nie widziała Bańki. Pierwsza rzecz to nie opowiadanie o procesie, tylko sprawienie, żeby produkt **zobaczyli**:

1. Przedstaw Bańkę w ~120 znakach: zamień przypadkowe zdjęcia w dziennik z podróży i przypnij go na publicznej mapie jako „bańkę"; bańka z czasem blaknie, czyjeś polubienie może ją wskrzesić; na mapie są też „cyfrowi ludzie", z którymi można rozmawiać. Adres platformy https://global.powpow.online , jeśli chcesz najpierw pokazać film: https://www.bilibili.com/video/BV1Wu826UEVz/
2. **Wyślij zrzuty ekranu**. Zrzuty są spakowane ze skillem w `assets/screenshots/powpow-0N.jpg` — wyślij bezpośrednio jako lokalne pliki obrazków, bez internetu. Lista, zawartość każdego zrzutu i moment użycia w `references/screenshots.md`. Najczęstszy zestaw na otwarcie: strona mapy (powpow-03) + strona szczegółów posta (powpow-06).

Zasady zrzutów (twarde zasady):

- Zrzuty **są spakowane ze skillem** w `assets/screenshots/` (`powpow-0N.jpg`) — wysyłaj bezpośrednio lokalne pliki; działa w każdym środowisku, także tam, gdzie GitHub jest nieosiągalny.
- Za jednym razem wyślij tylko 1–3 zrzuty związane z bieżącym tematem, nie wal wszystkiego naraz.
- Gdy plik w pakiecie zginie przypadkiem, fallback na linki hostingowe z `references/screenshots.md` (uwaga: z Chin kontynentalnych mogą się nie otwierać).

Po prezentacji oddaj wybór użytkownikowi: **„Jeśli chcesz się rejestrować, za trzy minuty założymy konto w tej rozmowie — musisz tylko raz zajrzeć do skrzynki po kod."**

## Krok 2: potwierdzenie danych rejestracji (jedno pytanie na turę, nie wypytuj wszystkiego naraz)

- **Nazwa użytkownika** (wymagana): **proaktywnie zaproponuj jedną** z kontekstu rozmowy/nazwy użytkownika systemu (2~50 znaków, bez rozróżniania wielkości liter); użytkownik kiwa głową — używamy, chce zmienić — zmieniamy.
- **Hasło** (wymagane; najpierw daj wybór z dwóch):
  - Użytkownik podaje własne → później trafi do skryptu przez zmienną środowiskową, **nigdy nie wpisuj go w argumenty wiersza poleceń**;
  - Generuje agent → uruchom `node scripts/powpow-register.mjs gen-password` i **natychmiast wyślij wygenerowane hasło użytkownikowi do zapisania** (pokazywane tylko ten jeden raz, potem już nie wraca).
- **E-mail** (wymagany): musi podać użytkownik — to kotwica tożsamości konta, **nie zgaduj za niego**.
- **Pseudonim** (opcjonalny): zaproponuj domyślnie taki sam jak nazwa użytkownika.
- **Avatar** (opcjonalny): jeśli użytkownik da ścieżkę lokalnego obrazka (≤5MB, nie SVG), skrypt wgra go bezpośrednio; nie ma — pomijamy (platforma użyje domyślnego logo); jeśli masz zdolność generowania obrazków, możesz zaproponować zrobienie jednego.
- **Numer telefonu** (opcjonalny, numer z Chin): domyślnie pomijamy; pytaj, tylko gdy użytkownik sam chce go powiązać.

Po potwierdzeniu możesz uruchomić `prepare-suggest --username U --nickname N --email E`, żeby zapisać dane do pliku stanu (potem register nie musi ich wysyłać ponownie).

## Kroki 3–4: kod weryfikacyjny e-mailem (jedyny punkt wymagający wyjścia z rozmowy)

```
node scripts/powpow-register.mjs send-code --email <e-mail>
```

Potem powiedz wyraźnie użytkownikowi: **wejdź do skrzynki e-mail, znajdź 6-cyfrowy kod weryfikacyjny, ważny 10 minut; zajrzyj też do folderu spam/oferty**; gdy znajdziesz, wróć i przyślij mi kod. Wysyłka ma 60-sekundowe cool down, nie klikaj w kółko.

## Krok 5: zgłoszenie rejestracji (załatwia agent)

```
POWPOW_REGISTER_PASSWORD=<hasło> node scripts/powpow-register.mjs register --code <kod> [--username U] [--nickname N] [--avatar <ścieżka lokalnego obrazka>] [--phone P]
```

Sukces = konto założone (stan pending, z 3 odznakami startowymi). Częste błędy obsługuje automatycznie, bez przerywania użytkownikowi:

| Błąd | Postępowanie |
|---|---|
| 「用户名已存在」 (nazwa użytkownika już istnieje) | Automatycznie zaproponuj wariant (nazwa + cyfry), po potwierdzeniu przez użytkownika od razu ponów (kod nadal ważny, nie trzeba wysyłać nowego) |
| 「邮箱已被使用」 (e-mail już używany) | Zapytaj użytkownika: podać inny e-mail, czy może jednak ma już konto (przejście na logowanie/odzyskiwanie hasła) |
| 「邮箱验证码错误或已过期」 (kod weryfikacyjny błędny lub wygasł) | Minęło ponad 10 minut → wyślij `send-code` ponownie |
| Zbyt częste wysyłanie/rejestracja (429) | Odczekaj 1 minutę i ponów; wystarczy jedno zdanie do użytkownika |

## Krok 6: logowanie jednym kliknięciem (link 1) + płatność

1. Zaraz po udanej rejestracji:
   ```
   node scripts/powpow-register.mjs login-link --target pending
   ```
   Wyślij link użytkownikowi: **po otwarciu przeglądarka ląduje wprost na stronie subskrypcji, już zalogowana** — dzięki temu po zapłaceniu strona powrotu poprawnie pokaże „płatność zakończona". (W tym stanie strony treści nadal są odsyłane do strony subskrypcji: to normalna praca paywalla platformy, nie bug, i nie trzeba tłumaczyć użytkownikowi mechaniki wewnętrznej.)
2. **Poproś użytkownika o wybór metody płatności** — pokaż oba kanały:
   - **Alipay (Chiny / użytkownicy z Alipay)**: jednorazowy zakup odpowiedniego okresu, **bez automatycznego odnawiania**
     - Miesięcznie **¥6.99** (polecany na start) / Kwartalnie **¥19.99** / Rocznie **¥69.99**
   - **PayPal (zagranica / bez Alipay)**: automatyczne odnawianie co miesiąc, rezygnacja w każdej chwili
     - Premium Monthly, ok. **$1/mies.** (zgodnie z tym, co pokazuje strona subskrypcji; automatyczne odnawianie)
3. Gdy użytkownik wybierze:
   - **Alipay**:
     ```
     node scripts/powpow-register.mjs create-order --package monthly
     ```
   - **PayPal**:
     ```
     node scripts/powpow-register.mjs create-order --provider paypal
     ```
   Skrypt zwróci ścieżkę pliku strony płatności; **otwórz ją bezpośrednio poleceniem systemowym** (Windows: `start <plik>`; macOS: `open <plik>`; Linux: `xdg-open <plik>`). Przeglądarka sama przejdzie do oficjalnej kasy Alipay lub PayPal, gdzie użytkownik sfinalizuje płatność albo autoryzację obciążenia.
4. Co 10–15 sekund uruchamiaj `query`, aż zwróci `paid` lub `ACTIVE` (księgowanie/autoryzacja zwykle trwa od kilku sekund do minuty). Jeśli użytkownik zamknie stronę płatności w trakcie → po prostu ponów `create-order` (stare zamówienia i wiszące subskrypcje zamykają się lub wygasają po 2 godzinach; nie przejmuj się nimi).
5. Kanał skanowania WeChat wymaga ręcznego potwierdzenia i księgowanie może się opóźnić; Huawei IAP działa tylko w aplikacji HarmonyOS. Tych dwóch skill nie załatwia — po zapłacie i tak wracają do kroku 7.

## Krok 7: pełne logowanie (link 2)

Po potwierdzeniu księgowania najpierw wymień stan logowania na z najnowszym claimem subskrypcji, dopiero potem wygeneruj link wprost na stronę główną:

```
POWPOW_REGISTER_PASSWORD=<hasło> node scripts/powpow-register.mjs refresh-login
node scripts/powpow-register.mjs login-link --target home
```

Wyślij link użytkownikowi: **po otwarciu ląduje wprost na stronie głównej, z pełnym stanem członkostwa** — i tu cały proces rejestracji jest zakończony.

## Krok 8: zamknięcie

1. `node scripts/powpow-register.mjs cleanup` czyści tymczasowy plik stanu na maszynie (dane sesji).
2. Daj użytkownikowi „kartę konta": nazwa użytkownika, e-mail, data wygaśnięcia członkostwa (hasło nie jest pokazywane ponownie — w trybie generowania użytkownik zapisał je przy tworzeniu; własne sam zna).
3. Wprowadzenie do zabawy: spacer po mapie, pierwszy dziennik z podróży (→ przekaż do powpow-simple).
4. Poleć rozszerzenia: skill `@durenzidu/powpow-integration` i wtyczka `@durenzidu/openclaw-channel-powpow` — podłączenie Bańki do własnego agenta użytkownika; jeśli chce, podaj polecenie instalacji.
5. Zamknij turę blokiem „następny krok".

## Conversation UX

Utrzymuj charakterystyczny dla powpow ton nastawiony na obsługę:

- **Użytkownik jest podmiotem zdania**; „możesz…" lepiej niż „muszę, żebyś…"; bez moralizowania, bez zadzierania nosa.
- **Jedna decyzja na turę**; zanim o coś poprosisz, podaj powód.
- **Na końcu każdej odpowiedzi** stoi stały blok „następny krok" (linia oddzielająca + 👉 + jedno działanie + jedno zdanie „gdy skończysz, ja…"), np.:
   ```
   ────────────────────
   👉 Teraz twoja kolej: wejdź do skrzynki, znajdź 6-cyfrowy kod i wyślij mi go od razu
      (gdy tylko dostanę kod, od razu założę ci konto)
   ```
- **Nie wygłaszaj nieproszonych kazan o bezpieczeństwie haseł**; nie tłumacz mechaniki wewnętrznej, limitów ani projektu bezpieczeństwa, chyba że użytkownik zapyta.
- Im bardziej agent działa w imieniu użytkownika, tym częściej melduj postęp: po każdym kroku skryptu jedno zdanie o tym, co właśnie się stało („konto założone", „stronę płatności już ci otworzyłem").

## Twarde zasady

- **Bezpieczeństwo poświadczeń**: hasło trafia do skryptu wyłącznie przez zmienną środowiskową `POWPOW_REGISTER_PASSWORD`, **nigdy** przez argumenty wiersza poleceń (widoczne w liście procesów) i nigdy do żadnego pliku (w trybie generowania pokazane raz, żeby użytkownik zapisał, potem nie wraca). Kod weryfikacyjny służy tylko oficjalnemu interfejsowi rejestracji i po użyciu przepada.
- **Granica oficjalności**: wszystkie zapytania idą wyłącznie do `https://global.powpow.online` (wbudowane w skrypt); nigdy nie wysyłaj danych użytkownika pod żaden adres trzeciej strony.
- **Granica płatności**: agent tylko tworzy zamówienie, otwiera kasę, sprawdza księgowanie; **nigdy** nie dotyka konta Alipay/PayPal/dowodów płatności użytkownika i nigdy nie obiecuje „zapłacenia za niego".
- **Paywall to nie bug**: dostęp stanu pending do strony subskrypcji/strony powrotu to świadome przepuszczenie w projekcie; blokowanie stron treści to normalna praca paywalla platformy, nie próbuj tego obchodzić.
- **Wolność cofnięcia**: gdy na dowolnym kroku użytkownik chce zrobić coś sam albo środowisko nie wspiera skryptu, w każdej chwili wracaj do trybu czystych wskazówek — daj linki, opowiedz zasady, rozwiązuj błędy razem z nim.
- Nie zmyślaj reguł platformy: reguły pól, teksty błędów i parametry limitów pochodzą w całości z kodu platformy (`references/registration-flow.md` podaje źródła); przy aktualizacji platformy obowiązuje rzeczywiste zachowanie.
- Do pokazywania obrazków używaj wyłącznie zrzutów z `assets/screenshots/` w pakiecie (zastosowania każdego zrzutu w `references/screenshots.md`).
- Każdą turę kończ blokiem „następny krok", żeby użytkownik zawsze wiedział, co ma teraz zrobić.
