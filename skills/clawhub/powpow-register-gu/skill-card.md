## Description:

Guides Gujarati-speaking users through PowPow account registration, product orientation, common registration issues, and subscription activation while keeping credentials and payment steps on official PowPow pages.

This skill is ready for commercial/non-commercial use.

## Publisher:

[durenzidu](https://clawhub.ai/user/durenzidu)

### License/Terms of Use:

MIT-0

## Use Case:

External users use this agent skill to understand PowPow, create an account, troubleshoot registration or activation issues, and complete subscription activation themselves on the official PowPow web or app experience.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Users may accidentally share passwords, verification codes, or payment proof in chat while following registration guidance.

Mitigation: Keep account creation, verification, and payment on the official PowPow pages; the agent should guide the user without requesting or receiving those sensitive values.

Risk: Outdated field rules or payment behavior could produce incorrect registration guidance if the PowPow service changes.

Mitigation: Treat the official PowPow pages as authoritative at runtime and use the bundled registration and activation references only as troubleshooting guidance.

Risk: Incorrect or untrusted screenshot links could misrepresent the product experience.

Mitigation: Use only the hosted screenshot links documented in the screenshot reference, and share only the screenshots relevant to the current user question.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/durenzidu/skills/powpow-register-gu)
- [PowPow official website](https://global.powpow.online)
- [PowPow registration page](https://global.powpow.online/register)
- [PowPow subscription page](https://global.powpow.online/subscription)
- [Product overview video](https://www.bilibili.com/video/BV1Wu826UEVz/)
- [Registration flow reference](artifact/references/registration-flow.md)
- [Payment and activation reference](artifact/references/payment-and-activation.md)
- [Screenshot reference](artifact/references/screenshots.md)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Gujarati conversational guidance with concise Markdown links and next-step blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guide-only output; the agent does not submit forms, collect credentials, collect verification codes, process payment proof, or run scripts.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
