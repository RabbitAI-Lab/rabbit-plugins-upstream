## Description:

Guides users through PowPow registration, email verification, Alipay or PayPal subscription activation, and sign-in within a conversation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[durenzidu](https://clawhub.ai/user/durenzidu)

### License/Terms of Use:

MIT-0

## Use Case:

PowPow users and their agents use this skill to create accounts, resolve registration problems, complete a subscription checkout, and access an activated account. Users supply their email verification code and complete payment themselves.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Local registration state can mix passwords, verification codes, or login tokens between users on a shared installation.

Mitigation: Use only in a trusted single-user agent environment until state-file isolation is fixed; run cleanup after registration to remove stored session tokens.

Risk: A misleading checkout link could direct a user to an unsafe payment page.

Mitigation: Verify the Alipay or PayPal checkout URL in the browser before paying; the user completes payment directly.

Risk: A password shared during registration could be exposed or reused elsewhere.

Mitigation: Use a unique password and avoid reusing sensitive passwords.

## Reference(s):

- [PowPow skill listing](https://clawhub.ai/durenzidu/skills/powpow-register-jv)
- [PowPow homepage](https://global.powpow.online)
- [Agent workflow](references/agent-flow.md)
- [Registration workflow](references/registration-flow.md)
- [Payment and activation](references/payment-and-activation.md)

## Skill Output:

**Output Type(s):** [Text, Guidance, Shell commands]

**Output Format:** [Conversational text and Markdown with links and optional shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May provide checkout and one-click sign-in links; checkout requires user action.]

## Skill Version(s):

2.1.0 (source: SKILL.md frontmatter and server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
