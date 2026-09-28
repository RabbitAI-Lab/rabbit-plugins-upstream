## Description:

Generates detailed images from text prompts and optional reference images using dLazy's hosted Seedream 5.0 Pro service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Designers, marketers, and developers use this skill to generate detailed commercial key visuals and brand assets from prompts and optional reference images.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected reference media are sent to dLazy's hosted service.

Mitigation: Only submit prompts and files you are comfortable sharing with the service.

Risk: Logging in can store a dLazy API key on the local device.

Mitigation: Protect the local configuration and rotate or revoke the key if it is exposed.

Risk: Running the skill installs or executes an external npm CLI.

Mitigation: Review the CLI before installation and prefer the pinned on-demand npx command when a global install is unnecessary.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-seedream-5-0-pro)
- [dLazy CLI homepage (skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package (skill metadata)](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration guidance, Text]

**Output Format:** [Markdown guidance and shell commands; CLI responses are JSON with generated image URLs.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated assets can be downloaded locally; asynchronous requests return a task ID.]

## Skill Version(s):

1.2.18 (source: ClawHub release metadata; embedded CLI install spec: 1.2.3)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
