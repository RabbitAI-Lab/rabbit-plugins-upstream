## Description:

Helps users register a PowPow account, activate a subscription through Alipay, and sign in using one-click links within a guided conversation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[durenzidu](https://clawhub.ai/user/durenzidu)

### License/Terms of Use:

MIT-0

## Use Case:

PowPow users can ask an agent to guide account registration, email verification, and subscription activation. The agent can prepare registration details and an Alipay order, while the user supplies the verification code and completes payment themselves.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Registration involves an email address, password choice, and email verification code shared in chat.

Mitigation: Share these details only when you intend to create a PowPow account; keep credentials and verification codes private.

Risk: Generated one-click login links and temporary session details grant account access until cleanup.

Mitigation: Treat login links as sensitive and complete the skill's cleanup step after activation.

Risk: The agent can initiate an Alipay subscription order.

Mitigation: Review the order and complete payment yourself on the Alipay checkout page.

## Reference(s):

- [PowPow website](https://global.powpow.online)
- [ClawHub skill listing](https://clawhub.ai/durenzidu/skills/powpow-register-ar)
- [Registration flow](references/registration-flow.md)
- [Payment and activation](references/payment-and-activation.md)

## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [Markdown with links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include sensitive one-click sign-in and checkout links; payment is completed by the user.]

## Skill Version(s):

2.0.1 (source: ClawHub release, skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
