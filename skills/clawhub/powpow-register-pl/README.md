# powpow-register

Asystent rejestracji PowPow (wersja OpenClaw): prowadzi nowego użytkownika od „nie wiem, czym jest PowPow" do „konto aktywowane, można normalnie korzystać" — prezentacja produktu (ze zrzutami ekranu), stopniowe prowadzenie przez rejestrację, rozwiązywanie błędów, objaśnienie aktywacji subskrypcji.

Skill czysto informacyjny, bez skryptów i bez zależności; wszystkie czynności rejestracyjne wykonuje użytkownik w przeglądarce / aplikacji.

## Instalacja

```
openclaw skills install @durenzidu/powpow-register
```

## Funkcje

1. **Prezentacja produktu**: otwarcie w ~120 znakach + linki do zrzutów ekranu hostowanych w publicznym repozytorium GitHub (strona mapy, strona szczegółów posta itp. — 6 obrazów, wysyłaj 1–3 w zależności od sceny).
2. **Prowadzenie przez rejestrację**: zasady pól (nazwa użytkownika / hasło / kod weryfikacyjny e-mail / numer telefonu / awatar), logowanie przez podmioty trzecie (Google / Watcha / Huawei), parametry limitów — wszystko pochodzi z kodu platformy i ma podane źródła.
3. **Rozwiązywanie błędów**: brak kodu weryfikacyjnego, zajęta nazwa użytkownika / e-mail, 403 nieaktywowane konto, zablokowane konto itd. — 13 typowych problemów.
4. **Aktywacja subskrypcji**: opis i rozwiązywanie problemów trzech kanałów — PayPal (web) / WeChat skan (ręczne potwierdzenie) / Huawei IAP (HarmonyOS); istniejące kanały płatności można bezpośrednio wykorzystać, skill tylko wskazuje drogę.

## Struktura plików

```
powpow-register/
├── SKILL.md                            # Główny przewodnik (warunki wyzwolenia, proces, zasady tonu)
├── README.md
├── .clawhubignore
└── references/
    ├── registration-flow.md            # Zasady pól, limity, tabela błędów (ze źródłami)
    ├── payment-and-activation.md       # Aktywacja subskrypcji, kanały płatności, wniosek o ponownym użyciu
    └── screenshots.md                  # Lista hostowanych zrzutów + szybki przegląd scen
```

## Bezpieczeństwo

- Nie zawiera żadnych kluczy; brak skryptów, nie dotyka poświadczeń użytkownika.
- **Nigdy nie proś** użytkownika o hasło, kod weryfikacyjny ani dane płatności; rejestracja i płatności odbywają się w całości na stronach platformy.

## Licencja

MIT-0 (jednolita licencja ClawHub).

## Linki

- Strona główna: https://global.powpow.online
- Rejestracja: https://global.powpow.online/register
- Poznaj PowPow (wideo): https://www.bilibili.com/video/BV1Wu826UEVz/