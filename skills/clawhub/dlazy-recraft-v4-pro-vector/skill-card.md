## Description:

Helps agents generate detailed vector artwork from text prompts through the dLazy-hosted Recraft V4 Pro Vector service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Designers, developers, and other agents use this skill to request vector-style illustrations and production assets from text prompts, then retrieve the generated result.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A third-party CLI stores a dLazy API key locally.

Mitigation: Review the CLI before installation and protect or rotate the key; use the pinned on-demand npx invocation if a persistent global binary is not wanted.

Risk: Prompts and any media files explicitly provided for generation are sent to dLazy's hosted service.

Mitigation: Avoid submitting confidential prompts or sensitive media unless authorized to share them with dLazy.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-recraft-v4-pro-vector)
- [dLazy CLI source (skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Text, Files]

**Output Format:** [Command guidance and JSON results with a generated asset URL; optional downloaded asset]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results may complete asynchronously; output URLs are hosted by dLazy.]

## Skill Version(s):

1.3.26 (source: server-resolved ClawHub release; artifact frontmatter says 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
