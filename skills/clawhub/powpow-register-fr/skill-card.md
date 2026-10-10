## Description:

Accompagne les utilisateurs dans l'inscription à PowPow (Bulle), l'activation de leur abonnement via Alipay et la connexion en un clic.

This skill is ready for commercial/non-commercial use.

## Publisher:

[durenzidu](https://clawhub.ai/user/durenzidu)

### License/Terms of Use:

MIT-0

## Use Case:

Les utilisateurs de PowPow peuvent créer un compte avec l'aide de l'agent, recevoir un code de vérification par e-mail, choisir un abonnement et se connecter. L'agent aide aussi à résoudre les blocages d'inscription et d'activation ; l'utilisateur effectue lui-même le paiement.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Les informations d'inscription sont envoyées à PowPow et un jeton de session temporaire est conservé pendant la configuration.

Mitigation: N'utiliser ce flux qu'avec l'accord de l'utilisateur et supprimer l'état temporaire à la fin.

Risk: Le parcours ouvre une page de paiement Alipay.

Mitigation: Effectuer le paiement uniquement sur la page officielle ; ne jamais communiquer ses identifiants ou moyens de paiement à l'agent.

## Reference(s):

- [Page de la compétence sur ClawHub](https://clawhub.ai/durenzidu/skills/powpow-register-fr)
- [Site officiel de PowPow](https://global.powpow.online)
- [Flux d'inscription](references/registration-flow.md)
- [Paiement et activation](references/payment-and-activation.md)
- [Flux pris en charge par l'agent](references/agent-flow.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Réponses en français avec liens et instructions de suivi]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Peut fournir des captures du produit, des liens de connexion et un accès à la caisse Alipay.]

## Skill Version(s):

2.0.1 (source: frontmatter et publication ClawHub)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
