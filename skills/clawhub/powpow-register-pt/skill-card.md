## Description:

Ajuda usuários a criar uma conta PowPow na Bubble, resolver problemas de registro e ativar a assinatura para usar o mapa, o feed e o chat com humanos digitais.

This skill is ready for commercial/non-commercial use.

## Publisher:

[durenzidu](https://clawhub.ai/user/durenzidu)

### License/Terms of Use:

MIT-0

## Use Case:

Usuários finais de língua portuguesa usam este skill para conhecer a Bubble/PowPow, criar uma conta, entender erros comuns de cadastro e concluir a ativação da assinatura nas páginas oficiais. O agente fornece orientação textual passo a passo; o usuário realiza o registro, a verificação de e-mail e o pagamento no navegador ou aplicativo.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A user may disclose a password, e-mail verification code, or payment proof while asking for registration help.

Mitigation: The skill instructs the agent not to request or receive these secrets; users complete credential entry, verification, and payment only on official PowPow pages.

Risk: A user may expect the assistant to complete payment or subscription activation on their behalf.

Mitigation: The skill limits payment help to navigation and explanation, and directs users to the official subscription page or app payment channel.

Risk: Registration or payment behavior may change after the skill documentation was authored.

Mitigation: The skill tells the agent not to invent platform rules and to defer to the live PowPow behavior when it differs from the documented flow.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/durenzidu/skills/powpow-register-pt)
- [Publisher profile](https://clawhub.ai/user/durenzidu)
- [PowPow official site](https://global.powpow.online)
- [Registration page](https://global.powpow.online/register)
- [Subscription page](https://global.powpow.online/subscription)
- [registration-flow.md](artifact/references/registration-flow.md)
- [payment-and-activation.md](artifact/references/payment-and-activation.md)
- [screenshots.md](artifact/references/screenshots.md)
- [Bubble product video](https://www.bilibili.com/video/BV1Wu826UEVz/)

## Skill Output:

**Output Type(s):** [Guidance, Text, Markdown]

**Output Format:** [Portuguese Markdown with step-by-step instructions, troubleshooting guidance, and links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guidance-only; no scripts, local file access, credential collection, or automatic payment actions.]

## Skill Version(s):

1.0.0 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
