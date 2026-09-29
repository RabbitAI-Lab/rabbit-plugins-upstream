# Aktywacja subskrypcji i płatności — powpow-register

## Wniosek (najpierw odpowiedź)

**Istniejące metody płatności można bezpośrednio wykorzystać — skill rejestracji wymaga zerowego nakładu na rozwój płatności.**

Powody:

1. Interfejs rejestracji (`src/app/api/auth/register/route.ts`) przy tworzeniu konta pending wystawia już cookie JWT + HttpOnly cookie pendingUserToken — użytkownik ląduje na `/subscription` w stanie zalogowanym; wszystkie trzy kanały płatności wiszą na tej stronie subskrypcji i aktywują to samo konto pending.
2. Interfejs logowania dla konta pending zwraca 403 + `redirectTo: '/subscription'` (cookie również ustawiane) — użytkownik w każdej chwili zostanie zaprowadzony z powrotem na tę samą stronę.
3. Zatem granica odpowiedzialności skillu rejestracji to po prostu „zaprowadzić użytkownika na /subscription"; nie potrzeba nowego interfejsu płatności, nowego modelu zamówienia ani żadnych zmian backendu.

Trzeba też pamiętać: płatności (przyciski SDK PayPal JS, ręczne potwierdzenie skanu WeChat, natywny IAP Huawei) **z natury nie mogą i nie powinny być dokonywane za użytkownika przez skill wiersza poleceń / czatu**. Nie próbuj wywoływać interfejsu płatności skryptem w imieniu użytkownika ani prosić o dane płatnicze.

## Trzy kanały na stronie subskrypcji

Strona subskrypcji `src/app/(public)/subscription/page.tsx` automatycznie pokazuje właściwy kanał w zależności od środowiska:

| Kanał | Środowisko | Mechanizm | Sposób aktywacji |
|---|---|---|---|
| Subskrypcja PayPal | Web (nie HarmonyOS) | `/api/subscription/create` tworzy subskrypcję PayPal → przekierowanie na autoryzację PayPal; automatyczne odnawianie co miesiąc, anulowanie w dowolnym momencie (`/api/subscription/manage`) | Webhook PayPal (`BILLING.SUBSCRIPTION.*`) automatycznie ustawia `accountStatus` na active |
| Subskrypcja skanem WeChat | Web (nie HarmonyOS) | Blok „Subskrypcja skanem WeChat" na dole strony: przelew przez skan kodu QR, **otwarcie po ręcznym potwierdzeniu** (`WechatQrPaymentSection`) | Ręczne potwierdzenie; zaksięgowanie może być opóźnione; po dokonaniu płatności nie zakładaj od razu porażki |
| Zakupy w aplikacji Huawei (IAP) | Aplikacja HarmonyOS | W WebView HarmonyOS PayPal / WeChat Pay są niedostępne, strona używa natywnego `NativeBridge.purchaseSubscription()` | `/api/subscription/activate-huawei` weryfikuje zamówienie Huawei i aktywuje |

Plany i ceny są odczytywane dynamicznie z `/api/subscription/plans` (plany PayPal); stały tekst strony: Auto-renews. Cancel anytime.

## Statusy i przekierowania

- Płatność udana → `/subscription/success` (callback PayPal z `subscriptionId`) → konto active → automatyczny powrót na stronę z parametru `next` (inaczej strona główna).
- Zasubskrybowany użytkownik ponownie wchodzący na stronę subskrypcji → widzi "You're All Set!", po 3 sekundach powrót na stronę główną.
- Płatność nieudana / anulowana → `/subscription/cancel`, można wznowić.

## Rozwiązywanie problemów

| Komunikat / sytuacja | Postępowanie |
|---|---|
| Po opłaceniu wciąż 403 | PayPal: Webhook czasem się opóźnia; zaloguj się ponownie, aby odświeżyć status (logowanie sprawdza najnowszy stan w DB); WeChat: ręczne potwierdzenie jeszcze nie nastąpiło, poczekaj; Huawei: sprawdź, czy w aplikacji pojawiła się strona sukcesu płatności |
| Strona subskrypcji pokazuje "No subscription plans available" | `/api/subscription/plans` nie ma dostępnego planu PayPal — problem konfiguracji po stronie platformy; poproś użytkownika, by spróbował później |
| Zapłacono WeChat, ale nie otwarto | Ręczne potwierdzenie jest asynchroniczne; jeśli w ciągu kilku godzin nie zostanie otwarte, skontaktuj się ze wsparciem platformy (dongtao@outlook.com) |

## Notatka: Alipay

W kodzie istnieje zestaw płatności webowych Alipay (`src/lib/alipay.ts`, `/api/payment/create-order`, model jednorazowej opłaty zwykłe członkostwo ¥9.90 / członkostwo premium ¥99; bez klucza piaskownicy automatycznie degraduje do płatności symulowanej), **ale nie jest podłączony do UI strony subskrypcji** — to kod nieużywany / zarezerwowany. Jeśli w przyszłości mielibyście włączyć Alipay na stronie subskrypcji, wystarczy podpiąć ten gotowy kod — to nie dotyczy tego skillu, stanowi tylko informację pomocniczą dla decyzji po stronie platformy.