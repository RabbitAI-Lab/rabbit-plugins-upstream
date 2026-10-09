## Description:

Helps users register for PowPow (Bulle), activate a subscription through Alipay, and sign in with one-click links, with guidance if automated registration is unavailable.

This skill is ready for commercial/non-commercial use.

## Publisher:

[durenzidu](https://clawhub.ai/user/durenzidu)

### License/Terms of Use:

MIT-0

## Use Case:

People creating a PowPow account can use the agent to complete email-verified registration, arrange subscription payment, and troubleshoot activation or sign-in. The user retrieves the verification code and completes payment at the checkout.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Registration shares an email verification code and account details with PowPow.

Mitigation: Use the skill only if comfortable sending these details to global.powpow.online; share the code only for the requested registration.

Risk: Generated passwords and one-click login links grant sensitive account access.

Mitigation: Treat passwords and login links as secrets and do not share them.

Risk: A subscription order leads to an Alipay checkout, and temporary local token state may persist.

Mitigation: Review the checkout before paying and run cleanup after the flow to remove the temporary token state.

## Reference(s):

- [PowPow homepage](https://global.powpow.online)
- [Agent registration flow](references/agent-flow.md)
- [Registration rules and troubleshooting](references/registration-flow.md)
- [Payment and activation](references/payment-and-activation.md)
- [Product screenshots](references/screenshots.md)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Links, Images]

**Output Format:** [Markdown guidance with links and optional bundled JPEG screenshots]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Provides registration and payment-status guidance; may return one-click login and checkout links.]

## Skill Version(s):

2.0.1 (source: release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
