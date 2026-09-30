# Kayıt süreci detayları — powpow-register

Sorun giderirken başvurulacak belge. Tüm kurallar platform kaynak kodundan gelir (Next.js ön yüz ve arka yüz tutarlılık doğrulaması), kaynakları belirtilmiştir. Platform güncellendikçe çevrimiçi gerçek davranış esas alınır.

## Giriş

- Kayıt sayfası: https://global.powpow.online/register
- Giriş sayfası: https://global.powpow.online/login
- Abonelik sayfası: https://global.powpow.online/subscription
- Paylaşım bağlantısı gibi `?next=...` ile girilirse, kayıt ve ödeme tamamlandıktan sonra otomatik olarak orijinal sayfaya dönülür.

## Form alanları ve kurallar

| Alan | Zorunlu | Kural | Kaynak kod |
|---|---|---|---|
| Avatar | İsteğe bağlı | Görsel ≤5 MB, SVG desteklenmez; sunucu otomatik sıkıştırır (>100 KB → 400×400 / kalite 90) | `src/app/api/auth/register/route.ts` |
| Kullanıcı adı | Zorunlu | 2–50 karakter, trim sonrası **küçük harfle** saklanır (Tom ile tom aynı ad; hem kayıt hem giriş büyük/küçük harfe duyarsız) | aynı yer (zod schema) |
| Şifre | Zorunlu | 8–100 karakter, büyük harf, küçük harf ve rakam içermelidir | aynı yer |
| Şifre onayı | Zorunlu | Şifreyle aynı (yalnızca ön yüzde doğrulanır) | `src/app/(public)/register/page.tsx` |
| Takma ad | İsteğe bağlı | ≤100 karakter; boş bırakılırsa kullanıcı adı alınır | register route |
| E-posta | **Zorunlu** | Geçerli e-posta formatı, ≤255 karakter; bir e-posta yalnızca bir hesap açabilir | register route |
| E-posta doğrulama kodu | **Zorunlu** | 6 haneli; **10 dakika geçerli**; başarılı doğrulamada geçersiz olur; yeniden gönderim eski kodu kullanılmış olarak işaretler | `src/lib/email-verification.ts` |
| Telefon numarası | İsteğe bağlı | Anakara Çin numarası `1[3-9]` ile başlar, toplam 11 hane; bir numara yalnızca bir hesaba bağlanabilir | register route |

Sayfada ayrıca üç üçüncü taraf giriş butonu bulunur: **Google, Watcha, Huawei hesabı** (`GoogleSignInButton` / `WatchaLoginButton` / `HuaweiLoginButton`). Üçüncü taraf hesabının yerel şifresi yoktur; sonradan şifreyle giriş denenirse «该账号未设置密码，请使用其他方式登录»（bu hesabın şifresi ayarlanmamış — lütfen başka bir yöntemle giriş yapın）mesajı alınır.

## Hız sınırı ve kaba kuvvet koruma parametreleri

| Davranış | Sınır | Kaynak |
|---|---|---|
| Kayıt gönderimi | **3 kez/dakika/IP**, aşımda 429 | `src/lib/rate-limit.ts` `REGISTER_RATE_LIMIT` |
| Doğrulama kodu gönderme | Aynı IP 1 kez/dakika **ve** aynı e-posta 1 kez/dakika, aşımda 429; ön yüz butonu 60 saniye geri sayar | `src/app/api/auth/register/send-code/route.ts` |
| Kod doğrulama | Her e-posta için 10 dakikada en fazla **5 deneme**; sınıra ulaşılınca kod doğru olsa bile reddedilir, yeni kod istenmelidir | `src/lib/email-verification.ts` |
| Şifremi unuttum kodu gönderme | 1 kez/dakika/IP | `src/app/api/auth/forgot-password/route.ts` |
| Giriş | 5 kez/dakika/IP; aynı hesapta **5 kez üst üste hatalı giriş 30 dakika kilitler** (423), bu sürede kalan deneme sayısı azalarak gösterilir | `src/app/api/auth/login/route.ts`, `rate-limit.ts` |

**Gizlilik koruması davranışı**: kod gönderme / şifremi unuttumda, e-posta kayıtlı olsun ya da olmasın, arayüz aynı başarı metnini döndürür; e-postanın kayıtlı olup olmadığı sızdırılmaz.

## Başarılı kayıt sonrası durum geçişleri

1. Kullanıcı `accountStatus: 'pending'` ile kaydedilir, başlangıçta **3 rozet** (register route).
2. Sunucu aynı anda iki HttpOnly cookie koyar: JWT (`/subscription`'a doğrudan erişim) ile pendingUserToken (abonelik süreci kimlik kanıtı).
3. Kayıt sayfası `pending_payment` algılar → `/subscription`'a geçer (`next` geri dönüş parametresi korunur).
4. Ödeme tamamlanınca → `accountStatus` `active` olur (PayPal Webhook ile otomatik aktifleşir; WeChat QR manuel onaylanır; Huawei IAP `activate-huawei` üzerinden ilerler). Detay: `payment-and-activation.md`.

Aktif olmayan (pending) kullanıcıların çekirdek API çağrıları (akış, harita, dijital insan sohbeti, yoklama vb.) her zaman 403 döndürür; buna gönderi paylaşım bağlantıları dahil değildir (herkese açık kalır).

## Yaygın hata giderme tablosu

| Belirti | Neden | Ne yapılmalı |
|---|---|---|
| 「用户名已存在」 | Kullanıcı adı dolu (büyük/küçük harf fark etmez) | Farklı bir kullanıcı adı seçin |
| 「邮箱已被使用」 | E-posta daha önce kayıt edilmiş | E-postayı değiştirin; ya da giriş yapıp + «şifremi unuttum» ile eski hesabı geri alın |
| 「邮箱验证码错误或已过期」 | Kod hatalı / 10 dakikayı aştı / 5 hatalı denemede reddedildi | «Yeniden gönder»e tıklayın, **en son** e-postadaki kodu kullanın |
| Doğrulama kodu gelmiyor | 60 saniye hız sınırı; ya da spam / promosyon klasörüne düştü | Geri sayım bitince tekrar gönderin; spam klasörünü kontrol edin |
| 「手机号已被使用」 | Telefon başka bir hesaba bağlı | Telefonu silin (isteğe bağlı alan) veya numarayı değiştirin |
| 「注册请求过于频繁」/ 429 | Kayıt 3 kez/dakika/IP sınırına ulaşıldı | Birkaç dakika bekleyip tekrar deneyin |
| 409「用户名或邮箱已被注册」 | Gönderim anında başkasıyla isim çakışması (eş zamanlı kayıt koruması) | Kullanıcı adını veya e-postayı değiştirip yeniden deneyin |
| 「图片大小不能超过5MB」/「不支持 SVG」 | Avatar kurallara uygun değil | Görseli değiştirin veya avatarı atlayın |
| Kayıt başarılı ama girişte 403「请完成订阅以激活账户」 | Hesap hâlâ pending | Giriş yapıp sayfadaki yönlendirmeyle `/subscription`'a gidip aboneliği tamamlayın |
| Giriş 423「账户已锁定」 | Şifre 5 kez yanlış girildi | 30 dakika bekleyin |
| Giriş 401「还剩 N 次尝试机会」 | Şifre hatalı, kilide yaklaşılıyor | İyice düşünüp deneyin veya doğrudan «şifremi unuttum» yolunu kullanın |
| 「该账号未设置密码，请使用其他方式登录」 | Üçüncü taraf (Google/Watcha/Huawei) hesabı | Orijinal üçüncü taraf butonuyla giriş yapın |
| 「该账号已注销」 | Hesap devre dışı bırakılmış (deactivate) | Yeniden kayıt olmanız gerekir |

## Girişle ilgili küçük notlar (giderme için de geçerli)

Girişte **kullanıcı adı / e-posta / telefon** üçlü giriş desteklenir (üçünden herhangi biri hesap adı olarak geçerlidir). Şifremi unuttum: giriş sayfası → «şifremi unuttum» → kayıtlı e-postanızı girin, 6 haneli kod alın → sıfırlayın.