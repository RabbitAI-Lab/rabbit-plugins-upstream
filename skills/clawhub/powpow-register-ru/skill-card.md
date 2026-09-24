## Description:

Helps Russian-speaking users understand PowPow, create an account, troubleshoot registration issues, and activate a subscription without handling credentials or payments in chat.

This skill is ready for commercial/non-commercial use.

## Publisher:

[durenzidu](https://clawhub.ai/user/durenzidu)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to guide Russian-speaking users through PowPow onboarding: product introduction, account registration, common registration errors, and subscription activation. The skill is informational and directs users to complete forms, verification, login, and payment directly on PowPow.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Users may try to share passwords, verification codes, or payment details in chat while asking for registration help.

Mitigation: The agent should not request or accept those secrets and should direct users to enter credentials, verification codes, and payment information only on PowPow or the relevant payment provider.

Risk: The skill sends users to registration, subscription, and public screenshot links, which could be misused if links are altered or presented without context.

Mitigation: Use the documented PowPow URLs and screenshot references, explain the purpose of each link, and keep payment or login actions under the user's direct control.

## Reference(s):

- [PowPow home page](https://global.powpow.online)
- [PowPow registration page](https://global.powpow.online/register)
- [PowPow subscription page](https://global.powpow.online/subscription)
- [PowPow introductory video](https://www.bilibili.com/video/BV1Wu826UEVz/)
- [Registration flow reference](references/registration-flow.md)
- [Payment and activation reference](references/payment-and-activation.md)
- [Product screenshots reference](references/screenshots.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown or plain text guidance with relevant links and screenshot references]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Russian-language user guidance; no code execution, form submission, credential handling, or payment processing.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
