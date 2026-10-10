## Description:

Helps users register a PowPow account, activate a subscription through Alipay, and obtain one-click login links through a guided conversation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[durenzidu](https://clawhub.ai/user/durenzidu)

### License/Terms of Use:

MIT-0

## Use Case:

PowPow users can ask an agent to guide or assist with account creation, email verification, subscription ordering, payment-status checks, and login. Users provide their own verification code and complete payment themselves on the Alipay page.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Account setup involves an email address, password choice, verification code, and possibly an avatar path.

Mitigation: Share these only when needed for registration, and run cleanup afterward to remove local token state.

Risk: Subscription ordering creates a payment handoff.

Mitigation: Complete payment personally on the Alipay page; do not give payment credentials to the agent.

## Reference(s):

- [PowPow website](https://global.powpow.online)
- [PowPow registration](https://global.powpow.online/register)
- [PowPow skill on ClawHub](https://clawhub.ai/durenzidu/skills/powpow-register-te)

## Skill Output:

**Output Type(s):** [Text, Guidance, Links]

**Output Format:** [Markdown conversation with login and payment links and optional screenshots]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Agent-assisted signup requires Node.js 18 or later; otherwise the skill provides guidance only.]

## Skill Version(s):

2.0.1 (source: release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
