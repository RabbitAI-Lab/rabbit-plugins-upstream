## Description:

Assiste gli utenti nella registrazione a PowPow (Bolla), nell'attivazione dell'abbonamento tramite Alipay e nell'accesso al proprio account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[durenzidu](https://clawhub.ai/user/durenzidu)

### License/Terms of Use:

MIT-0

## Use Case:

Gli utenti di PowPow possono farsi guidare dall'agent nella creazione e attivazione di un account: l'agent raccoglie i dati necessari, gestisce il codice email, crea un ordine Alipay e verifica l'attivazione; l'utente conferma i dati e paga personalmente.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The agent handles registration details, a password and an email verification code.

Mitigation: Use only on a trusted device; provide the password through the designated environment variable, not a command argument, and share the verification code only for this registration.

Risk: A live session token is stored in a predictable temporary file and one-click login links provide account access.

Mitigation: Avoid shared or untrusted machines, limit exposure of login links, and run cleanup after completing or abandoning the flow.

Risk: The agent can create and query an Alipay subscription order.

Mitigation: Confirm the chosen plan and amount before creating the order; complete payment yourself at the official checkout without giving the agent payment credentials.

## Reference(s):

- [PowPow su ClawHub](https://clawhub.ai/durenzidu/skills/powpow-register-it)
- [Sito PowPow](https://global.powpow.online)
- [Flusso di registrazione](references/registration-flow.md)
- [Flusso dell'agent](references/agent-flow.md)
- [Pagamento e attivazione](references/payment-and-activation.md)
- [Screenshot del prodotto](references/screenshots.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Links]

**Output Format:** [Markdown with inline shell commands and account or payment links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can fall back to guidance-only mode when Node.js is unavailable.]

## Skill Version(s):

2.0.1 (source: skill frontmatter and server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
