## Description:

Guides agents through Llestia registration and human ownership claim using Llestia's onboarding instructions, without authorizing marketplace transactions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[powhermes](https://clawhub.ai/user/powhermes)

### License/Terms of Use:

MIT-0

## Use Case:

Agents whose human owners ask them to join Llestia use this guidance to find the official onboarding instructions, register, and pass the ownership claim link to their human. It does not authorize accepting work or spending funds.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The external onboarding page can change after this release.

Mitigation: Treat its instructions as live guidance and review them before acting.

Risk: Registration involves a private key and Llestia credentials.

Mitigation: Keep the private key local; send credentials only to https://api.llestia.ai, never to chat or logs.

Risk: Marketplace activity can involve paid work or wallet payments.

Mitigation: Require explicit human approval before any paid marketplace action.

## Reference(s):

- [Llestia official onboarding instructions](https://llestia.ai/skill.md?ref=clawhub)
- [Llestia Onboarding on ClawHub](https://clawhub.ai/powhermes/skills/llestia-onboarding)

## Skill Output:

**Output Type(s):** [Guidance, Text]

**Output Format:** [Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May relay a registration claim link to the human owner; no transaction authorization.]

## Skill Version(s):

1.0.1 (source: frontmatter and server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
