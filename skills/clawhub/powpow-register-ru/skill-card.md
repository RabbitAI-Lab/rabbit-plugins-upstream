## Description:

Guides users through PowPow account registration, email verification, subscription activation through Alipay, and one-click sign-in.

This skill is ready for commercial/non-commercial use.

## Publisher:

[durenzidu](https://clawhub.ai/user/durenzidu)

### License/Terms of Use:

MIT-0

## Use Case:

People creating a PowPow account use this skill to complete registration, verify their email, activate a subscription, and troubleshoot sign-in or payment issues. They can instead follow the manual website flow.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Delegated account creation involves an email verification code and account password.

Mitigation: Share the verification code only for registration; pass the password through the designated environment variable, not command arguments, or choose manual website registration.

Risk: A temporary PowPow session token is held during registration and sign-in.

Mitigation: Use the cleanup step after activation and avoid sharing sign-in links beyond the intended user.

Risk: Activating a subscription opens an Alipay checkout page and requires payment.

Mitigation: Have the user complete payment directly in the checkout page; the agent must not access their Alipay account or payment instruments.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/durenzidu/skills/powpow-register-ru)
- [PowPow official website](https://global.powpow.online)
- [Registration guidance](references/registration-flow.md)
- [Payment and activation guidance](references/payment-and-activation.md)
- [Agent-assisted registration flow](references/agent-flow.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Links]

**Output Format:** [Markdown text with commands and sign-in or checkout links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Node.js 18 or later for assisted registration; offers manual guidance otherwise.]

## Skill Version(s):

2.0.1 (source: frontmatter and server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
