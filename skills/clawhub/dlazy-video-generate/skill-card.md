## Description:

Video generation skill that helps an agent select and run an appropriate dLazy CLI video model for text-to-video, image-to-video, first/last-frame video, reference-driven video, digital human, and lip-sync workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and creative operators use this skill to generate, animate, edit, or lip-sync videos through dLazy cloud video models from natural-language prompts and optional image, video, or audio inputs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected image, video, or audio files are sent to dLazy cloud services for processing.

Mitigation: Avoid sending confidential or restricted media unless organizational policy permits use of dLazy as a cloud processor.

Risk: The dLazy API key may be saved in the local CLI configuration.

Mitigation: Use per-invocation DLAZY_API_KEY where appropriate, and revoke or rotate saved keys when access should change.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-video-generate)
- [dLazy homepage](https://dlazy.com)
- [dLazy CLI source](https://github.com/dlazyai/cli)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, Guidance, JSON, URLs]

**Output Format:** [Markdown guidance with shell commands and JSON command output from the dLazy CLI]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill selects a dLazy video subcommand, checks its help output, and returns hosted generation result URLs or CLI error information.]

## Skill Version(s):

1.4.8 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
