## Description:

Accompagne les utilisateurs dans l’inscription à PowPow Bulle, l’activation de leur abonnement via Alipay ou PayPal et la connexion à leur compte.

This skill is ready for commercial/non-commercial use.

## Publisher:

[durenzidu](https://clawhub.ai/user/durenzidu)

### License/Terms of Use:

MIT-0

## Use Case:

Les utilisateurs de PowPow Bulle peuvent demander à leur agent de les guider dans l’inscription, de traiter les difficultés courantes, puis de les aider à activer leur abonnement ; ils saisissent eux-mêmes leur code reçu par e-mail et finalisent le paiement auprès d’Alipay ou de PayPal.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: La compétence traite des mots de passe, des codes de vérification et des jetons de session.

Mitigation: Ne partagez pas les liens de connexion, traitez-les comme des accès sensibles et supprimez l’état temporaire après le parcours.

Risk: L’activation de l’abonnement implique un paiement et peut entraîner un renouvellement automatique avec PayPal.

Mitigation: Vérifiez le montant et les conditions de renouvellement, puis payez uniquement sur les pages officielles Alipay ou PayPal.

## Reference(s):

- [Fiche ClawHub de la compétence](https://clawhub.ai/durenzidu/skills/powpow-register-fr)
- [Site PowPow Bulle](https://global.powpow.online)
- [Parcours d’inscription](references/registration-flow.md)
- [Paiement et activation](references/payment-and-activation.md)
- [Parcours de l’agent](references/agent-flow.md)

## Skill Output:

**Output Type(s):** [Guidance, Text, Links, Images]

**Output Format:** [Réponses conversationnelles en Markdown, liens de connexion et de paiement, captures d’écran facultatives]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Inscription et activation assistées ; mode guide sans Node.js 18 ou plus.]

## Skill Version(s):

2.1.0 (source: métadonnées de la version et frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
