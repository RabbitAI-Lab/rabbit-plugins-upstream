## Description:

Ajuda usuários a criar uma conta PowPow, verificar o e-mail, ativar uma assinatura pelo Alipay ou PayPal e acessar a plataforma por um link de login.

This skill is ready for commercial/non-commercial use.

## Publisher:

[durenzidu](https://clawhub.ai/user/durenzidu)

### License/Terms of Use:

MIT-0

## Use Case:

Pessoas que desejam usar o PowPow podem obter ajuda para criar a conta, resolver problemas de verificação e ativar uma assinatura. O usuário confirma o código recebido por e-mail e conclui pessoalmente o pagamento no Alipay ou PayPal; sem Node.js 18 ou superior, a skill oferece orientação manual.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A skill armazena temporariamente um token reutilizável de login em um arquivo de nome previsível durante etapas de conta e cobrança.

Mitigation: Use em uma máquina confiável de usuário único, execute a limpeza ao terminar e prefira o fluxo manual se não quiser criar um token local temporário.

Risk: O agente ajuda a criar uma conta, processar a verificação por e-mail e iniciar um pedido de assinatura.

Mitigation: Autorize essas etapas conscientemente e confirme que o navegador está nas páginas oficiais do PowPow, Alipay ou PayPal antes de pagar.

Risk: A assinatura PayPal pode implicar cobranças recorrentes.

Mitigation: Confirme deliberadamente os termos de renovação antes de autorizar a assinatura no PayPal.

## Reference(s):

- [Página da skill no ClawHub](https://clawhub.ai/durenzidu/skills/powpow-register-pt)
- [Site oficial do PowPow](https://global.powpow.online)
- [Fluxo de registro](references/registration-flow.md)
- [Pagamento e ativação](references/payment-and-activation.md)
- [Fluxo do agente](references/agent-flow.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Respostas em texto ou Markdown com instruções, comandos e links de login ou pagamento]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [O pagamento é concluído pelo usuário no provedor escolhido; a skill não publica diários nem cria humanos digitais.]

## Skill Version(s):

2.1.0 (source: release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
