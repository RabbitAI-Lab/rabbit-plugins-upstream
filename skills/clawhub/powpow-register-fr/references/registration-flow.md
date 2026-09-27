# Parcours d'inscription en détail — powpow-register

À consulter pour le dépannage. Toutes les règles proviennent du code source de la plateforme (validation cohérente Next.js côté frontend et backend), avec sources citées.
En cas de mise à jour de la plateforme, le comportement réel en ligne fait foi.

## Entrées

- Page d'inscription : https://global.powpow.online/register
- Page de connexion : https://global.powpow.online/login
- Page d'abonnement : https://global.powpow.online/subscription
- Si l'utilisateur arrive via un lien partagé contenant `?next=...`, il sera automatiquement ramené à la page d'origine après l'inscription + le paiement.

## Champs du formulaire et règles

| Champ | Obligatoire | Règle | Source |
|---|---|---|---|
| Avatar | Facultatif | Image ≤5 Mo, SVG non pris en charge ; compression automatique côté serveur (>100 Ko compressé en 400×400 / qualité 90) | `src/app/api/auth/register/route.ts` |
| Nom d'utilisateur | Obligatoire | 2 à 50 caractères, stocké en **minuscules** après trim (Tom et tom sont considérés comme le même nom d'utilisateur ; inscription et connexion sont insensibles à la casse) | idem (schéma zod) |
| Mot de passe | Obligatoire | 8 à 100 caractères, doit contenir majuscules, minuscules et chiffres | idem |
| Confirmation du mot de passe | Obligatoire | Doit correspondre au mot de passe (validation frontend uniquement) | `src/app/(public)/register/page.tsx` |
| Surnom | Facultatif | ≤100 caractères ; par défaut, le nom d'utilisateur | register route |
| E-mail | **Obligatoire** | Format d'e-mail valide, ≤255 caractères ; un e-mail ne peut enregistrer qu'un seul compte | register route |
| Code de vérification e-mail | **Obligatoire** | 6 chiffres ; **valable 10 minutes** ; invalidé une fois vérifié ; un renvoi marque l'ancien code comme utilisé | `src/lib/email-verification.ts` |
| Téléphone | Facultatif | Numéro de Chine continentale commençant par `1[3-9]`, 11 chiffres au total ; un numéro ne peut être lié qu'à un seul compte | register route |

La page propose aussi trois boutons de connexion tiers : **Google, Watcha, compte Huawei** (`GoogleSignInButton` / `WatchaLoginButton` / `HuaweiLoginButton`). Les comptes tiers n'ont pas de mot de passe local ; tenter de se connecter ensuite avec un mot de passe renvoie « 该账号未设置密码，请使用其他方式登录 » (Ce compte n'a pas de mot de passe défini, veuillez utiliser une autre méthode de connexion).

## Limitation de débit et paramètres anti-force brute

| Comportement | Limite | Source |
|---|---|---|
| Envoi de l'inscription | **3 fois/minute/IP**, 429 au-delà | `src/lib/rate-limit.ts` `REGISTER_RATE_LIMIT` |
| Envoi du code de vérification | Même IP 1 fois/minute **et** même e-mail 1 fois/minute, 429 au-delà ; compte à rebours de 60 secondes sur le bouton frontend | `src/app/api/auth/register/send-code/route.ts` |
| Vérification du code | Maximum **5 tentatives** par e-mail en 10 minutes ; une fois le plafond atteint, refus même avec le bon code — un nouveau code est nécessaire | `src/lib/email-verification.ts` |
| Code mot de passe oublié | 1 fois/minute/IP | `src/app/api/auth/forgot-password/route.ts` |
| Connexion | 5 fois/minute/IP ; **5 échecs consécutifs verrouillent le compte 30 minutes** (423), avec un message d'essais restants décroissant pendant la période | `src/app/api/auth/login/route.ts`, `rate-limit.ts` |

**Comportement de protection de la vie privée** : lors de l'envoi du code de vérification / mot de passe oublié, l'interface renvoie le même message de succès que l'e-mail soit enregistré ou non, sans révéler si l'e-mail existe.

## Déroulement des statuts après une inscription réussie

1. L'utilisateur est enregistré avec `accountStatus: 'pending'` et **3 badges initiaux** (register route).
2. Le serveur pose en même temps deux cookies HttpOnly : JWT (permet l'accès direct à `/subscription`) et pendingUserToken (justificatif d'identité pour le parcours d'abonnement).
3. La page d'inscription détecte `pending_payment` → redirection vers `/subscription` (le paramètre de retour `next` est conservé).
4. Paiement terminé → `accountStatus` passe à `active` (PayPal active automatiquement via Webhook ; QR code WeChat par confirmation manuelle ; IAP Huawei via `activate-huawei`). Voir `payment-and-activation.md`.

Les appels aux API cœur (fil d'actualités, carte, dialogue avec les humains numériques, check-ins, etc.) par un utilisateur non activé (pending) renvoient tous 403 ; les liens de posts partagés sont l'exception (ils restent accessibles publiquement).

## Tableau des erreurs courantes

| Message | Cause | Que faire |
|---|---|---|
| 「用户名已存在」(Nom d'utilisateur déjà existant) | Nom d'utilisateur déjà pris (insensible à la casse) | Choisir un autre nom d'utilisateur |
| 「邮箱已被使用」(E-mail déjà utilisé) | E-mail déjà enregistré | Changer d'e-mail ; ou passer par la connexion + « Mot de passe oublié » pour récupérer l'ancien compte |
| 「邮箱验证码错误或已过期」(Code de vérification e-mail incorrect ou expiré) | Code mal saisi / plus de 10 minutes / rejeté après plus de 5 tentatives | Cliquer sur « Renvoyer » et utiliser le code du **dernier** e-mail reçu |
| Code de vérification non reçu | Limitation de 60 secondes ; ou arrivé dans les spams/promotions | Attendre la fin du compte à rebours avant de renvoyer ; vérifier le dossier des spams |
| 「手机号已被使用」(Numéro de téléphone déjà utilisé) | Numéro lié à un autre compte | Supprimer le numéro (champ facultatif) ou en utiliser un autre |
| 「注册请求过于频繁」/ 429 (Trop de demandes d'inscription) | Plafond de 3 inscriptions/minute/IP atteint | Attendre quelques minutes et réessayer |
| 409「用户名或邮箱已被注册」(Nom d'utilisateur ou e-mail déjà enregistré) | Collision avec un autre utilisateur au moment de l'envoi (repli de concurrence) | Changer le nom d'utilisateur ou l'e-mail puis réessayer |
| 「图片大小不能超过5MB」/「不支持 SVG」(La taille de l'image ne peut pas dépasser 5 Mo / SVG non pris en charge) | Avatar non conforme | Changer d'image ou sauter l'avatar |
| Inscription réussie mais connexion 403「请完成订阅以激活账户」(Veuillez finaliser votre abonnement pour activer votre compte) | Le compte est encore pending | Après connexion, suivre l'invite de la page et aller sur `/subscription` pour finaliser l'abonnement |
| Connexion 423「账户已锁定」(Compte verrouillé) | Mot de passe saisi 5 fois de travers | Attendre 30 minutes |
| Connexion 401「还剩 N 次尝试机会」(Il reste N tentatives) | Mot de passe incorrect, proche du verrouillage | Bien réfléchir avant de réessayer, ou passer directement par « Mot de passe oublié » |
| 「该账号未设置密码，请使用其他方式登录」(Ce compte n'a pas de mot de passe défini, veuillez utiliser une autre méthode de connexion) | Compte tiers (Google/Watcha/Huawei) | Se connecter avec le bouton tiers d'origine |
| 「该账号已注销」(Ce compte a été désactivé) | Compte désactivé | Une nouvelle inscription est nécessaire |

## Astuces de connexion (utiles aussi pour le dépannage)

La connexion accepte un champ combiné **nom d'utilisateur / e-mail / téléphone** (n'importe lequel des trois fonctionne comme identifiant).
Mot de passe oublié : page de connexion → « Mot de passe oublié » → saisir l'e-mail d'inscription, recevoir un code à 6 chiffres → réinitialiser.