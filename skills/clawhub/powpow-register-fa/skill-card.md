## Description:

Helps users register for PowPow, activate a subscription, and access their account through one-click login links.

This skill is ready for commercial/non-commercial use.

## Publisher:

[durenzidu](https://clawhub.ai/user/durenzidu)

### License/Terms of Use:

MIT-0

## Use Case:

PowPow users can ask an agent to guide or complete account registration, email verification, subscription checkout, and login. The user supplies account details, retrieves the email code, and completes payment on the payment page.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The agent handles the PowPow account password during registration.

Mitigation: Do not share payment credentials with the agent; keep account credentials private and use the documented registration flow.

Risk: A temporary PowPow session token remains on the local device during registration.

Mitigation: Run the documented cleanup step after registration and activation.

Risk: The skill opens a checkout page and polls for payment status.

Mitigation: Verify the payment page domain before paying and enter payment details only on the official payment page.

## Reference(s):

- [PowPow skill listing](https://clawhub.ai/durenzidu/skills/powpow-register-fa)
- [PowPow website](https://global.powpow.online)
- [Registration flow](references/registration-flow.md)
- [Payment and activation](references/payment-and-activation.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands]

**Output Format:** [Conversational text with links and optional shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May provide registration and login links, payment status, and troubleshooting steps.]

## Skill Version(s):

2.0.1 (source: release evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
