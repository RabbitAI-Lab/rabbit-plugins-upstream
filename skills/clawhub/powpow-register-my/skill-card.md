## Description:

Guides users through PowPow account registration, email verification, Alipay or PayPal subscription checkout, and account activation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[durenzidu](https://clawhub.ai/user/durenzidu)

### License/Terms of Use:

MIT-0

## Use Case:

PowPow customers use this skill to register an account, resolve verification or activation issues, and complete subscription checkout while retaining control of payment approval.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Registration uses an email verification code and account password.

Mitigation: Use the code only for PowPow verification, pass the password through the designated environment variable rather than command arguments or files, and avoid repeating credentials in chat.

Risk: A session token may be stored temporarily while signup and activation are in progress.

Mitigation: Run the documented cleanup step after completion and do not share login links or tokens with others.

Risk: PayPal checkout may start a monthly auto-renewing subscription.

Mitigation: Confirm the recurring terms before approving payment; the agent should only open checkout and check status, not handle payment credentials.

## Reference(s):

- [PowPow website](https://global.powpow.online)
- [ClawHub skill release](https://clawhub.ai/durenzidu/skills/powpow-register-my)
- [Agent workflow](references/agent-flow.md)
- [Registration guide](references/registration-flow.md)
- [Payment and activation guide](references/payment-and-activation.md)
- [Product screenshots](references/screenshots.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Links]

**Output Format:** [Conversational text and Markdown with links and optional shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Provides checkout and login links; payment authorization remains with the user.]

## Skill Version(s):

2.1.0 (source: skill frontmatter and ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
