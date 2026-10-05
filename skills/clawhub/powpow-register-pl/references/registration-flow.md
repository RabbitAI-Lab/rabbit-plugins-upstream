# Szczegółowy proces rejestracji — powpow-register

Dokument do konsultacji przy rozwiązywaniu problemów. Wszystkie zasady pochodzą z kodu źródłowego platformy (spójna walidacja frontendu i backendu Next.js), z podanym źródłem. Gdy platforma się aktualizuje, decydujące jest rzeczywiste zachowanie online.

## Wejście

- Strona rejestracji: https://global.powpow.online/register
- Strona logowania: https://global.powpow.online/login
- Strona subskrypcji: https://global.powpow.online/subscription
- Jeśli użytkownik wszedł przez link z `?next=...`, po rejestracji i płatności automatycznie wróci na pierwotną stronę.

## Pola formularza i zasady

| Pole | Wymagane | Zasada | Źródło w kodzie |
|---|---|---|---|
| Awatar | Opcjonalne | Obraz ≤5 MB, SVG nieobsługiwane; serwer automatycznie kompresuje (>100 KB → 400×400 / jakość 90) | `src/app/api/auth/register/route.ts` |
| Nazwa użytkownika | Wymagane | 2–50 znaków, po trim zapisywana **małymi literami** (Tom i tom to ta sama nazwa; zarówno rejestracja, jak i logowanie nie rozróżniają wielkości liter) | j.w. (schema zod) |
| Hasło | Wymagane | 8–100 znaków, musi zawierać wielką literę, małą literę i cyfrę | j.w. |
| Potwierdzenie hasła | Wymagane | Zgodne z hasłem (walidacja tylko po stronie frontendu) | `src/app/(public)/register/page.tsx` |
| Pseudonim | Opcjonalne | ≤100 znaków; jeśli puste, domyślnie nazwa użytkownika | rejestracja route |
| E-mail | **Wymagane** | Poprawny format e-mail, ≤255 znaków; jeden e-mail może zarejestrować tylko jedno konto | rejestracja route |
| Kod weryfikacyjny e-mail | **Wymagane** | 6 cyfr; **ważny 10 minut**; po udanej weryfikacji unieważniany; ponowne wysłanie oznacza stary kod jako użyty | `src/lib/email-verification.ts` |
| Numer telefonu | Opcjonalne | Chiński numer komórkowy zaczynający się od `1[3-9]`, łącznie 11 cyfr; jeden numer można przypisać tylko do jednego konta | rejestracja route |

Strona oferuje też trzy przyciski logowania przez podmioty trzecie: **Google, Watcha, konto Huawei** (`GoogleSignInButton` / `WatchaLoginButton` / `HuaweiLoginButton`). Konta zewnętrzne nie mają lokalnego hasła; późniejsza próba logowania hasłem da komunikat „该账号未设置密码，请使用其他方式登录"（to konto nie ma ustawionego hasła — zaloguj się w inny sposób）.

## Parametry limitów i ochrony przed atakami brute force

| Zachowanie | Limit | Źródło |
|---|---|---|
| Wysłanie rejestracji | **3 razy/minutę/IP**, powyżej 429 | `src/lib/rate-limit.ts` `REGISTER_RATE_LIMIT` |
| Wysłanie kodu weryfikacyjnego | 1 raz/minutę/IP **oraz** 1 raz/minutę/e-mail, powyżej 429; przycisk frontendu z 60-sekundowym odliczaniem | `src/app/api/auth/register/send-code/route.ts` |
| Weryfikacja kodu | Maks. **5 prób** na e-mail w ciągu 10 minut; po przekroczeniu odmowa nawet przy poprawnym kodzie — trzeba wysłać nowy | `src/lib/email-verification.ts` |
| Wysłanie kodu „nie pamiętam hasła" | 1 raz/minutę/IP | `src/app/api/auth/forgot-password/route.ts` |
| Logowanie | 5 razy/minutę/IP; **5 kolejnych nieudanych prób blokuje konto na 30 minut** (423), w trakcie pokazywana jest malejąca liczba pozostałych prób | `src/app/api/auth/login/route.ts`, `rate-limit.ts` |

**Zachowanie ochrony prywatności**: przy wysyłce kodu / „nie pamiętam hasła", niezależnie od tego, czy e-mail jest zarejestrowany, interfejs zwraca taki sam komunikat sukcesu, nie ujawniając, czy e-mail istnieje.

## Zmiany statusu po udanej rejestracji

1. Użytkownik zapisywany z `accountStatus: 'pending'`, początkowe **3 odznaki** (route rejestracji).
2. Serwer jednocześnie ustawia dwa ciasteczka HttpOnly: JWT (bezpośredni dostęp do `/subscription`) oraz pendingUserToken (poświadczenie tożsamości w procesie subskrypcji).
3. Strona rejestracji wykrywa `pending_payment` → przekierowanie na `/subscription` (z zachowaniem parametru powrotu `next`).
4. Po zakończeniu płatności → `accountStatus` zmienia się na `active` (PayPal przez automatyczną aktywację Webhook; WeChat przez ręczne potwierdzenie; Huawei IAP przez `activate-huawei`). Szczegóły: `payment-and-activation.md`.

Wywołania rdzennych API (kanał postów, mapa, rozmowy z cyfrowymi ludźmi, logowanie itp.) przez nieaktywowanych (pending) użytkowników zwracają 403; wyjątkiem są linki do postów (pozostają publicznie dostępne).

## Tabela typowych błędów

| Komunikat | Powód | Co zrobić |
|---|---|---|
| 「用户名已存在」 | Nazwa użytkownika zajęta (bez rozróżniania wielkości liter) | Zmień nazwę użytkownika |
| 「邮箱已被使用」 | E-mail już zarejestrowany | Zmień e-mail; albo zaloguj się + „nie pamiętam hasła", aby odzyskać stare konto |
| 「邮箱验证码错误或已过期」 | Zły kod / ponad 10 minut / odrzucony po 5 błędnych próbach | Kliknij „Wyślij ponownie", użyj kodu z **najnowszej** wiadomości |
| Nie przychodzi kod weryfikacyjny | Limit 60 s; albo kod trafił do spamu / wiadomości reklamowych | Poczekaj na koniec odliczania i wyślij ponownie; sprawdź folder spamu |
| 「手机号已被使用」 | Telefon przypięty do innego konta | Usuń numer (opcjonalny) lub zmień numer |
| 「注册请求过于频繁」/ 429 | Osiągnięto limit 3 rejestracji/minutę/IP | Odczekaj kilka minut i spróbuj ponownie |
| 409「用户名或邮箱已被注册」 | Kolizja nazwy z kimś innym w momencie wysyłki (zabezpieczenie na wypadek jednoczesnych zapisów) | Zmień nazwę lub e-mail i ponów próbę |
| 「图片大小不能超过5MB」/「不支持 SVG」 | Awatar niezgodny z zasadami | Zmień obraz lub pomiń awatar |
| Rejestracja OK, ale logowanie 403「请完成订阅以激活账户」 | Konto wciąż pending | Zaloguj się i zgodnie z podpowiedzią na stronie przejdź na `/subscription`, aby dokończyć subskrypcję |
| Logowanie 423「账户已锁定」 | Hasło błędne 5 razy z rzędu | Poczekaj 30 minut |
| Logowanie 401「还剩 N 次尝试机会」 | Błędne hasło, blisko zablokowania | Zastanów się, zanim spróbujesz, albo od razu użyj „nie pamiętam hasła" |
| 「该账号未设置密码，请使用其他方式登录」 | Konto przez podmiot trzeci (Google/Watcha/Huawei) | Zaloguj się pierwotnym przyciskiem podmiotu trzeciego |
| 「该账号已注销」 | Konto zdezaktywowane (deactivate) | Trzeba zarejestrować się ponownie |

## Ciekawostki o logowaniu (przydatne przy rozwiązywaniu problemów)

Logowanie wspiera wejście **nazwa użytkownika / e-mail / numer telefonu** (dowolna z trzech wartości jako identyfikator konta). Nie pamiętasz hasła: strona logowania → „nie pamiętam hasła" → podaj zarejestrowany e-mail, otrzymasz 6-cyfrowy kod → zresetuj.