## Description:

Creates multi-shot storyboard-to-video projects with scripts, character and shot prompts, reference sheets, first and last frames, image-to-video shots, voice or TTS, music, sound effects, subtitles, and Remotion assembly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and creative developers use this skill to run dLazy's storyboard template for multi-shot animated shorts with consistent characters. The skill starts or continues project-scoped dLazy chat sessions and can attach local reference files when requested.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends prompts and options to dLazy's hosted API.

Mitigation: Review the dLazy service and avoid submitting sensitive prompts unless the service terms and data handling meet the user's requirements.

Risk: Local files are uploaded to dLazy media storage when the user passes --files.

Mitigation: Attach only files intended for upload, and inspect file paths before running commands with --files.

Risk: Authentication stores a dLazy API key in the local CLI configuration or uses DLAZY_API_KEY.

Mitigation: Use revocable organization-scoped keys, restrict local config access, and rotate or revoke keys when access is no longer needed.

Risk: The workflow depends on a pinned external npm CLI and hosted service.

Mitigation: Review the pinned package, npm listing, and source link before installation when supply-chain assurance is required.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-storyboard)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and streamed CLI responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce project-scoped guidance and command output from the hosted dLazy storyboard service.]

## Skill Version(s):

1.3.19 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
