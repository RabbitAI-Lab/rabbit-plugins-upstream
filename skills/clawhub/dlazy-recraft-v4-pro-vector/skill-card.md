## Description:

Generates high-fidelity vector artwork from text prompts using the Recraft V4 Pro Vector model for production-grade SVG assets and detailed illustrations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and design teams use this skill to generate vector artwork from prompts through the dLazy CLI and hosted API.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and referenced media paths may be sent to dLazy's hosted service.

Mitigation: Avoid submitting confidential prompts or media unless the user accepts dLazy's service handling for that data.

Risk: Authentication stores a dLazy API key locally when using login or auth set.

Mitigation: Use least-privilege API keys when available, rotate or revoke keys from the dLazy dashboard, and protect the local CLI config file.

Risk: The skill installs and runs the third-party @dlazy/cli package through npm or npx.

Mitigation: Review or trust the package before installation and prefer npx or an isolated environment when a global CLI is not desired.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-recraft-v4-pro-vector)
- [dLazy CLI homepage](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy website](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, JSON, Files, Guidance]

**Output Format:** [JSON response with generated output URLs; optional downloaded asset file when --save is used]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a dLazy API key; prompts and referenced media files may be sent to dLazy API and media storage endpoints.]

## Skill Version(s):

1.3.16 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
