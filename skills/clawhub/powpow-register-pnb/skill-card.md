## Description:

PowPow Register guides Punjabi-language users through PowPow account registration, subscription activation, and common registration or payment troubleshooting without handling passwords, verification codes, or payment details.

This skill is ready for commercial/non-commercial use.

## Publisher:

[durenzidu](https://clawhub.ai/user/durenzidu)

### License/Terms of Use:

MIT-0

## Use Case:

External PowPow users use this skill to understand the product, open the official registration or subscription pages, complete the required form and activation steps themselves, and troubleshoot common account setup issues in Punjabi.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A user may try to share passwords, verification codes, or payment details in chat while following registration guidance.

Mitigation: Keep all credential, verification, and payment entry on PowPow's official website or app, and do not request or process those values in the agent conversation.

Risk: A user may expect the agent to create the account, complete payment, or activate the subscription on their behalf.

Mitigation: Frame the skill as guidance only: the user performs registration and payment actions directly in PowPow, while the agent explains the next step and troubleshooting options.

Risk: Payment activation, especially manually confirmed WeChat payment, may not appear immediately.

Mitigation: Explain that some activation paths can take time, suggest re-login or waiting where appropriate, and direct unresolved issues to platform support rather than treating delayed activation as immediate failure.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/durenzidu/skills/powpow-register-pnb)
- [PowPow Official Site](https://global.powpow.online)
- [PowPow Registration Page](https://global.powpow.online/register)
- [PowPow Subscription Page](https://global.powpow.online/subscription)
- [registration-flow.md](references/registration-flow.md)
- [payment-and-activation.md](references/payment-and-activation.md)
- [screenshots.md](references/screenshots.md)
- [PowPow Product Video](https://www.bilibili.com/video/BV1Wu826UEVz/)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown-style conversational guidance with links and next-step instructions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Documentation-only guidance; no scripts, local execution, account actions, credential collection, or payment processing.]

## Skill Version(s):

1.0.0 (source: evidence release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
