## Description:

Text-to-image generation with Jimeng, quickly converting text prompts into image outputs through the dLazy CLI and hosted API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to ask an agent to generate Jimeng images from prompts, optionally with reference images, through the dLazy CLI. It is suited for creative image generation workflows where users can provide prompts and manage dLazy account credentials and usage costs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill relies on a third-party npm CLI and hosted dLazy/Jimeng service.

Mitigation: Install only when that service is intended, prefer explicit invocation or npx in sensitive environments, and review the package or source before deployment.

Risk: Prompts and selected local media files are sent to dLazy endpoints for generation.

Mitigation: Avoid submitting confidential prompts or media unless that data sharing is approved for the environment.

Risk: Image generation may consume dLazy account credits.

Mitigation: Use dry-run or account controls where appropriate, and make users aware of insufficient-balance errors before retrying.

Risk: The dLazy API key is required for use.

Mitigation: Store the key with the CLI auth flow or protected environment variables, rotate it when needed, and avoid exposing it in logs or prompts.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-jimeng-t2i)
- [dLazy CLI homepage](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy website](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, JSON, Files, Guidance]

**Output Format:** [Markdown guidance with bash examples; runtime CLI responses are JSON containing image URLs, async task IDs, or saved image files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a dLazy API key. Prompts and selected media are sent to dLazy endpoints, and usage may incur account costs.]

## Skill Version(s):

1.3.15 (source: server release metadata; artifact frontmatter declares 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
