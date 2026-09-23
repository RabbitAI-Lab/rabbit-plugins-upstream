## Description:

Ayuda paso a paso para crear una cuenta en PowPow (Bubble), resolver errores comunes y activar la suscripcion para usar el mapa y el chat con humanos digitales.

This skill is ready for commercial/non-commercial use.

## Publisher:

[durenzidu](https://clawhub.ai/user/durenzidu)

### License/Terms of Use:

MIT-0

## Use Case:

External Spanish-speaking PowPow/Bubble users use this skill to understand the product, register an account, troubleshoot common registration problems, and complete subscription activation through the official web or app flow.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill discusses registration, verification, and subscription activation where users may encounter passwords, email codes, or payment proof.

Mitigation: Keep passwords, email codes, and payment proof inside the official website or app, and do not ask the user to share them in chat.

Risk: The artifact includes more internal authentication and rate-limit details than normal users need.

Mitigation: Use those details only for troubleshooting when relevant, and trim backend-oriented details from public-facing guidance where possible.

## Reference(s):

- [README](artifact/README.md)
- [Flujo de registro en detalle](artifact/references/registration-flow.md)
- [Activacion de suscripcion y pago](artifact/references/payment-and-activation.md)
- [Capturas de la interfaz del producto](artifact/references/screenshots.md)
- [PowPow official site](https://global.powpow.online)
- [PowPow registration page](https://global.powpow.online/register)
- [PowPow product video](https://www.bilibili.com/video/BV1Wu826UEVz/)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Spanish Markdown responses with links, image references, troubleshooting steps, and next-step prompts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Conversational guidance only; the user performs registration, credential entry, verification, and payment on official PowPow pages.]

## Skill Version(s):

1.0.0 (source: frontmatter, release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
