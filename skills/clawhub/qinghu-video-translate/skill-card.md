## Description:

Automatically recognizes speech in videos and translates it into multiple languages, with options for AI dubbing, subtitles, and lip-sync localization.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, localization teams, and agents use this skill to submit video translation jobs through qhkit, monitor status, and deliver translated video outputs with subtitles, dubbing, or lip sync.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may install or upgrade unpinned global qhkit tooling.

Mitigation: Require explicit user approval before installation or upgrade, and prefer a reviewed or isolated environment for the CLI.

Risk: The skill may configure an API token for the third-party service.

Mitigation: Use a scoped token where available, avoid exposing it in logs, and remove or rotate it when access is no longer needed.

Risk: Selected local videos may be uploaded to a third-party service for processing.

Mitigation: Confirm the upload with the user first and avoid confidential, regulated, or otherwise sensitive media unless the transfer is acceptable.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/qinghu-video-translate)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [Qinghu API key dashboard](https://www.iqinghu.com/workbench/dashboard/api-keys)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with shell commands and JSON CLI parameters]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guides qhkit video translation generation, status polling, installation, upgrade, token configuration, and delivery of returned media URLs.]

## Skill Version(s):

0.1.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
