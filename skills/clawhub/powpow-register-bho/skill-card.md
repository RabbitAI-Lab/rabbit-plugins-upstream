## Description:

Guides users through PowPow account registration, email verification, optional avatar upload, Alipay or PayPal subscription activation, and one-click login.

This skill is ready for commercial/non-commercial use.

## Publisher:

[durenzidu](https://clawhub.ai/user/durenzidu)

### License/Terms of Use:

MIT-0

## Use Case:

PowPow users can register and activate an account through an assisted conversation, then receive a one-click login link. The skill can also guide them through common registration and activation problems; it does not create posts or digital people.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Registration sends the user's email and optional avatar to PowPow.

Mitigation: Confirm the user agrees to sharing this information with PowPow before registering or uploading an avatar.

Risk: One-click login links and locally retained session state can expose account access.

Mitigation: Treat login links as secrets, share them only with the intended user, and run cleanup when the flow ends.

Risk: Payment orders and redirects may lead users to a fraudulent checkout or expose payment credentials.

Mitigation: Verify the browser is on official PowPow, PayPal, or Alipay domains before payment; the user pays directly and never shares payment credentials with the agent.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/durenzidu/skills/powpow-register-bho)
- [PowPow official website](https://global.powpow.online)
- [Agent flow](artifact/references/agent-flow.md)
- [Registration flow](artifact/references/registration-flow.md)
- [Payment and activation](artifact/references/payment-and-activation.md)

## Skill Output:

**Output Type(s):** [Text, Guidance, Shell commands, Images]

**Output Format:** [Chat messages with registration steps, login links, and optional bundled screenshots]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Node.js 18 or later for assisted execution; otherwise provides instructions only.]

## Skill Version(s):

2.1.0 (source: skill frontmatter and ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
