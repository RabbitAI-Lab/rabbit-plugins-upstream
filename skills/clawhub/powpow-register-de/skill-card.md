## Description:

Hilft Nutzer:innen, ein PowPow- (Bubble-)Konto zu registrieren, typische Registrierungsprobleme zu beheben und das Abonnement ueber die offiziellen PowPow-Seiten zu aktivieren.

This skill is ready for commercial/non-commercial use.

## Publisher:

[durenzidu](https://clawhub.ai/user/durenzidu)

### License/Terms of Use:

MIT-0

## Use Case:

External German-speaking PowPow/Bubble users use this skill to understand the product, open the official registration and subscription pages, follow field-by-field account setup guidance, and troubleshoot registration or activation issues without sharing credentials in chat.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A user could share passwords, verification codes, or payment confirmations in chat while following registration guidance.

Mitigation: Keep credentials, verification codes, and payment confirmations on the official PowPow website or app; the skill must not request or process them.

Risk: Registration, rate-limit, or subscription details may become stale if the PowPow platform changes.

Mitigation: Use the official PowPow pages as the authority during registration and avoid inventing platform rules beyond the supplied references.

Risk: The skill discusses payment activation, but a chat skill cannot safely pay or submit payment interfaces for a user.

Mitigation: Direct users to the official subscription page and keep all PayPal, WeChat QR, or Huawei IAP actions under user control.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/durenzidu/skills/powpow-register-de)
- [Official PowPow website](https://global.powpow.online)
- [Registration page](https://global.powpow.online/register)
- [Subscription page](https://global.powpow.online/subscription)
- [Bubble introduction video](https://www.bilibili.com/video/BV1Wu826UEVz/)
- [Registration flow reference](artifact/references/registration-flow.md)
- [Payment and activation reference](artifact/references/payment-and-activation.md)
- [Product screenshots reference](artifact/references/screenshots.md)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [German-language conversational guidance with links and concise next-step blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [No code execution; registration, verification, and payment actions remain on official PowPow pages.]

## Skill Version(s):

1.0.0 (source: frontmatter, release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
