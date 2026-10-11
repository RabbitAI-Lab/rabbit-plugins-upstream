# Proces załatwiania przez agenta i kontrakt skryptu — powpow-register

Szczegóły wykonania każdego kroku ze SKILL.md. Wszystkie polecenia mają postać `node scripts/powpow-register.mjs
<podpolecenie> [argumenty]`; skrypt ma **zero zależności**, wymaga **Node ≥ 18**, a wszystkie zapytania idą
wyłącznie do `https://global.powpow.online`.

## Projekt bezpieczeństwa (dlaczego tak)

| Rozwiązanie | Powód |
|---|---|
| Hasło wchodzi tylko przez zmienną środowiskową `POWPOW_REGISTER_PASSWORD` | Argumenty wiersza poleceń procesu są widoczne dla innych procesów na tej samej maszynie (powierzchnia wycieku argv); zmienną środowiskową skrypt czyta i od razu używa |
| Hasło **nigdy nie trafia do pliku stanu**, nigdy nie pojawia się w logach | Plik stanu może zostać na dysku; w trybie generowania w rozmowie pokazywany jest raz, żeby użytkownik zapisał |
| Plik stanu w systemowym katalogu tymczasowym (`os.tmpdir()/powpow-register-state.json`, 0600) | Zawiera tylko pięć pól email / username / nickname / token / outTradeNo; `cleanup` czyści jednym ruchem |
| JWT zdobyty przez agenta jest wymieniany na cookie przeglądarki przez oficjalny endpoint `me?token=` | Oficjalny mostek platformy zaprojektowany pod WebView HarmonyOS; weryfikacja podpisu sprawdza tylko podpis + termin ważności, nie wiąże odcisku urządzenia, więc przeglądarka użytkownika może go użyć |
| Płatność to tylko create-order / query / otwarcie kasy | Akt płatności i dowody płatności na zawsze zostają między użytkownikiem a oficjalną kasą Alipay, agent ich nie dotyka |

## Spis poleceń

| Polecenie | Kluczowe argumenty | Działanie / moment |
|---|---|---|
| `status` | —— | Podgląd postępu procesu (czyta plik stanu); po przerwaniu rozmowy uruchom najpierw to |
| `gen-password` | —— | Generuje mocne hasło 24-znakowe (wielkie + małe litery + cyfry); stdout pokazuje je **tylko ten jeden raz** |
| `prepare-suggest` | `--username --nickname --email` | Zapisuje potwierdzone dane do pliku stanu (potem register nie musi ich wysyłać ponownie) |
| `send-code` | `--email` | Wyzwala wysyłkę 6-cyfrowego kodu weryfikacyjnego (ważny 10 minut, cool down 60 s) |
| `register` | `--code` (wymagane); `--username --nickname --avatar --phone` (opcjonalne; jeśli są w pliku stanu, nie trzeba podawać) | Zakłada konto pending; hasło przez zmienną środowiskową `POWPOW_REGISTER_PASSWORD`; po sukcesie JWT automatycznie ląduje w pliku stanu |
| `login-link` | `--target pending` albo `--target home` | Generuje link logowania jednym kliknięciem (projekt podwójnego linku, patrz niżej) |
| `create-order` | `--package monthly\|quarterly\|yearly` | Tworzy zamówienie Alipay; zwraca ścieżkę pliku strony płatności + outTradeNo (automatycznie zapisywane do pliku stanu) |
| `query` | —— | Sprawdza status zamówienia `paid / pending / closed / unknown` (outTradeNo brany z pliku stanu), odpytywanie co 10–15 s |
| `refresh-login` | hasło przez zmienną środowiskową | Ponowne logowanie na **nowy JWT** (claim subskrypcji przechodzi z NONE na ACTIVE); po zaksięgowaniu płatności obowiązkowo uruchomić |
| `whoami` | —— | Tokenem z pliku stanu sprawdza konto i status subskrypcji (weryfikacja, czy aktywacja zaskoczyła) |
| `cleanup` | —— | Usuwa plik stanu (obowiązkowo na zamknięciu) |

**Przekazywanie zmiennej środowiskowej** (hasło nigdy nie wchodzi na wiersz poleceń):

```bash
# bash / zsh / WSL
POWPOW_REGISTER_PASSWORD='<hasło>' node scripts/powpow-register.mjs register --code 123456
# PowerShell
$env:POWPOW_REGISTER_PASSWORD = '<hasło>'; node scripts/powpow-register.mjs register --code 123456
# cmd
set POWPOW_REGISTER_PASSWORD=<hasło> && node scripts/powpow-register.mjs register --code 123456
```

## Mechanizm podwójnego linku (rdzeń projektu)

Stanem logowania platformy jest cookie HttpOnly — agent nie może sam posadzić cookie w przeglądarce
użytkownika; mostkiem jest oficjalny endpoint `/api/auth/me?token=<JWT>&redirect=<ścieżka w obrębie
serwisu>`: weryfikacja podpisu → dla użytkownika pending sesja jest automatycznie doprawiana → `Set-Cookie:
powpow_token` (HttpOnly / SameSite=Lax / 7 dni) → walidacja redirect (tylko pojedynczy ukośnik na początku,
zakaz `//` i backslasha, po rozwinięciu musi być same-origin) → 307 tymczasowe przekierowanie na stronę
docelową.

- **Link 1 (dawany od razu po udanej rejestracji)**: `--target pending` → ląduje na `/subscription`.
  Przeglądarka użytkownika wchodzi w stan „półzalogowania": strona subskrypcji i strona powrotu Alipay są
  widoczne i obsługiwane; strony treści nadal są przez paywall odsyłane z powrotem na stronę subskrypcji
  (trzy warstwy: kontrola claimów JWT w bramie → ponowny sprawdzian w bazie → kontrola w rdzeniowych API;
  zachowanie normalne).
- **Link 2 (dawany po potwierdzeniu paid)**: najpierw `refresh-login` na nowy JWT (płatność aktualizuje tylko
  bazę, nie zmienia claimów już wydanego JWT; bez wymiany będzie wyglądać jak „zapłacone, a nie ma
  członkostwa"), potem `--target home` → ląduje na stronie głównej, z pełnym stanem członkostwa.

## Pełna sekwencja (ścieżka normalna)

```
1.  status                          # Samokontrola środowiska
2.  (Krok 2: potwierdzenie danych w rozmowie, hasło z dwóch wariantów; tryb generowania: gen-password → niech użytkownik od razu zapisze)
3.  prepare-suggest --username U --nickname N --email E
4.  send-code --email E             # → użytkownik idzie do skrzynki po kod (jedyny punkt wyjścia z rozmowy ①)
5.  POWPOW_REGISTER_PASSWORD=*** register --code 123456 [--avatar pic.jpg]
6.  login-link --target pending     # → link 1 wysłany do użytkownika
7.  (użytkownik wybiera pakiet) create-order --package monthly
8.  start <plik strony płatności>   # Windows; macOS: open, Linux: xdg-open
    # → użytkownik płaci w kasie Alipay (punkt wyjścia z rozmowy ②)
9.  query (co 10–15 s) aż do paid
10. refresh-login                   # Nowy JWT z claimem ACTIVE
11. login-link --target home        # → link 2 wysłany do użytkownika
12. whoami                          # Potwierdzenie subscriptionStatus: ACTIVE (opcjonalnie)
13. cleanup                         # Czyszczenie pliku stanu
```

## Mapowanie: polecenie → API platformy

| Polecenie skryptu | Interfejs platformy |
|---|---|
| `send-code` | `POST /api/auth/register/send-code` |
| `register` | `POST /api/auth/register` (multipart, bezpośrednie wgranie avatara) |
| `login-link` | `GET /api/auth/me?token=…&redirect=…` (sam link; zadziała po kliknięciu w przeglądarce) |
| `create-order` | `POST /api/payment/alipay/create-order` (Bearer) |
| `query` | `GET /api/payment/alipay/query?outTradeNo=…` (Bearer) |
| `refresh-login` | `POST /api/auth/login` (`{step:1, username, password}`) |
| `whoami` | `GET /api/auth/me?token=…` |

Źródła reguł: pola rejestracji i limity w `registration-flow.md`; pakiety i łańcuch aktywacji w
`payment-and-activation.md` (oba podają pliki kodu platformy).

## Obsługa błędów na poziomie skryptu

| Objaw | Postępowanie |
|---|---|
| `Node 版本过低` (wersja Node zbyt niska) | Powrót do trybu czystych wskazówek, nie forsuj |
| Błąd sieci / timeout | Jedna ponowna próba; przy dalszej porażce niech użytkownik sprawdzi sieć i idziemy dalej (plik stanu istnieje — od początku uruchom `status`, żeby odzyskać) |
| register zwraca błąd biznesowy (nazwa użytkownika zajęta itd.) | Obsłuż wg tabeli z kroku 5 SKILL.md, **kodu weryfikacyjnego nie trzeba wysyłać ponownie** (wciąż ważny 10 minut) |
| register zwraca 「邮箱验证码错误或已过期」 (kod weryfikacyjny błędny lub wygasł) | Minął termin → `send-code` ponownie |
| Po `create-order` użytkownik zamknął stronę płatności | Po prostu ponów `create-order` (stare zamówienie zamknie się samo po 2 h) |
| `query` wciąż pending | Użytkownik mógł nie zapłacić; zapytaj jednym zdaniem. Jeśli zapłacił → idź wg tabeli w payment-and-activation.md |
| `refresh-login` 403 `pending_payment` | Płatność jeszcze nie zaksięgowana; wróć do kroku 9 i odpytuj dalej |
| Zgubiony plik stanu (przypadkiem usunięty / inna maszyna) | `whoami`/`refresh-login` nie zadziałają; niech użytkownik w przeglądarce, w której otwierał link 1, odświeży stronę subskrypcji, żeby potwierdzić stan, albo zaloguje się ponownie (tryb webowy) |

## Tryb awaryjny (czyste wskazówki)

Przy dowolnym z poniższych natychmiast wracaj do czystych wskazówek w stylu v1 i przestań męczyć skrypt:

- Brak Node ≥ 18 albo dwie porażki skryptu tego samego typu z rzędu;
- Użytkownik wprost mówi „zrobię to sam w przeglądarce";
- Polityka firmy/urządzenia blokuje skryptowi dostęp do sieci.

Po cofnięciu: daj stronę rejestracji https://global.powpow.online/register i stronę subskrypcji
https://global.powpow.online/subscription , prowadź rozwiązywanie błędów wg reguł `registration-flow.md`,
ton bez zmian, każda tura nadal kończy się blokiem „następny krok".
