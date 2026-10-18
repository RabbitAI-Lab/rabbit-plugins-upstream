## Description:

Guides users through PowPow account registration, email verification, Alipay or PayPal membership activation, and one-click sign-in.

This skill is ready for commercial/non-commercial use.

## Publisher:

[durenzidu](https://clawhub.ai/user/durenzidu)

### License/Terms of Use:

MIT-0

## Use Case:

PowPow users can ask an assistant to help create an account, resolve registration or activation issues, and set up a paid membership while completing checkout themselves. The skill does not publish posts or create digital humans.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The assistant handles the account password and email verification code during registration.

Mitigation: Use manual web registration if you do not want an assistant handling credentials; review this access before installing.

Risk: A PowPow session token is stored locally during the registration flow.

Mitigation: Run the skill's cleanup step after use to remove temporary session data.

Risk: The assistant creates Alipay or PayPal checkout sessions, which may exceed a user's intended consent scope.

Mitigation: Confirm the payment option and checkout details yourself, and complete payment directly in the provider's checkout.

## Reference(s):

- [PowPow Register ClawHub release](https://clawhub.ai/durenzidu/skills/powpow-register-ha)
- [PowPow website](https://global.powpow.online)
- [Registration flow](references/registration-flow.md)
- [Payment and activation](references/payment-and-activation.md)
- [Agent flow](references/agent-flow.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Text]

**Output Format:** [Markdown with links and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes registration progress, checkout guidance, and sign-in links.]

## Skill Version(s):

2.1.0 (source: frontmatter and ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
