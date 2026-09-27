## Description:

Creates multi-shot animated storyboard and video projects with scripts, character and shot prompts, reference sheets, first and last frames, i2v shot videos, voice/TTS, music, sound effects, subtitles, and Remotion assembly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, developers, and agents use this skill to start or continue dLazy storyboard projects for multi-shot animated shorts with consistent characters.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts are sent to the third-party dLazy hosted API.

Mitigation: Review prompts for sensitive content before use and confirm that dLazy's hosted service is acceptable for the workflow.

Risk: Files explicitly attached with the CLI may be uploaded to dLazy media storage.

Mitigation: Attach only files intended for upload, and avoid confidential media unless approved for the service.

Risk: The dLazy API key is stored locally by the CLI.

Mitigation: Protect the local CLI config, use OS account permissions, and rotate or revoke the organization API key when needed.

Risk: Running the pinned third-party npm CLI may execute code outside NVIDIA control.

Mitigation: Review the pinned npm package or source repository before installation, especially for sensitive environments.

Risk: Hosted generation can consume dLazy credits.

Mitigation: Check credit availability before longer runs and handle insufficient-balance errors by directing users to the dLazy credits dashboard.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-storyboard)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)
- [dLazy API key dashboard](https://dlazy.com/dashboard/organization/api-key)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and streamed CLI/service responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May reference generated storyboard or video assets returned by dLazy; local files are uploaded only when explicitly attached.]

## Skill Version(s):

1.3.20 (source: server release evidence; artifact frontmatter reports 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
