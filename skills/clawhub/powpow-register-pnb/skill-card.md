## Description:

Guides users through PowPow account registration, email verification, Alipay or PayPal subscription activation, and one-click sign-in.

This skill is ready for commercial/non-commercial use.

## Publisher:

[durenzidu](https://clawhub.ai/user/durenzidu)

### License/Terms of Use:

MIT-0

## Use Case:

PowPow users and their agents use this skill to create an account, resolve registration issues, complete a paid subscription, and access the activated account. If the assisted flow is unavailable, it provides instructions for completing registration and payment in the browser.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Passwords, verification codes, and sign-in links may expose account access if shared or retained in chat.

Mitigation: Treat codes and links as sensitive, keep them within the current session, and avoid sharing passwords unnecessarily.

Risk: The assisted flow creates live payment orders, and PayPal subscriptions may renew automatically.

Mitigation: Confirm the payment provider and subscription terms with the user before proceeding; let the user complete payment at the provider's checkout.

Risk: Session-related data may remain in local temporary files or chat logs.

Mitigation: Run the documented cleanup after use; choose manual browser registration and payment if local or chat handling is unacceptable.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/durenzidu/skills/powpow-register-pnb)
- [PowPow homepage](https://global.powpow.online)
- [Registration flow](references/registration-flow.md)
- [Agent flow](references/agent-flow.md)
- [Payment and activation](references/payment-and-activation.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Conversational text with links and optional shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Provides payment and sign-in links; requires Node.js 18 or later for the assisted flow.]

## Skill Version(s):

2.1.0 (source: release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
