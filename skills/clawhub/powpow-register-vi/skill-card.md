## Description:

Helps users register a PowPow account, activate a membership through Alipay, and sign in using a one-click link.

This skill is ready for commercial/non-commercial use.

## Publisher:

[durenzidu](https://clawhub.ai/user/durenzidu)

### License/Terms of Use:

MIT-0

## Use Case:

External users and their agents use this skill to complete PowPow signup, troubleshoot registration, and activate a paid membership. The agent can guide the process or assist with account creation and order tracking; the user supplies an email verification code and completes payment themselves.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Signup sends the user's email and chosen profile details to PowPow.

Mitigation: Ask for the user's consent and send only the details needed to create the account.

Risk: Account credentials and a temporary local session token require careful handling.

Mitigation: Keep the password out of command arguments and files, avoid sharing sign-in links, and run cleanup after registration.

Risk: Activating membership creates an Alipay checkout order involving a real payment.

Mitigation: Have the user review the order and pay only on the official checkout page; never request Alipay credentials or pay on their behalf.

## Reference(s):

- [PowPow registration skill on ClawHub](https://clawhub.ai/durenzidu/skills/powpow-register-vi)
- [PowPow homepage](https://global.powpow.online)
- [Registration flow](artifact/references/registration-flow.md)
- [Payment and activation](artifact/references/payment-and-activation.md)
- [Agent flow](artifact/references/agent-flow.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands]

**Output Format:** [Markdown with links and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes registration and checkout steps, status updates, and sign-in links.]

## Skill Version(s):

2.0.1 (source: skill frontmatter and ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
