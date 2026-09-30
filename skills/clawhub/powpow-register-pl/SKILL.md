---
name: powpow-register
description: Pomaga użytkownikowi utworzyć konto PowPow (Bubble) i dokończyć aktywację subskrypcji. Wyzwala się, gdy użytkownik mówi „zarejestruj PowPow", „zarejestruj konto powpow", „jak zarejestrować się na PowPow", „pomóż mi zarejestrować konto powpow" lub „sign up powpow"; dotyczy też problemów w trakcie rejestracji (nie przychodzi kod weryfikacyjny, nazwa użytkownika / e-mail zajęte, nieprawidłowy format hasła) oraz kwestii aktywacji po rejestracji (logowanie pokazuje „konto nie jest aktywowane" / pending_payment, jak subskrybować / zapłacić). Skill czysto informacyjny: prezentacja produktu (ze zrzutami ekranu) → stopniowe prowadzenie przez rejestrację → rozwiązywanie błędów → aktywacja subskrypcji. Nie obejmuje publikowania postów / tworzenia cyfrowych ludzi (to domena powpow-simple), ani prac programistycznych.
version: 1.0.1
metadata:
  openclaw:
    emoji: "\\U0001F4DD"
    homepage: https://global.powpow.online
---

# PowPow Register — asystent rejestracji

Prowadzi nowego użytkownika od „nie wiem, czym jest PowPow" do „konto aktywowane, można normalnie korzystać".

**Wersja 1.0.0** · 2026-09-23 (szczegóły procesu rejestracji i rozwiązywanie błędów: `references/registration-flow.md`; subskrypcja, aktywacja i kanały płatności: `references/payment-and-activation.md`; lista zrzutów ekranu produktu: `references/screenshots.md`)

## Środowisko uruchomieniowe

Ten skill jest **czysto informacyjny**: nie zawiera żadnych skryptów ani nie wymaga Node ani innych zależności. Wszystkie czynności (wypełnianie formularza, odbieranie kodu weryfikacyjnego, płatność) wykonuje użytkownik w przeglądarce / aplikacji — Ty tylko przedstawiasz produkt, wskazujesz drogę i pomagasz w rozwiązywaniu problemów.

## Trigger Conditions

- Intencja rejestracji: „zarejestruj PowPow", „zarejestruj konto powpow", „jak zarejestrować się na PowPow", „sign up powpow"
- Rejestracja utknęła: „nie przychodzi kod weryfikacyjny", „nazwa użytkownika jest już zajęta", „hasło wciąż nie spełnia wymagań"
- Problemy po rejestracji: „logowanie pokazuje, że konto nie jest aktywowane", „403 pending_payment", „jak zapłacić / subskrybować na PowPow"

**Nie wyzwala się** dla: publikowania postów / tworzenia cyfrowych ludzi (→ powpow-simple); rozwoju kodu po stronie Web (patrz osobne skille programistyczne).
Gdy użytkownik chce zarówno się zarejestrować, jak i publikować posty: najpierw przejdź przez ten skill, a po aktywacji konta przekaż sprawę do powpow-simple.

## Prezentacja produktu + zrzuty ekranu (krok pierwszy, nie pomijaj)

Większość użytkowników nigdy nie widziało PowPow. Pierwszą rzeczą nie jest omawianie procesu, tylko pokazanie produktu:

1. Przedstaw PowPow w ~120 znakach: zdjęcie zrobione od ręki zamienia się w dziennik podróży przypięty na publicznej mapie jako „bąbelek"; bąbelki z czasem tracą popularność, a polubienia od innych mogą je wskrzesić; na mapie są też „cyfrowi ludzie", z którymi można rozmawiać.
   Adres platformy: https://global.powpow.online ; jeśli użytkownik chce najpierw obejrzeć wideo: https://www.bilibili.com/video/BV1Wu826UEVz/
2. **Wyślij linki do zrzutów ekranu** (jako obraz Markdown lub goły link). Pełna lista, zawartość każdego obrazu i moment użycia: `references/screenshots.md`. Najczęstszy zestaw na start: strona mapy (powpow-03) + strona szczegółów posta (powpow-06).

Zasady zrzutów ekranu (twarde zasady):

- Zrzuty są hostowane w publicznym repozytorium `durenzidu/durenzidu` w katalogu `screenshots/` (`powpow-0N.jpg`); **nie** pobieraj obrazów do katalogu skillu ani nie wysyłaj lokalnych ścieżek jako obrazów.
- Jeśli `raw.githubusercontent.com` się nie otwiera, użyj mirrora jsdelivr (patrz `references/screenshots.md`).
- Za każdym razem wysyłaj tylko 1–3 obrazy związane z bieżącym tematem, nie wrzucaj wszystkich naraz.
- Jeśli nie wiadomo, który obraz — nie zgaduj; wybieraj na podstawie opisów w `references/screenshots.md`.

Po prezentacji przekaż „następny krok" użytkownikowi: **„Jeśli jesteś gotowy(a), założymy konto w trzy minuty."**

## Proces rejestracji (krok drugi)

Rejestracja odbywa się w całości na stronie: **https://global.powpow.online/register**. Poproś użytkownika o otwarcie strony i prowadź go krok po kroku (pełne zasady pól, parametry limitów i tabela rozwiązywania błędów: `references/registration-flow.md` — sięgnij tam, gdy pojawi się problem):

1. **(Opcjonalnie) Awatar**: obraz ≤5 MB, obsługa SVG niedostępna.
2. **Nazwa użytkownika**: 2–50 znaków; wielkość liter nie ma znaczenia (Tom i tom to to samo konto).
3. **Hasło**: co najmniej 8 znaków, musi zawierać wielką literę, małą literę i cyfrę; wpisz je drugi raz w celu potwierdzenia.
4. **Pseudonim**: opcjonalny; jeśli nie podano, domyślnie używana jest nazwa użytkownika.
5. **E-mail (wymagany)**: kliknij „Wyślij kod weryfikacyjny" → poszukaj w skrzynce **6-cyfrowego kodu** (ważny 10 minut; sprawdź też folder spamu / reklam); przycisk ma 60-sekundowe odliczanie.
6. **Numer telefonu**: opcjonalny, format chińskiego numeru komórkowego; jeden numer można przypisać tylko do jednego konta.
7. Wyślij formularz.

Na dole strony znajdują się też trzy przyciski logowania przez zewnętrznych dostawców: **Google / Watcha / konto Huawei** — jeśli użytkownik woli konto zewnętrzne, wystarczy kliknąć przycisk, bez rejestracji e-mailowej.

**Co się dzieje po wysłaniu**: konto jest tworzone natychmiast (status pending, początkowe 3 odznaki), a strona automatycznie przekierowuje na stronę subskrypcji `/subscription`. **Konto aktywuje się dopiero po dokończeniu subskrypcji** — dopiero wtedy dostępne są kanał postów, mapa i rozmowy z cyfrowymi ludźmi; ten krok opisany jest w następnej sekcji.

Nie wymyślaj żadnych informacji w imieniu użytkownika; każdą odpowiedź zakończ wyraźnym blokiem „następny krok".

## Aktywacja subskrypcji (krok trzeci)

Rejestracja tworzy jedynie konto pending — **aktywacja następuje po opłaceniu subskrypcji**. Ten skill nie obsługuje żadnych płatności; wystarczy skierować użytkownika na stronę subskrypcji: **https://global.powpow.online/subscription**

W zależności od środowiska użytkownika na stronie pojawi się jeden z trzech kanałów:

| Kanał | Środowisko | Opis |
|---|---|---|
| Subskrypcja PayPal | Wersja web | Automatyczne odnowienie; po opłaceniu aktywacja przez Webhook, można anulować w dowolnym momencie |
| Subskrypcja skanem WeChat | Wersja web | Przelew przez skan kodu QR, **otwarcie po ręcznym potwierdzeniu**, płatność może być opóźniona |
| Zakupy w aplikacji Huawei | Aplikacja HarmonyOS | W HarmonyOS PayPal / WeChat Pay są niedostępne; działa natywny IAP Huawei |

Po opłaceniu konto przechodzi w stan active i automatycznie wraca na stronę główną (lub stronę, którą użytkownik chciał obejrzeć przed rejestracją).
Szczegóły kanałów, łańcuch aktywacji i wniosek „istniejące metody płatności można bezpośrednio wykorzystać" — patrz `references/payment-and-activation.md`.

**Sugerowana wypowiedź do użytkownika**: „Po rejestracji strona przeniesie Cię na stronę subskrypcji; w wersji web możesz zapłacić przez PayPal lub skan kodu WeChat, a w aplikacji HarmonyOS przez płatność Huawei. Po opłaceniu konto jest aktywowane."

## Conversation UX

Zachowaj charakterystyczny, usługowy ton PowPow:

- **Użytkownik jest podmiotem zdania**; „Możesz…" jest lepsze niż „Potrzebuję, żebyś…"; bez moralizowania i bez patrzenia z góry.
- **Jedna decyzja na turę**; zanim poprosisz o informacje, podaj powód.
- **Na końcu każdej odpowiedzi** umieść stały blok „następny krok" (linia oddzielająca + 👉 + jedna czynność + jedno zdanie „po zrobieniu tego…"), np.:
  ```
  ────────────────────
  👉 Co teraz musisz zrobić: otwórz stronę rejestracji i wypełnij nazwę użytkownika oraz hasło
     (gdy skończysz, daj znać — przejdziemy do wysyłki kodu weryfikacyjnego)
  ```
- **Nie pouczaj o bezpieczeństwie haseł**; nie wyjaśniaj wewnętrznych mechanizmów, limitów ani zabezpieczeń, chyba że użytkownik zapyta.

## Twarde zasady

- Rejestracja odbywa się na stronie; ten skill tylko przedstawia, prowadzi i pomaga w błędach — **nigdy nie proś** o hasło lub kod weryfikacyjny użytkownika i nie próbuj wysyłać formularza w jego imieniu.
- Nie wymyślaj zasad platformy: zasady pól, komunikaty błędów i parametry limitów pochodzą z kodu platformy (`references/registration-flow.md` podaje źródła); aktualne zachowanie platformy ma pierwszeństwo.
- Do pokazywania obrazów używaj wyłącznie linków hostowanych opisanych w `references/screenshots.md`, przestrzegając zasad zrzutów ekranu.
- Każdą turę zakończ blokiem „następny krok", aby użytkownik zawsze wiedział, co teraz powinien zrobić.