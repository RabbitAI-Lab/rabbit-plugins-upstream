## Description:

Begleitet Nutzer:innen bei der PowPow-Registrierung, der Aktivierung eines Alipay- oder PayPal-Abonnements und dem anschließenden Ein-Klick-Login.

This skill is ready for commercial/non-commercial use.

## Publisher:

[durenzidu](https://clawhub.ai/user/durenzidu)

### License/Terms of Use:

MIT-0

## Use Case:

PowPow-Neulinge können mit diesem Skill ein Konto einrichten und Probleme bei E-Mail-Bestätigung, Anmeldung oder Abo-Aktivierung lösen. Der Agent unterstützt die Registrierung und bereitet die Zahlung vor; Nutzer:innen bestätigen ihre E-Mail und bezahlen selbst an der Kasse.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The agent handles an email verification code and an account password during registration.

Mitigation: Only use this skill if comfortable sharing the verification code with the agent; supply the password through an environment variable, or register manually on the website.

Risk: Generated sign-in links contain session tokens, and session and payment state is stored locally for part of the flow.

Mitigation: Treat sign-in links as sensitive, avoid sharing them, and run cleanup after finishing.

Risk: The agent creates payment orders and opens an external checkout during subscription activation.

Mitigation: Review the checkout and complete the payment yourself; choose manual website payment if you do not want the agent involved.

## Reference(s):

- [PowPow-Skill auf ClawHub](https://clawhub.ai/durenzidu/skills/powpow-register-de)
- [Offizielle PowPow-Website](https://global.powpow.online)
- [PowPow-Registrierung](https://global.powpow.online/register)
- [Registrierungsablauf](references/registration-flow.md)
- [Zahlung und Aktivierung](references/payment-and-activation.md)
- [Agentenablauf](references/agent-flow.md)

## Skill Output:

**Output Type(s):** [Text, Guidance, Shell commands]

**Output Format:** [Markdown with links and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can provide product screenshots, sign-in links and a summary of account details.]

## Skill Version(s):

2.1.0 (source: frontmatter, server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
