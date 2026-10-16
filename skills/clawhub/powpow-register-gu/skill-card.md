## Description:

Guides Gujarati-speaking users through PowPow registration, email verification, subscription activation via Alipay or PayPal, and one-click login.

This skill is ready for commercial/non-commercial use.

## Publisher:

[durenzidu](https://clawhub.ai/user/durenzidu)

### License/Terms of Use:

MIT-0

## Use Case:

PowPow users can use this Gujarati-language assistant to register an account, troubleshoot verification or activation, complete a subscription checkout themselves, and obtain a login link. It does not create posts or digital humans.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Account email, password, verification code, and optional profile information pass through the agent during registration.

Mitigation: Review the skill before installing, especially on shared machines; provide the password through an environment variable and avoid sharing unnecessary personal details.

Risk: A live session token and subscription order details are kept in a predictable temporary file.

Mitigation: Avoid shared machines where possible and run the skill's cleanup step when finished.

Risk: Subscription checkout involves real payment, and PayPal is described as auto-renewing.

Mitigation: Confirm checkout opens the official Alipay or PayPal flow; complete payment yourself, never give payment credentials to the agent, and review renewal terms.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/durenzidu/skills/powpow-register-gu)
- [PowPow official website](https://global.powpow.online)
- [Agent-assisted workflow](artifact/references/agent-flow.md)
- [Registration workflow](artifact/references/registration-flow.md)
- [Payment and activation](artifact/references/payment-and-activation.md)

## Skill Output:

**Output Type(s):** [Text, Guidance, Shell commands]

**Output Format:** [Conversational Markdown with links and optional shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Provides registration and checkout links, next-step guidance, and account activation status.]

## Skill Version(s):

2.1.0 (source: skill frontmatter and server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
