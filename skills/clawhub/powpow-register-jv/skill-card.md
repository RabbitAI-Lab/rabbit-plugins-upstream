## Description:

Javanese-language guidance for introducing PowPow Gelembung, helping users register an account, troubleshoot signup issues, and complete subscription activation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[durenzidu](https://clawhub.ai/user/durenzidu)

### License/Terms of Use:

MIT-0

## Use Case:

External users and support agents use this skill to guide Javanese-speaking users through PowPow registration, subscription activation, and common signup or payment troubleshooting. The skill provides instructions and links while leaving account creation, credential entry, and payment actions to the user in PowPow's own web or app interface.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Users may try to share passwords, email verification codes, or payment proof in chat while getting registration help.

Mitigation: The skill directs the agent not to ask for passwords, verification codes, or payment proof; users complete those steps directly in PowPow's web or app interface.

Risk: The guidance sends users to PowPow subscription pages and externally hosted public screenshot links.

Mitigation: Use only the documented PowPow pages and public screenshot links, and do not script payment flows, make payments for users, or download screenshots into the skill.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/durenzidu/skills/powpow-register-jv)
- [PowPow official site](https://global.powpow.online)
- [PowPow registration page](https://global.powpow.online/register)
- [PowPow subscription page](https://global.powpow.online/subscription)
- [PowPow introduction video](https://www.bilibili.com/video/BV1Wu826UEVz/)
- [Registration flow reference](references/registration-flow.md)
- [Payment and activation reference](references/payment-and-activation.md)
- [Screenshot interface reference](references/screenshots.md)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Conversational Markdown with links and concise next-step prompts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Documentation-only guidance; no scripts, API calls, credential collection, or payments are performed by the skill.]

## Skill Version(s):

1.0.0 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
