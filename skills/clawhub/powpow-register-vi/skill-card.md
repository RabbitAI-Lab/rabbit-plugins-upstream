## Description:

Helps users register for PowPow, verify their email, activate a membership through Alipay or PayPal, and receive a one-click login link.

This skill is ready for commercial/non-commercial use.

## Publisher:

[durenzidu](https://clawhub.ai/user/durenzidu)

### License/Terms of Use:

MIT-0

## Use Case:

PowPow users can use this skill to create an account, resolve registration issues, and complete membership activation. The agent guides email verification and checkout, while the user supplies the verification code and pays at the checkout page.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Registration sends the user's email and password to PowPow.

Mitigation: Use the skill only if you are comfortable providing these credentials to PowPow; keep the password private.

Risk: Generated one-click login links grant access to the user's account.

Mitigation: Treat login links as sensitive and do not share them.

Risk: Temporary registration state contains a session token.

Mitigation: Run the skill's cleanup step when finished.

## Reference(s):

- [PowPow Register on ClawHub](https://clawhub.ai/durenzidu/skills/powpow-register-vi)
- [PowPow homepage](https://global.powpow.online)
- [Agent flow](references/agent-flow.md)
- [Registration flow](references/registration-flow.md)
- [Payment and activation](references/payment-and-activation.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Links]

**Output Format:** [Markdown text with commands and checkout or login links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Node.js 18 or newer for assisted signup; otherwise provides manual guidance.]

## Skill Version(s):

2.1.0 (source: skill frontmatter and ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
