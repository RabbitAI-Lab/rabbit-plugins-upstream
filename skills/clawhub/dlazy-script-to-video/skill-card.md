## Description:

Helps turn scripts into storyboarded, shot-by-shot videos by planning scenes, generating shots, assembling footage, and validating the result.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and production teams use this skill to turn a screenplay or scene breakdown into a multi-shot animated video with a consistent storyboard, sound, and subtitles.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and attached files are sent to dLazy's hosted service.

Mitigation: Avoid attaching private scripts or media unless you are comfortable uploading them to dLazy.

Risk: Logging in can save an API key on the local machine.

Mitigation: Use an appropriate account and protect local credentials; choose the pinned npx invocation if a global CLI installation is undesirable.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-script-to-video)
- [dLazy CLI repository (declared metadata link)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Conversational text with storyboard and video-production guidance and CLI commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Video generation is handled by the dLazy service; the skill's agent-facing output is guidance and project results.]

## Skill Version(s):

1.0.19 (source: ClawHub release metadata; artifact frontmatter says 1.0.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
