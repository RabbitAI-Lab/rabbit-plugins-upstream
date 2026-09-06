## Description:

Converts storyboard details into a video-generation pipeline that can be added to a canvas.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and creative workflow users use this skill to read storyboard context, compute video dimensions, assemble audio, image, and video generation nodes, and draw the resulting pipeline onto a canvas.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may install or run the dLazy CLI and ask the agent to execute generation commands.

Mitigation: Review the CLI package and use a controlled workspace before installation or command execution.

Risk: Prompts and referenced image, video, or audio files may be uploaded to dLazy services.

Mitigation: Use only media and prompt content that is approved for upload to third-party services.

Risk: The dLazy API key may be stored in a local CLI configuration file or passed through an environment variable.

Mitigation: Use a scoped key where possible, protect the local configuration file, and rotate or revoke the key when access is no longer needed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-video-storyboard-generate)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Guidance, JSON, Shell commands, Configuration]

**Output Format:** [Markdown guidance with JSON pipeline content and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce canvas pipeline JSON and command-line instructions for the dLazy CLI.]

## Skill Version(s):

1.2.10 (source: server release metadata; artifact frontmatter lists 1.2.3)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
