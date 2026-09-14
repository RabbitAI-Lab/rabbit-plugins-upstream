## Description:

This skill helps agents invoke dLazy's Seedance 2.5 video-generation CLI for ByteDance's model, supporting prompts, multimodal references, first/last-frame control, durations up to 30 seconds, and resolutions up to 4K.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to generate videos through the dLazy hosted Seedance 2.5 service from agent workflows, including prompt-based generation, multimodal references, and first/last-frame control.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill relies on a third-party npm CLI and hosted dLazy service that receive prompts, selected media files, and API credentials.

Mitigation: Use the pinned or on-demand CLI path from the artifact, review the package before use, and avoid submitting sensitive or restricted content.

Risk: The dLazy API key may be stored in local CLI configuration or supplied through an environment variable.

Mitigation: Keep local configuration access limited to the user account and rotate or revoke the API key if it may have been exposed.

Risk: Local image, video, or audio paths passed to generation options can be uploaded to dLazy media storage.

Mitigation: Confirm that referenced files are intended for cloud processing before running the command.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-seedance-2-5)
- [Publisher profile](https://clawhub.ai/user/dlazyai)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON CLI responses containing generated media URLs or async task status.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The workflow requires a dLazy API key and may upload prompts and selected image, video, or audio files to dLazy service endpoints.]

## Skill Version(s):

1.2.12 (source: server release metadata; artifact frontmatter declares CLI package version 1.2.3)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
