## Description:

Guides users through PowPow account registration, email verification, Alipay or PayPal subscription activation, and one-click sign-in.

This skill is ready for commercial/non-commercial use.

## Publisher:

[durenzidu](https://clawhub.ai/user/durenzidu)

### License/Terms of Use:

MIT-0

## Use Case:

PowPow users can ask an agent to set up an account, handle email verification, open a payment page for subscription activation, and provide sign-in links. If the required runtime is unavailable, the agent provides guided instructions instead.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Registration involves an email address, password choice, and verification code.

Mitigation: Share these only for the requested account setup; use the official registration flow and do not repeat the password after setup.

Risk: A temporary local session token remains available until cleanup.

Mitigation: Run the skill's cleanup step after registration or when the user stops the process, and share sign-in links only with the intended user.

Risk: A subscription order can lead to a real payment or recurring PayPal charges.

Mitigation: Confirm the provider and plan with the user; have the user complete payment directly on the official Alipay or PayPal page.

## Reference(s):

- [PowPow skill on ClawHub](https://clawhub.ai/durenzidu/skills/powpow-register-ur)
- [PowPow website](https://global.powpow.online)
- [Registration flow](artifact/references/registration-flow.md)
- [Payment and activation](artifact/references/payment-and-activation.md)
- [Agent flow](artifact/references/agent-flow.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance, Shell commands]

**Output Format:** [Conversational Markdown with sign-in and payment links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Provides account and activation status; registration requires an email verification code and payment is completed by the user.]

## Skill Version(s):

2.1.0 (source: SKILL.md frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
