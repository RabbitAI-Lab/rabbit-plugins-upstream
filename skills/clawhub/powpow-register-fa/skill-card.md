## Description:

Guides Persian-speaking users through PowPow account registration, subscription activation, common sign-up errors, and introductory product screenshots without collecting credentials or acting on the user's behalf.

This skill is ready for commercial/non-commercial use.

## Publisher:

[durenzidu](https://clawhub.ai/user/durenzidu)

### License/Terms of Use:

MIT-0

## Use Case:

External Persian-speaking PowPow users use this skill to understand the Bubble product, open the correct registration and subscription pages, resolve common registration or activation problems, and learn what information they should keep private. The agent provides step-by-step guidance only; the user completes registration, verification, and payment in the PowPow web or app interface.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A user could share passwords, email verification codes, or payment details during a guided registration conversation.

Mitigation: The skill must keep registration and payment inside the PowPow web or app interface and must not ask for passwords, verification codes, or payment details.

Risk: A user may expect the agent to submit registration, subscription, or payment actions on their behalf.

Mitigation: The skill should provide guidance only and should direct the user to complete all account, verification, and payment actions themselves.

Risk: Registration or payment behavior may differ if the live PowPow platform changes after the reference files were written.

Mitigation: The skill should treat the live platform behavior as authoritative and use the bundled reference files only as support for troubleshooting.

## Reference(s):

- [Registration flow reference](references/registration-flow.md)
- [Payment and activation reference](references/payment-and-activation.md)
- [Product screenshots reference](references/screenshots.md)
- [PowPow website](https://global.powpow.online)
- [PowPow registration page](https://global.powpow.online/register)
- [PowPow subscription page](https://global.powpow.online/subscription)
- [PowPow introduction video](https://www.bilibili.com/video/BV1Wu826UEVz/)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Text]

**Output Format:** [Persian conversational guidance with Markdown links and optional hosted screenshot links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [No scripts, local execution, dependency installation, or credential handling.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
