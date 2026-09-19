## Description:

Generates multi-shot storyboard-based animated videos with scripts, consistent characters, shot prompts, reference sheets, first/last frames, image-to-video shots, voice/TTS, music, SFX, subtitles, and Remotion assembly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, developers, and agent users use this skill to invoke the dLazy storyboard template for multi-shot animated shorts with consistent characters and generated media assets.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and attached files may be sent to the dLazy hosted service.

Mitigation: Avoid uploading sensitive files or confidential prompts unless the user intends to share them with dLazy.

Risk: Authentication stores a local dLazy API key.

Mitigation: Use the documented dLazy login or auth flow, keep the local config protected, and rotate or revoke the key from the dLazy dashboard when needed.

Risk: The skill depends on an external npm-distributed CLI and hosted API endpoints.

Mitigation: Review the pinned CLI package and repository before installation, and install only when use of the dLazy service is acceptable.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-storyboard)
- [dLazy CLI repository](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown and terminal text with inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May reference project ids and uploaded file URLs returned by the dLazy service.]

## Skill Version(s):

1.3.17 (source: server release metadata; artifact frontmatter reports 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
