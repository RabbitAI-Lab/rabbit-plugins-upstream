## Description:

Converts storyboard details into a canvas-ready video-generation pipeline.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and creative agents use this skill to read storyboard fields, compute video dimensions, define a per-scene audio and video generation pipeline, and add that pipeline to a canvas.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses persistent dLazy API credentials and may store them in local CLI configuration.

Mitigation: Use a scoped API key where possible, rotate or revoke it when no longer needed, and prefer per-run environment variables for sensitive sessions.

Risk: Prompts and local media paths provided to the CLI may be uploaded to dLazy services.

Mitigation: Avoid sensitive prompts or media unless upload is intended, and review inputs before running generation commands.

Risk: The skill relies on a global or npx-installed npm CLI and terminal generation commands.

Mitigation: Review the package before installation, pin the intended CLI version, and run one confirmed command at a time.

Risk: The skill can add generated audio, image, and video pipeline elements to a canvas.

Mitigation: Review the proposed pipeline JSON and canvas changes before applying them.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/dlazyai/skills/dlazy-video-storyboard-generate)
- [dLazy CLI Homepage](https://github.com/dlazyai/cli)
- [dLazy CLI npm Package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy Homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with JSON pipeline snippets and CLI commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires npm or npx and dLazy API credentials; may generate canvas elements and hosted media URLs through the dLazy CLI.]

## Skill Version(s):

1.2.5 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
