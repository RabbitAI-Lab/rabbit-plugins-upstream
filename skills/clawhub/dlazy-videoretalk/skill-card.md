## Description:

Video Retalk uses the dLazy CLI and hosted API to generate a lip-synced talking-person video from a source video and replacement voice audio, with an optional reference face image for multi-face videos.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, creators, and developers use this skill to run dLazy VideoRetalk lip-sync generation from a talking-person video and a new audio track. It supports selecting a target person with a reference face image when a video contains multiple faces.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing or running a third-party CLI can introduce package and execution risk.

Mitigation: Review the referenced dLazy CLI source or npm package before use, and prefer npx/on-demand execution or an isolated install in sensitive environments.

Risk: Video, audio, and image inputs may be uploaded to dLazy API and media storage endpoints for processing.

Mitigation: Only pass media files that are approved for upload to dLazy, and avoid submitting confidential or restricted content unless the service terms and organizational policy allow it.

Risk: A saved dLazy API key is a credential that could be misused if exposed.

Mitigation: Protect the local CLI configuration, use environment-scoped credentials where appropriate, and rotate or revoke the key if compromise is suspected.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-videoretalk)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, JSON, Files]

**Output Format:** [Markdown guidance with bash commands and JSON CLI responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return hosted result URLs or an async generateId; --save can download the generated asset.]

## Skill Version(s):

1.3.13 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
