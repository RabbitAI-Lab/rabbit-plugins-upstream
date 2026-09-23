## Description:

Provides Marathi guidance for introducing PowPow, helping users register an account, troubleshoot registration issues, and complete subscription activation without collecting credentials or handling payment.

This skill is ready for commercial/non-commercial use.

## Publisher:

[durenzidu](https://clawhub.ai/user/durenzidu)

### License/Terms of Use:

MIT-0

## Use Case:

External users use this skill to understand PowPow, create and activate an account, and resolve common registration or subscription activation problems. The agent gives step-by-step guidance while the user completes forms, verification, and payment only on official PowPow pages or provider flows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Users may try to share passwords, verification codes, or payment proof in chat while registering or activating an account.

Mitigation: The assistant should not ask for passwords, verification codes, or payment proof; users should complete registration and payment only on official PowPow pages or provider flows.

Risk: Guidance about subscription activation could be mistaken for agent-side payment handling.

Mitigation: Keep the skill limited to navigation and troubleshooting guidance; do not submit forms, call payment interfaces, or attempt payment on the user's behalf.

## Reference(s):

- [ClawHub listing](https://clawhub.ai/durenzidu/skills/powpow-register-mr)
- [PowPow official website](https://global.powpow.online)
- [PowPow registration page](https://global.powpow.online/register)
- [PowPow subscription page](https://global.powpow.online/subscription)
- [Registration flow reference](references/registration-flow.md)
- [Payment and activation reference](references/payment-and-activation.md)
- [Screenshot reference](references/screenshots.md)
- [PowPow introduction video](https://www.bilibili.com/video/BV1Wu826UEVz/)

## Skill Output:

**Output Type(s):** [Guidance, Text, Markdown]

**Output Format:** [Marathi conversational guidance with Markdown links, images, and next-step prompts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guide-only; no scripts, dependency installation, credential collection, form submission, or agent-side payment handling.]

## Skill Version(s):

1.0.0 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
