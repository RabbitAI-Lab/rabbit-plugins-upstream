## Description:

Guides users through PowPow account registration, email verification, subscription activation, and one-click sign-in within a conversation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[durenzidu](https://clawhub.ai/user/durenzidu)

### License/Terms of Use:

MIT-0

## Use Case:

PowPow users can ask an agent to help create an account, resolve registration issues, place a subscription order, confirm activation, and obtain sign-in links. The user supplies an email code and completes any payment personally in Alipay; without Node.js 18 or later, the skill provides manual guidance instead.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: On shared agent machines, a local session file can mix different users' account or payment flows.

Mitigation: Run one registration or payment flow at a time, avoid environments where conversations share an OS account, and clean up session state after completion.

Risk: The flow handles account details, a temporary sign-in token, optional avatar files, and payment order data.

Mitigation: Limit access to the intended user's session and leave payment entry and confirmation to the user in Alipay.

## Reference(s):

- [PowPow Register on ClawHub](https://clawhub.ai/durenzidu/skills/powpow-register)
- [PowPow website](https://global.powpow.online)
- [Agent-assisted registration flow](references/agent-flow.md)
- [Registration requirements and troubleshooting](references/registration-flow.md)
- [Payment and activation guidance](references/payment-and-activation.md)
- [Product screenshot guide](references/screenshots.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Conversational Markdown with sign-in and checkout links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include bundled product screenshots, registration updates, and account details; the user completes payment outside the conversation.]

## Skill Version(s):

2.0.1 (source: skill frontmatter and ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
