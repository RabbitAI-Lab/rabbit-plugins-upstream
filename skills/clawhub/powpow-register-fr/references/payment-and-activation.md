# Activation de l'abonnement et paiement — powpow-register

## Conclusion (la réponse d'abord)

**Les moyens de paiement existants sont directement réutilisables — le skill d'assistance à l'inscription ne requiert aucun développement de paiement.**

Raisons :

1. L'interface d'inscription (`src/app/api/auth/register/route.ts`) délivre déjà un cookie JWT + un cookie HttpOnly pendingUserToken lors de la création du compte pending, de sorte que l'utilisateur arrive sur `/subscription` déjà connecté — les trois canaux de paiement dépendent de cette page d'abonnement et activent tous le même compte pending.
2. L'interface de connexion renvoie 403 + `redirectTo: '/subscription'` pour les comptes pending et pose les cookies de la même façon — un utilisateur qui paie plus tard sera toujours ramené vers la même page.
3. La frontière de responsabilité d'un skill d'assistance à l'inscription est donc simplement « amener l'utilisateur vers /subscription » ; aucune nouvelle interface de paiement, aucun nouveau modèle de commande, aucune modification backend.

À noter aussi : l'étape de paiement (bouton PayPal JS SDK, confirmation manuelle du QR code WeChat, IAP natif Huawei) **signifie qu'il est impossible et inapproprié qu'un skill en ligne de commande/chat paie à la place de l'utilisateur**. N'essayez pas d'appeler des interfaces de paiement depuis un script pour payer pour l'utilisateur, et ne demandez pas ses justificatifs de paiement.

## Les trois canaux de la page d'abonnement

La page d'abonnement `src/app/(public)/subscription/page.tsx` affiche automatiquement le canal adapté selon l'environnement d'exécution :

| Canal | Environnement | Mécanisme | Activation |
|---|---|---|---|
| Abonnement PayPal | Web (hors HarmonyOS) | `/api/subscription/create` crée un abonnement PayPal → redirection vers l'autorisation PayPal ; renouvellement automatique mensuel, annulable à tout moment (`/api/subscription/manage`) | Le Webhook PayPal (`BILLING.SUBSCRIPTION.*`) passe automatiquement `accountStatus` à active |
| Abonnement par QR code WeChat | Web (hors HarmonyOS) | Section « S'abonner par scan WeChat » en bas de page : virement par scan, **activé après confirmation manuelle** (`WechatQrPaymentSection`) | Confirmation manuelle ; le crédit peut prendre du temps — ne concluez pas prématurément à un échec juste après le paiement |
| Achat intégré Huawei (IAP) | Dans l'app HarmonyOS | PayPal / WeChat Pay indisponibles dans la WebView HarmonyOS, la page utilise le natif `NativeBridge.purchaseSubscription()` | `/api/subscription/activate-huawei` vérifie la commande Huawei puis active |

Les formules et les prix sont lus dynamiquement depuis `/api/subscription/plans` (formules PayPal) ; le texte fixe de la page : Auto-renews. Cancel anytime.

## Statuts et redirections

- Paiement réussi → `/subscription/success` (le callback PayPal porte `subscriptionId`) → compte active → retour automatique à la page d'origine spécifiée par le paramètre `next` (accueil sinon).
- Un utilisateur déjà abonné qui visite la page d'abonnement → affiche "You're All Set!", retour automatique à l'accueil après 3 secondes.
- Échec/annulation du paiement → `/subscription/cancel`, une nouvelle tentative est possible.

## Dépannage

| Message | Traitement |
|---|---|
| Toujours 403 après le paiement | PayPal : le Webhook est parfois en retard — se déconnecter puis se reconnecter pour rafraîchir le statut (la connexion revérifie le dernier statut en base) ; WeChat : confirmation manuelle pas encore terminée, attendre un peu ; Huawei : vérifier si la page de succès de paiement intégré est apparue |
| La page d'abonnement affiche "No subscription plans available" | Aucune formule PayPal disponible sur `/api/subscription/plans` — un problème de configuration côté plateforme ; demander à l'utilisateur de réessayer plus tard |
| Paiement WeChat effectué mais non activé | La confirmation manuelle est asynchrone ; si rien n'est activé après quelques heures, contacter le support de la plateforme (dongtao@outlook.com) |

## Remarque : Alipay

Le code contient un ensemble de paiement web Alipay (`src/lib/alipay.ts`, `/api/payment/create-order`, mode d'achat unique : adhésion classique ¥9,90 / adhésion premium ¥99 ; dégradation automatique vers un paiement simulé si la clé sandbox n'est pas configurée), **mais il n'est pas branché à l'UI de la page d'abonnement** — du code inactif/en réserve. Si Alipay doit un jour être activé sur la page d'abonnement, ce code prêt à l'emploi peut être raccordé — cela ne concerne pas ce skill et n'est mentionné ici que pour référence côté plateforme.