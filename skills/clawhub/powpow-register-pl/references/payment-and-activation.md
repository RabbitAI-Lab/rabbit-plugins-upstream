# Aktywacja subskrypcji i płatność — powpow-register

## Konkluzja (najpierw odpowiedź)

**Kanał Alipay jest uruchomiony (od 2026-10-07) i jest główną polecaną metodą płatności tego skilla; agent
może załatwiać składanie zamówienia i śledzenie księgowania.**
Użytkownicy spoza Chin / bez Alipay cofają się do PayPal; WeChat QR (potwierdzenie ręczne) i Huawei IAP
wciąż istnieją, ale skill ich nie załatwia.

Granice odpowiedzialności na etapie płatności: agent może **tworzyć zamówienie, otwierać kasę, sprawdzać
księgowanie**; **nigdy** nie dotyka konta Alipay/dowodów płatności użytkownika i nigdy nie obiecuje
„zapłacenia za niego". Akt płatności zawsze wykonuje sam użytkownik w oficjalnej kasie Alipay.

## Kanał Alipay (vibepay, główny)

Model zakupu jednorazowego: płacisz raz, dostajesz dany okres, **bez automatycznego odnawiania**. Pakiety są
zaszyte w `src/lib/alipay-vibepay.ts` (`ALIPAY_PACKAGES`):

| key | planId | Nazwa | Cena | Okres |
|---|---|---|---|---|
| `monthly` | alipay-monthly | Członkostwo miesięczne | ¥6.99 | 30 dni |
| `quarterly` | alipay-quarterly | Członkostwo kwartalne | ¥19.99 | 90 dni |
| `yearly` | alipay-yearly | Członkostwo roczne | ¥69.99 | 365 dni |

### Kontrakt interfejsów (skrypt skilla już je opakował, agent nie skleja requestów ręcznie)

| Interfejs | Metoda | Opis |
|---|---|---|
| `/api/payment/alipay/create-order` | POST | Wymaga `Authorization: Bearer <JWT>` (wystarczy użytkownik pending). body `{package}` → zwraca `{paymentHtml, outTradeNo, amount, planName}`; `paymentHtml` to strona z formularzem auto-submitującym do bramki Alipay |
| `/api/payment/alipay/query` | GET `?outTradeNo=` | Też autoryzacja Bearer. Zwraca `paid` / `pending` / `closed` / `unknown` |
| `/api/payment/alipay/notify` | POST (callback serwera Alipay) | Weryfikacja pięciu elementów (podpis, app_id, zgodność kwoty, TRADE_SUCCESS/TRADE_FINISHED, unikalność merchanta) → **idempotentna** aktualizacja zamówienia + utworzenie subskrypcji + aktywacja konta. Skill nigdy tego interfejsu nie dotyka |
| `/payment/alipay/return` | Strona powrotu w przeglądarce | Ścieżka publiczna; po płatności pokazuje potwierdzenie „płatność zakończona", odpytując w pętli o prawdziwy stan z backendu |

- Nieopłacone zamówienie **zamyka się automatycznie po 2 godzinach**; użytkownik odpadnie w trakcie → po
  prostu `create-order` ponownie, starym się nie przejmuj.
- Skrypt zapisuje `paymentHtml` do tymczasowego pliku HTML; agent otwiera go poleceniem systemowym i wchodzi
  do kasy Alipay (skan QR albo logowanie i płatność w Alipay).

### Łańcuch aktywacji (automatyczny, bez udziału człowieka)

Weryfikacja notify przechodzi → `paymentOrders` oznaczone opłacone → `user_subscriptions` utworzone/
przedłużone (`planId` i `currentPeriodEnd` liczone z durationDays; odnowienie dokłada się na pierwotną datę
wygaśnięcia) → `users.accountStatus: active` + `subscriptionStatus: ACTIVE` → strona powrotu odpytuje do
paid i pokazuje sukces.

### Po zapłacie trzeba wymienić stan logowania (ważne)

JWT niesie claim subskrypcji (konto pending ma `NONE`). **Księgowanie płatności aktualizuje tylko bazę —
nie zmienia już wydanego JWT**; claim starego tokena to nadal NONE i link logowania zrobiony z niego będzie
wyglądał jak „brak członkostwa". Dlatego po potwierdzeniu `paid` skill najpierw odpala `refresh-login`
(ponowne logowanie na nowy JWT z claimem ACTIVE), a dopiero potem generuje link 2. To zamierzony projekt, nie
łatka na lukę.

## Cztery kanały na stronie subskrypcji

Strona subskrypcji `src/app/(public)/subscription/page.tsx` pokazuje je zależnie od środowiska:

| Kanał | Środowisko | Mechanizm | Sposób aktywacji |
|---|---|---|---|
| **Alipay (główny)** | WWW | `AlipayPaymentSection` przez interfejsy vibepay (tabela wyżej) | notify: automatyczna aktywacja po stronie serwera, w sekundę |
| Subskrypcja PayPal | WWW (poza HarmonyOS) | `/api/subscription/create` → przekierowanie na autoryzację PayPal; odnawianie co miesiąc, do wypowiedzenia w każdej chwili (`/api/subscription/manage`) | PayPal Webhook (`BILLING.SUBSCRIPTION.*`) automatycznie ustawia active |
| Subskrypcja WeChat QR | WWW (poza HarmonyOS) | Na dole strony „Subskrypcja przez QR WeChat": skan i przelew | **Potwierdzenie ręczne**, księgowanie może się opóźniać; po zapłacie nie spiesz się z werdyktem porażki |
| Zakup w aplikacji Huawei | W aplikacji HarmonyOS | Natywne `NativeBridge.purchaseSubscription()` | `/api/subscription/activate-huawei` weryfikuje zamówienie Huawei i aktywuje |

Plan i ceny PayPal czytane dynamicznie z `/api/subscription/plans`; stały tekst na stronie: Auto-renews.
Cancel anytime.

## Stany i przekierowania

- Alipay opłacone → strona powrotu pokazuje sukces; PayPal sukces → `/subscription/success` → konto active →
  automatyczny powrót na stronę pierwotną z parametru `next` (bez niego — strona główna).
- Użytkownik z aktywną subskrypcją wejdzie na stronę subskrypcji → „You're All Set!", po 3 sekundach
  automatyczny powrót na stronę główną.
- Płatność nieudzona/anulowana (PayPal) → `/subscription/cancel`, można rozpocząć od nowa.

## Rozwiązywanie problemów

| Objaw | Postępowanie |
|---|---|
| Alipay opłacone, `query` wciąż pending | Notify sporadycznie się opóźnia; odczekaj 30 sekund i sprawdź ponownie. Jeśli dalej nic — niech użytkownik zajrzy w przeglądarce na stan strony powrotu; jeśli i to nie pomoże, kontakt z pomocą platformy (dongtao@outlook.com) z numerem `outTradeNo` |
| Alipay opłacone, a link 2 i tak wpada na blokadę | Pominięto `refresh-login` (claim starego JWT niezaktualizowany) — najpierw `refresh-login`, potem `login-link` |
| Po zapłacie nadal 403 (PayPal) | Webhook bywa opóźniony; zaloguj się ponownie, żeby odświeżyć stan |
| WeChat opłacone, a subskrypcji brak | Potwierdzenie ręczne jest asynchroniczne; jeśli w ciągu kilku godzin nie aktywuje się, wtedy kontakt z pomocą platformy |
| Strona subskrypcji pokazuje "No subscription plans available" | `/api/subscription/plans` nie ma dostępnych planów PayPal — problem konfiguracji po stronie platformy; użytkownicy z Chin mogą po prostu użyć Alipay |

## Uwaga historyczna

W kodzie jest jeszcze jeden, **stary** zestaw płatności webowych Alipay (`src/lib/alipay.ts`,
`/api/payment/create-order`, ¥9.90/¥99 zakup jednorazowy; w sandboxie bez kluczy degraduje się do płatności
symulowanej), nigdy niepodpięty do UI strony subskrypcji, niezwiązany z vibepay. Skill go nie dotyka;
`alipay-vibepay.ts` to obecnie obowiązujący kanał.
