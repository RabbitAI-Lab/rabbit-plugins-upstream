## Description:

Guides agents to generate detailed vector illustrations from text prompts using dLazy's hosted Recraft V4 Pro Vector service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Designers and developers use this skill to request vector illustrations and production-oriented graphic assets from text prompts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Authentication requires a dLazy API key that may be stored locally.

Mitigation: Protect the local key and rotate or revoke it if compromised.

Risk: Prompts and any explicitly supplied local media files are sent to dLazy's hosted service.

Mitigation: Avoid submitting sensitive prompts or media unless the hosted service is appropriate for them.

Risk: Using the skill requires installing or running the pinned dLazy CLI.

Mitigation: Review the CLI and its permissions before installing or executing it.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-recraft-v4-pro-vector)
- [dLazy CLI repository](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy website](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands]

**Output Format:** [Markdown with command examples and generated asset links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The CLI can download the generated asset to a local path or return an asynchronous task ID.]

## Skill Version(s):

1.3.30 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
