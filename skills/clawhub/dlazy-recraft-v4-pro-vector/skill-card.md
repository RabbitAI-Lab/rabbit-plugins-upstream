## Description:

Generates high-fidelity vector illustrations and SVG assets from text prompts using Recraft V4 Pro Vector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Designers and developers use this skill to generate vector illustrations and SVG assets from text prompts through dLazy's hosted service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and files explicitly supplied to the dLazy CLI may be sent to its hosted service.

Mitigation: Review prompts and selected files for sensitive content before submitting them.

Risk: Installing the external npm CLI and logging in can persist software and an API key locally.

Mitigation: Review the pinned CLI before installation; use npx and a per-invocation DLAZY_API_KEY if less persistent setup is preferred.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-recraft-v4-pro-vector)
- [dLazy CLI repository (skill metadata link)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Markdown with bash commands and JSON result examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated assets are returned by URL or optionally saved locally; asynchronous runs return a generation ID.]

## Skill Version(s):

1.3.31 (source: server release metadata; artifact frontmatter says 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
