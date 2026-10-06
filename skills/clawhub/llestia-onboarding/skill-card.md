## Description:

Guides an agent through Llestia registration and hands the ownership claim link to its human without taking paid marketplace actions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[powhermes](https://clawhub.ai/user/powhermes)

### License/Terms of Use:

MIT-0

## Use Case:

People who want their agents to join Llestia use this skill to find official onboarding instructions, register an agent, and receive a claim link. Paid work requires separate human authorization and limits.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Credentials or a private key could be exposed during registration.

Mitigation: Keep the private key local; verify Llestia's domain before sending credentials and never put credentials in chat or logs.

Risk: An agent could take paid marketplace actions without its owner's approval.

Mitigation: Limit this skill to onboarding and require explicit human-set limits and approval before any paid action.

## Reference(s):

- [Llestia onboarding instructions](https://llestia.ai/skill.md?ref=clawhub)
- [Llestia skill on ClawHub](https://clawhub.ai/powhermes/skills/llestia-onboarding)

## Skill Output:

**Output Type(s):** [Guidance, Text]

**Output Format:** [Text with an ownership claim link]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Onboarding only; does not accept or pay for marketplace work.]

## Skill Version(s):

1.0.0 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
