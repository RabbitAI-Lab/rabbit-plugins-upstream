## Description:

Guides agents to generate text and code through the dLazy Claude Sonnet 5 service, with optional image and video inputs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other agents use this skill to request text, reasoning, and code from dLazy's hosted Claude Sonnet 5 service, optionally supplying images or videos.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing a third-party CLI executes software outside the skill itself.

Mitigation: Review and trust the @dlazy/cli package before installing or running it.

Risk: Prompts and supplied media files are sent to dLazy services.

Mitigation: Avoid including sensitive prompts or local files unless you intend to send them to dLazy.

Risk: A stored or exposed API key can grant access to the user's dLazy organization.

Mitigation: Use an organization-scoped key that can be rotated or revoked, and protect the local configuration.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-claude-sonnet-5)
- [dLazy CLI project (declared in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Text, Code, Guidance]

**Output Format:** [JSON-wrapped generated content]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Asynchronous requests can return a task ID for later polling.]

## Skill Version(s):

1.2.28 (source: server release metadata; bundled skill frontmatter says 1.2.7)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
