## Description:

Guides Punjabi-speaking users through PowPow account registration, email verification, subscription activation, and common registration or payment blockers.

This skill is ready for commercial/non-commercial use.

## Publisher:

[durenzidu](https://clawhub.ai/user/durenzidu)

### License/Terms of Use:

MIT-0

## Use Case:

External Punjabi-speaking PowPow users use this skill to understand the product, create an account on the official registration page, troubleshoot verification issues, and activate a subscription without sharing credentials in chat.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Users may disclose passwords, verification codes, third-party login details, or payment credentials in chat.

Mitigation: The skill instructs users to complete credentials, verification, login, and payment only on official PowPow or provider pages and not in chat.

Risk: Subscription activation can be delayed after payment, especially for manual WeChat verification.

Mitigation: The skill distinguishes PayPal webhook activation, WeChat manual confirmation, and Huawei IAP activation, and guides users to wait or contact platform support when appropriate.

Risk: PowPow registration, field validation, or payment behavior may change after the skill release.

Mitigation: The skill treats the live PowPow page as authoritative and uses its reference files only as troubleshooting guidance.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/durenzidu/skills/powpow-register-pa)
- [PowPow website](https://global.powpow.online)
- [PowPow registration page](https://global.powpow.online/register)
- [PowPow subscription page](https://global.powpow.online/subscription)
- [PowPow introduction video](https://www.bilibili.com/video/BV1Wu826UEVz/)
- [Registration flow reference](references/registration-flow.md)
- [Payment and activation reference](references/payment-and-activation.md)
- [Screenshot reference](references/screenshots.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Punjabi conversational guidance with Markdown links and next-step blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [No executable code; directs users to official PowPow pages for registration, verification, third-party login, and payment.]

## Skill Version(s):

1.0.0 (source: SKILL.md frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
