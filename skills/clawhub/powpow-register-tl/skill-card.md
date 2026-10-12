## Description:

Helps people register a PowPow (Bula) account, activate a subscription through Alipay or PayPal, and receive a one-click sign-in link.

This skill is ready for commercial/non-commercial use.

## Publisher:

[durenzidu](https://clawhub.ai/user/durenzidu)

### License/Terms of Use:

MIT-0

## Use Case:

PowPow users can get guided account registration, resolve verification or activation problems, and complete subscription setup while paying directly at the checkout page.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Registration details and a temporary login token are handled during account setup.

Mitigation: Confirm that details are sent only to the official PowPow site and run the cleanup step when finished.

Risk: A checkout page is created or opened during subscription activation.

Mitigation: Pay directly through the checkout page; do not give the agent Alipay or PayPal credentials.

## Reference(s):

- [PowPow website](https://global.powpow.online)
- [ClawHub skill listing](https://clawhub.ai/durenzidu/skills/powpow-register-tl)
- [Registration flow](references/registration-flow.md)
- [Payment and activation](references/payment-and-activation.md)

## Skill Output:

**Output Type(s):** [Text, Guidance, Shell commands]

**Output Format:** [Markdown with links and optional shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes registration progress, checkout guidance, and one-click sign-in links; falls back to manual guidance without Node.js.]

## Skill Version(s):

2.1.0 (source: frontmatter and server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
