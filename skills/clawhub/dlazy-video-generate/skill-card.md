## Description:

Generates AI videos by selecting an appropriate dLazy CLI video model for text-to-video, image-to-video, frame-constrained video, digital-human, or lip-sync requests.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, creators, and agents use this skill to turn prompts or supplied image, video, or audio media into generated videos through the dLazy CLI and hosted API.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected local image, video, or audio files may be sent to dLazy services.

Mitigation: Confirm the intended inputs before running commands and avoid uploading private or sensitive media unless approved.

Risk: The skill invokes an external npm CLI and may create a persistent global install.

Mitigation: Install only if dLazy and the npm package are trusted; use npx or an isolated environment for one-off use.

Risk: Video generation can consume paid API credits.

Mitigation: Check the dLazy account, balance, and command parameters before execution.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-video-generate)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands; dLazy CLI executions return JSON envelopes.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires npm or npx and a dLazy API key; selected local media may be uploaded to dLazy services.]

## Skill Version(s):

1.4.14 (source: server release metadata; artifact frontmatter reports 1.4.6)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
