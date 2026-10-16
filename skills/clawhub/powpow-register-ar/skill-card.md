## Description:

Helps users register for PowPow, activate an Alipay or PayPal subscription, and obtain a one-click sign-in link through a guided conversation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[durenzidu](https://clawhub.ai/user/durenzidu)

### License/Terms of Use:

MIT-0

## Use Case:

PowPow users can ask an agent to create an account, resolve registration issues, and arrange subscription activation while completing email verification and payment themselves. The skill can also guide users through the official site if automated registration is unavailable.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The agent handles account credentials and email verification during registration.

Mitigation: Install only if you trust the publisher and PowPow; share verification codes only for the intended registration and avoid exposing passwords in commands or chat history.

Risk: One-click sign-in links contain reusable login tokens, including in locally stored session state.

Mitigation: Treat sign-in links like passwords, do not share them, and run the skill's cleanup step after registration.

Risk: Subscription setup involves payment and PayPal may renew automatically.

Mitigation: Verify the official payment page, price, and renewal terms before paying; complete payment yourself or use the official website manually.

## Reference(s):

- [PowPow official website](https://global.powpow.online)
- [PowPow registration](https://global.powpow.online/register)
- [Registration flow](references/registration-flow.md)
- [Payment and activation](references/payment-and-activation.md)
- [Agent flow](references/agent-flow.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Links]

**Output Format:** [Conversational text and Markdown with links and command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Provides registration progress, payment-page and sign-in links, and account details; may attach bundled product screenshots.]

## Skill Version(s):

2.1.0 (source: SKILL.md frontmatter and ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
