# Àwọn Àlàyé Ìlànà Ìforúkọsílẹ̀ — powpow-register

Wo ó nígbà ìṣàwárí ìṣòro. Gbogbo àwọn ìlànà wá láti inú kóòdù ìpìlẹ̀ pẹ̀pẹ̀ (ìfọwọ́sí ìbáṣepọ̀ Next.js iwájú/ẹ̀yìn), a sì tọ́ka orísun. Nígbà tí pẹ̀pẹ̀ bá ṣe àtúnyẹ̀wò, tẹ̀lé ìwà gidi tó wà lórí ayélujára.

## Àwọn Ojú-Ìwé

- Ojú-ìwé ìforúkọsílẹ̀: https://global.powpow.online/register
- Ojú-ìwé ìwọlé: https://global.powpow.online/login
- Ojú-ìwé ìforúkọsílẹ̀: https://global.powpow.online/subscription
- Tí wọ́n bá wọlé nípasẹ̀ ọ̀rọ̀ asopọ̀ ìpínpín mìíràn pẹ̀lú `?next=...`, lẹ́yìn tí ìforúkọsílẹ̀ + ìsanwó bá parí, yóò padà sí ojú-ìwé àkọ́kọ́ fúnrarẹ̀.

## Àwọn Pápá Fọ́ọ̀mù àti Àwọn Ìlànà

| Pápá | Dánilójú | Ìlànà | Orísun Kóòdù |
|---|---|---|---|
| Àwòrán ìdánimọ̀ | Ìyàn | Àwòrán ≤5MB, SVG kò ṣiṣẹ́; sẹ́fà á gbé e sílẹ̀ fúnrarẹ̀ (>100KB ni a máa ń fúyẹ́ sí 400×400 / didára 90) | `src/app/api/auth/register/route.ts` |
| Orúkọ olùmúlò | Dánilójú | 2~50 lẹ́tà, lẹ́yìn trim a máa ń fi sí **lẹ́tà kékeré** (Tom àti tom jẹ́ orúkọ olùmúlò kan; ìforúkọsílẹ̀ àti ìwọlé kì í ya lẹ́tà ńlá/kékeré) | Lókè (zod schema) |
| Ọ̀rọ̀ àsìrí | Dánilójú | 8~100 lẹ́tà, ó gbọ́dọ̀ ní lẹ́tà ńlá, lẹ́tà kékeré àti nọ́ḿbà nínú | Lókè |
| Ìmúdarí ọ̀rọ̀ àsìrí | Dánilójú | Ó gbọ́dọ̀ bá ọ̀rọ̀ àsìrí mu (ìfọwọ́sí iwájú nìkan) | `src/app/(public)/register/page.tsx` |
| Orúkọ ìpè | Ìyàn | ≤100 lẹ́tà; tí kò bá kún, orúkọ olùmúlò náà ni a ó lò | register route |
| Ìmélì | **Dánilójú** | Ìrísí ìmélì tó pé, ≤255 lẹ́tà; ìmélì kan ṣoṣo ni ó lè forúkọ àkọọlẹ̀ kan sílẹ̀ | register route |
| Kódì ìmúdarí ìmélì | **Dánilójú** | Nọ́ḿbà mẹ́fà; **ó ṣiṣẹ́ fún ìṣẹ́jú mẹ́wàá**; a máa ń pa á run lẹ́yìn ìmúdarí tó yọrí sí rere; tí a bá tún rán, kódì àtijọ́ di àìṣiṣẹ́ | `src/lib/email-verification.ts` |
| Nọ́ḿbà fóónù | Ìyàn | Nọ́ḿbà fóónù orílẹ̀-èdè Ṣáínà tó bẹ̀rẹ̀ pẹ̀lú `1[3-9]`, lápapọ̀ 11 nọ́ḿbà; nọ́ḿbà fóónù kan ṣoṣo ni ó lè so mọ́ àkọọlẹ̀ kan | register route |

Ní àfikún, ojú-ìwé náà ní àwọn bọ̀tìnì ìwọlé onígbà-mẹ́ta: **Google, Watcha, Àkọọlẹ̀ Huawei** (`GoogleSignInButton` / `WatchaLoginButton` / `HuaweiLoginButton`). Àwọn àkọọlẹ̀ onígbà-mẹ́ta kò ní ọ̀rọ̀ àsìrí inú; tí o bá gbìyànjú láti wọlé pẹ̀lú ọ̀rọ̀ àsìrí lẹ́yìn náà, o ó rí àṣìṣe «该账号未设置密码，请使用其他方式登录» (àkọọlẹ̀ yìí kò ní ọ̀rọ̀ àsìrí tí a ṣètò, jọ̀wọ́ fi ọ̀nà mìíràn wọlé).

## Àwọn Ìdíwọ̀n Àkópọ̀ àti Ààbò Ìkúnlẹ̀

| Ìgbésẹ̀ | Ìdíwọ̀n | Orísun |
|---|---|---|
| Fífi ìforúkọsílẹ̀ sílẹ̀ | **Ìgbà mẹ́ta / ìṣẹ́jú / IP**; 429 nígbà tí ó bá rékọjá | `src/lib/rate-limit.ts` `REGISTER_RATE_LIMIT` |
| Ríran kódì ìmúdarí | Ìgbà kan / ìṣẹ́jú tí IP kanna àti ìgbà kan / ìṣẹ́jú tí ìmélì kanna; 429 nígbà tí ó bá rékọjá; bọ̀tìnì iwájú ní kààntì ọgọ́ta ìṣẹ́jú-àáyá | `src/app/api/auth/register/send-code/route.ts` |
| Ìmúdarí kódì | Ó pọ̀jù **ìgbìyànjú 5** nínú ìṣẹ́jú mẹ́wàá fún ìmélì kọ̀ọ̀kan; nígbà tí ààlà bá dé, kódì náà yóò di àìṣiṣẹ́ bí ó tilẹ̀ jẹ́ pé ó tọ̀nà, a ó ní láti rán tuntun | `src/lib/email-verification.ts` |
| Ríran kódì ìgbàgbé ọ̀rọ̀ àsìrí | Ìgbà kan / ìṣẹ́jú / IP | `src/app/api/auth/forgot-password/route.ts` |
| Ìwọlé | Ìgbà márùn-ún / ìṣẹ́jú / IP; àkọọlẹ̀ kanna tí ó bá ṣìnà **ìgbà márùn-ún léraléra á di tíípá fún ìṣẹ́jú ọgbọ̀n** (423), nígbà náà a máa ń fi iye ìgbìyànjú tó kù hàn títí ré | `src/app/api/auth/login/route.ts`, `rate-limit.ts` |

**Ìwà ààbò ìkọ̀kọ̀**: nígbà ríran kódì ìmúdarí / ìgbàgbé ọ̀rọ̀ àsìrí, bí ìmélì náà ti forúkọ sílẹ̀ tàbí kò sí, interface máa ń dá ìránṣẹ́ àṣeyọrí kanna padà, kò fi ìmélì tó forúkọ sílẹ̀ hàn.

## Ìyípadà Ipò Lẹ́yìn Ìforúkọsílẹ̀ Àṣeyọrí

1. A máa ń fi olùmúlò pamọ́ pẹ̀lú `accountStatus: 'pending'` nínú ibùdó ìsọfúnni, pẹ̀lú **àmì-ẹ̀yẹ mẹ́ta àkọ́kọ́** (register route).
2. Sẹ́fà máa ń fi cookies HttpOnly méjì sílẹ̀ nígbàkanna: JWT (láti lè dé `/subscription` taara) àti pendingUserToken (ìdánilójú ìlànà ìforúkọsílẹ̀).
3. Ojú-ìwé ìforúkọsílẹ̀ bá rí `pending_payment` → ó lọ sí `/subscription` (ó pa ìpín ìpadà `next` mọ́).
4. Ìsanwó parí → `accountStatus` di `active` (PayPal máa ń ṣiṣẹ́ fúnrarẹ̀ nípasẹ̀ Webhook; QR WeChat ń gba ìfọwọ́sowọ́pọ̀ ènìyàn; Huawei IAP ń lọ nípasẹ̀ `activate-huawei`). Wo `payment-and-activation.md` fún àwọn àlàyé.

Olùmúlò tí kò tíì ṣiṣẹ́ (pending) tí ó bá lo àwọn API pàtàkì (ìtàn ìkọ̀wé, máàpù, sísọ̀rọ̀ pẹ̀lú àwọn ènìyàn dídijitá, ṣíṣàmìsí àbẹ̀wò, àti bẹ́ẹ̀ lọ) yóò rí 403 nígbà gbogbo; àwọn ọ̀rọ̀ asopọ̀ ìkọ̀wé tí a pín ṣoṣo ni yóò ṣiṣẹ́ (a fi wọ́n sílẹ̀ ní ìmọ́ fún gbogbo ènìyàn).

## Tábìlì Ìṣàwárí Àwọn Àṣìṣe Tó Wọ́pọ̀

| Ìṣẹ̀lẹ̀ (Ìránṣẹ́ ẹ̀rọ) | Ìdí | Ohun tí ó ṣe |
|---|---|---|
| 「用户名已存在」 (Orúkọ olùmúlò ti wà tẹ́lẹ̀) | Orúkọ olùmúlò náà ti ní ẹni tó ń lò ó (kò ya lẹ́tà ńlá/kékeré) | Yí orúkọ olùmúlò padà |
| 「邮箱已被使用」 (Ìmélì ti lò) | Ìmélì náà ti forúkọ sílẹ̀ tẹ́lẹ̀ | Yí ìmélì padà; tàbí wọlé + «Mo gbàgbé ọ̀rọ̀ àsìrí» láti gba àkọọlẹ̀ àtijọ́ padà |
| 「邮箱验证码错误或已过期」 (Kódì ìmúdarí ìmélì ṣìnà tàbí ti pé) | Kódì tí a kọ jẹ̀ àṣìṣe / ó ti pé ju ìṣẹ́jú mẹ́wàá / ó ti ju ìgbìyànjú àṣìṣe 5 lọ | Tẹ «Rán lẹ́ẹ̀kan sí i», lo kódì ìmúdarí **tuntun** |
| Kò rí kódì ìmúdarí | Ààlà ọgọ́ta ìṣẹ́jú-àáyá; tàbí ó wọ inú spam/ìpolówó | Dúró tí kààntì bá parí kí o tó tún rán; wo àpótí spam |
| 「手机号已被使用」 (Nọ́ḿbà fóónù ti lò) | Nọ́ḿbà fóónù náà ti so mọ́ àkọọlẹ̀ mìíràn | Yọ nọ́ḿbà fóónù kúrò (ìyàn) tàbí yí nọ́ḿbà padà |
| 「注册请求过于频繁」 / 429 (Ìbéèrè ìforúkọsílẹ̀ ti pọ̀ jù) | Ó tí rékọjá ààlà ìgbà mẹ́ta / ìṣẹ́jú / IP | Dúró fún ìṣẹ́jú díẹ̀ kí o tó gbìyànjú lẹ́ẹ̀kan sí i |
| 409「用户名或邮箱已被注册」 (Orúkọ olùmúlò tàbí ìmélì ti forúkọ sílẹ̀) | Àkóba pẹ̀lú orúkọ ẹlòmíì ní àkókò fífilẹ̀ (ààbò ìjàkadì) | Yí orúkọ olùmúlò tàbí ìmélì padà kí o sì gbìyànjú lẹ́ẹ̀kan sí i |
| 「图片大小不能超过5MB」 / 「不支持 SVG」 (Àwòrán kò gbọ́dọ̀ ju 5MB lọ / SVG kò ṣiṣẹ́) | Àwòrán ìdánimọ̀ kò bá ìlànà mu | Yí àwòrán padà tàbí fo àwòrán ìdánimọ̀ |
| Ìforúkọsílẹ̀ ṣe ṣùgbọ́n ìwọlé ń sọ 403「请完成订阅以激活账户」 (Jọ̀wọ́ parí ìforúkọsílẹ̀ láti mú àkọọlẹ̀ rẹ ṣiṣẹ́) | Àkọọlẹ̀ náà ṣì pending | Lẹ́yìn ìwọlé, tẹ̀lé ìtọ́ka ojú-ìwé kí o lọ sí `/subscription` kí o parí ìforúkọsílẹ̀ |
| Ìwọlé 423「账户已锁定」 (Àkọọlẹ̀ ti tíipa) | Ọ̀rọ̀ àsìrí ṣìnà ìgbà márùn-ún léraléra | Dúró fún ìṣẹ́jú ọgbọ̀n |
| Ìwọlé 401「还剩 N 次尝试机会」 (Ìgbìyànjú N ṣì kù) | Ọ̀rọ̀ àsìrí ṣìnà, ó súnmọ́ ìtíípá | Rò ó dáradára kí o gbìyànjú, tàbí lọ sí «Mo gbàgbé ọ̀rọ̀ àsìrí» taara |
| 「该账号未设置密码，请使用其他方式登录」 (Àkọọlẹ̀ yìí kò ní ọ̀rọ̀ àsìrí tí a ṣètò, jọ̀wọ́ fi ọ̀nà mìíràn wọlé) | Àkọọlẹ̀ onígbà-mẹ́ta (Google/Watcha/Huawei) ni | Wọlé nípasẹ̀ bọ̀tìnì onígbà-mẹ́ta tí o lò ṣáájú |
| 「该账号已注销」 (Àkọọlẹ̀ ti fagilé) | A ti deactivate àkọọlẹ̀ náà | A ní láti forúkọ sílẹ̀ lẹ́ẹ̀kan sí i |

## Ìmọ̀ Kékèké Ìwọlé (Ó wúlò fún ìṣàwárí ìṣòro pẹ̀lú)

Ìwọlé **ṣe àtìlẹ́yìn orúkọ olùmúlò / ìmélì / nọ́ḿbà fóónù** lápapọ̀ (ẹ̀yìn kẹ̀ẹ̀kan lè jẹ́ ìdánimọ̀ àkọọlẹ̀). Ìgbàgbé ọ̀rọ̀ àsìrí: ojú-ìwé ìwọlé → «Mo gbàgbé ọ̀rọ̀ àsìrí» → fi ìmélì tí o forúkọ sílẹ̀ lẹ́yìn rẹ̀ láti gba kódì oní nọ́ḿbà mẹ́fà → ṣètò ọ̀rọ̀ àsìrí tuntun.