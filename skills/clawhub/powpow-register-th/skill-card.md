## Description:

PowPow Register is a Thai-language guidance skill that introduces PowPow, walks users through account registration, helps troubleshoot signup and activation issues, and points users to subscription options without collecting credentials or payment details.

This skill is ready for commercial/non-commercial use.

## Publisher:

[durenzidu](https://clawhub.ai/user/durenzidu)

### License/Terms of Use:

MIT-0

## Use Case:

External Thai-speaking PowPow users use this skill to understand the product, create an account in their browser or app, resolve common registration errors, and finish membership activation through PowPow-supported payment flows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Users may mistake registration guidance for permission to share credentials, verification codes, or payment proof with the assistant.

Mitigation: Keep account creation and payment inside PowPow or the relevant payment provider, and do not ask users to provide passwords, verification codes, or payment proof.

Risk: The skill sends users to external PowPow, screenshot, video, and payment-provider flows.

Mitigation: Make it clear when the user is opening an external page and keep payment decisions and actions in the official PowPow or provider interface.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/durenzidu/skills/powpow-register-th)
- [PowPow homepage](https://global.powpow.online)
- [PowPow registration page](https://global.powpow.online/register)
- [PowPow subscription page](https://global.powpow.online/subscription)
- [PowPow introduction video](https://www.bilibili.com/video/BV1Wu826UEVz/)
- [Registration flow reference](references/registration-flow.md)
- [Payment and activation reference](references/payment-and-activation.md)
- [Product screenshots reference](references/screenshots.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown conversation guidance with links and next-step action blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Thai-language guidance; no scripts, API calls, credential handling, or payment execution.]

## Skill Version(s):

1.0.0 (source: SKILL.md frontmatter and ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
