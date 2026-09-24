## Description:

Provides Urdu-language, step-by-step guidance for registering a PowPow (بابل) account, resolving common signup issues, and activating a subscription without handling user credentials or payments.

This skill is ready for commercial/non-commercial use.

## Publisher:

[durenzidu](https://clawhub.ai/user/durenzidu)

### License/Terms of Use:

MIT-0

## Use Case:

External Urdu-speaking PowPow users use this skill to understand the product, complete registration in their own browser or app, troubleshoot verification and activation issues, and navigate subscription options without sharing secrets in chat.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Users may disclose passwords, verification codes, or payment receipts in chat while asking for registration help.

Mitigation: The skill instructs the agent not to request or collect those values and keeps registration and payment actions on official PowPow pages.

Risk: Users may expect the agent to complete payment or subscription activation for them.

Mitigation: The skill limits its role to guidance, directs users to the official subscription page, and avoids payment handling or receipt collection.

Risk: Screenshots or product links could be copied from local or unverified locations.

Mitigation: The skill uses the documented hosted screenshot links and the official PowPow website, registration, and subscription URLs.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/durenzidu/skills/powpow-register-ur)
- [PowPow official website](https://global.powpow.online)
- [PowPow registration page](https://global.powpow.online/register)
- [PowPow subscription page](https://global.powpow.online/subscription)
- [PowPow introduction video](https://www.bilibili.com/video/BV1Wu826UEVz/)
- [registration-flow.md](references/registration-flow.md)
- [payment-and-activation.md](references/payment-and-activation.md)
- [screenshots.md](references/screenshots.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown text with links, troubleshooting steps, and next-step prompts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [No local code execution; the skill guides the user through official PowPow pages and avoids collecting passwords, verification codes, or payment receipts.]

## Skill Version(s):

1.0.0 (source: SKILL.md frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
