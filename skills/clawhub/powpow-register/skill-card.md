## Description:

Helps people register for PowPow, activate a subscription through Alipay, and sign in with a one-click link.

This skill is ready for commercial/non-commercial use.

## Publisher:

[durenzidu](https://clawhub.ai/user/durenzidu)

### License/Terms of Use:

MIT-0

## Use Case:

New PowPow users can get conversational help with account registration, email verification, subscription activation, and sign-in. The agent can submit registration details and create an Alipay order; the user enters their verification code and completes payment themselves.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Registration shares personal details with PowPow and temporarily stores account details and a session token on the device.

Mitigation: Use the skill only with the user's consent, avoid sharing the sign-in link, and run cleanup after registration to remove temporary state.

Risk: An optional avatar upload reads a local image supplied by the user.

Mitigation: Upload only an image the user explicitly chooses and intends to share with PowPow.

Risk: Subscription activation involves a real payment and a temporary local checkout page.

Mitigation: Confirm the selected plan and let the user pay only on the official Alipay checkout page; never ask the agent for payment credentials.

## Reference(s):

- [PowPow website](https://global.powpow.online)
- [PowPow registration](https://global.powpow.online/register)
- [PowPow subscription](https://global.powpow.online/subscription)
- [Agent registration flow](references/agent-flow.md)
- [Registration troubleshooting](references/registration-flow.md)
- [Payment and activation guidance](references/payment-and-activation.md)

## Skill Output:

**Output Type(s):** [Text, Guidance, Shell commands, Sign-in and checkout links]

**Output Format:** [Conversational Markdown with links and optional shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Node.js 18 or newer for assisted registration; falls back to manual guidance without it.]

## Skill Version(s):

2.0.0 (source: skill frontmatter and server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
