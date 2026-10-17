# powpow-register

Asystent rejestracji PowPow Bańka (wersja OpenClaw): przeprowadza nowego użytkownika od „nie wiem, czym jest
Bańka" do „konto aktywne, logowanie jednym kliknięciem, zaczynamy" — prezentacja produktu (ze zrzutami
interfejsu), rejestracja załatwiana przez agenta (łącznie z wgrywaniem avatara), zamówienie subskrypcji Alipay/PayPal
i śledzenie księgowania, logowanie jednym kliknięciem na podwójnym linku, rozwiązywanie błędów.

**Od v2.0.0 tryb agenta działającego w imieniu użytkownika, od v2.1.0 także PayPal**: główny skrypt `scripts/powpow-register.mjs` zero
zależności (Node ≥ 18); użytkownik przez cały czas nie wychodzi z rozmowy, tylko dwa razy na chwilę: po kod do
skrzynki e-mail i na płatność w kasie Alipay lub PayPal. Bez Node'a albo gdy użytkownik chce działać sam — automatyczny
powrót do trybu czystych wskazówek.

## Instalacja

```
openclaw skills install @durenzidu/powpow-register
```

## Funkcje

1. **Prezentacja produktu**: otwarcie ~120 znaków + zrzuty interfejsu spakowane ze skillem (`assets/screenshots/`
   to 6 obrazków: strona mapy, strona szczegółów posta itd.; wybierz i wyślij 1–3 wg scenariusza; bez zewnętrznego
   hostingu, działa offline).
2. **Rejestracja załatwiana przez agenta**: agent proaktywnie proponuje nazwę użytkownika/pseudonim, hasło z dwóch
   wariantów (podaje użytkownik albo generuje agent), wysyłka i zgłoszenie kodu weryfikacyjnego, bezpośrednie
   wgranie avatara (≤5MB, nie SVG), automatyczna obsługa częstych błędów (zajęte/wygasłe/limity).
3. **Logowanie jednym kliknięciem (podwójny link)**: po udanej rejestracji od razu link „półzalogowania" prosto na
   stronę subskrypcji; po zaksięgowaniu płatności wymiana na nowy stan logowania i link z pełnym członkostwem
   prosto na stronę główną (przez oficjalny mostek `me?token=` platformy, automatycznie ustawia cookie HttpOnly).
4. **Płatność subskrypcji**: zarówno Alipay (miesięcznie ¥6.99 / kwartalnie
   ¥19.99 / rocznie ¥69.99, jednorazowy zakup bez automatycznego odnawiania), jak i PayPal (Premium Monthly, ok. $1/mies., automatyczne odnawianie, rezygnacja w każdej chwili) załatwia agent + odpytywanie o księgowanie;
   skanowanie WeChat/Huawei IAP tylko ze wskazaniem drogi.
5. **Rozwiązywanie błędów**: kod nie dochodzi, nazwa użytkownika/e-mail zajęte, 403 konto nieaktywne, konto
   zablokowane i inne częste problemy — wszystko z kodu platformy z podanymi źródłami.

## Struktura plików

```
powpow-register/
├── SKILL.md                            # Główny przewodnik (warunki wyzwolenia, proces 8 kroków, normy tonu, twarde zasady)
├── README.md
├── .clawhubignore
├── assets/
│   └── screenshots/                    # Zrzuty produktu w pakiecie (powpow-01~06.jpg)
├── scripts/
│   └── powpow-register.mjs             # Skrypt główny (zero zależności, Node≥18, 11 podpoleceń)
└── references/
    ├── agent-flow.md                   # Kontrakt skryptu, pełna sekwencja, mechanizm podwójnego linku, projekt bezpieczeństwa
    ├── registration-flow.md            # Reguły pól, limity, tabela rozwiązywania błędów (ze źródłami kodu)
    ├── payment-and-activation.md       # Kontrakt Alipay vibepay, łańcuch aktywacji, rozwiązywanie po kanałach
    └── screenshots.md                  # Lista zrzutów w pakiecie + ściąga scenariuszy
```

## Bezpieczeństwo

- **Hasło** wchodzi do procesu skryptu tylko przez zmienną środowiskową, nigdy jako argument wiersza poleceń,
  nie ląduje na dysku, nie wchodzi do pliku stanu; hasło wygenerowane przez agenta pokazywane jest raz, żeby
  użytkownik zapisał.
- **Kod weryfikacyjny** służy tylko oficjalnemu interfejsowi rejestracji, po użyciu przepada; plik stanu
  (e-mail/nazwa użytkownika/token/numer zamówienia) leży w systemowym katalogu tymczasowym, a po zakończeniu
  procesu `cleanup` czyści go jednym ruchem.
- **Płatność**: agent tylko tworzy zamówienie, otwiera kasę i sprawdza księgowanie; nigdy nie dotyka konta
  Alipay/PayPal ani dowodów płatności użytkownika, nigdy nie płaci za niego. Płatność zawsze odbywa się między
  użytkownikiem a oficjalną kasą.
- Wszystkie zapytania idą tylko do oficjalnej domeny `https://global.powpow.online`; nie zawiera żadnych kluczy.

## Licencja

MIT-0 (ujednolicona licencja ClawHub).

## Linki

- Strona oficjalna: https://global.powpow.online
- Rejestracja: https://global.powpow.online/register
- Poznaj Bańkę (film): https://www.bilibili.com/video/BV1Wu826UEVz/
