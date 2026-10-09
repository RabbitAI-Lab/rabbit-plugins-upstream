## Description:

Turns an idea into a reviewable video-production plan covering story, characters, scenes, shots, images, and video assembly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and production teams use this skill to turn an idea into a structured, user-reviewed plan for generating visual assets and assembling a video.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The canvas plan and later terminal-generation instructions conflict, leaving execution authority unclear.

Mitigation: Clarify the intended workflow with the publisher and require explicit user approval before running commands or starting generation.

Risk: Installing or running the dLazy CLI and storing an API key locally may expose credentials or execute unreviewed commands.

Mitigation: Review CLI installation and generation commands before execution; use a per-run DLAZY_API_KEY when persistent storage is not desired.

Risk: Prompts and supplied media are sent to dLazy services, and generation consumes remote resources.

Mitigation: Obtain approval for external uploads and resource use; avoid submitting sensitive material without authorization.

## Reference(s):

- [dLazy CLI source and usage reference](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Configuration instructions, Media links]

**Output Format:** [Markdown plans, canvas workflow guidance, command snippets, and generated media URLs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Video generation and media delivery depend on dLazy services and user confirmation.]

## Skill Version(s):

1.3.29 (source: ClawHub release metadata; artifact frontmatter states 1.3.9)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
