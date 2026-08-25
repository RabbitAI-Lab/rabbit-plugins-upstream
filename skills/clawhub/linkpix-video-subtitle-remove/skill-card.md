## Description:

Removes hard-coded subtitles from user-selected videos with qhkit video-edit and returns clean video outputs after task polling.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to remove existing subtitles or on-screen caption text from videos before reuse, translation, or secondary editing. The skill helps configure qhkit, submit subtitle-removal jobs, poll for completion, and deliver resulting video URLs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: User-selected videos are uploaded to the qhkit/iqinghu service for processing.

Mitigation: Install and use the skill only when the user is comfortable sending the selected videos to that service.

Risk: Generating subtitle-removal jobs may consume provider credits after submission.

Mitigation: Review the submitted file list and any available credit estimate with the user before approving a generate action.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/linkpix-video-subtitle-remove)
- [Publisher profile](https://clawhub.ai/user/autoagc)
- [@iqinghu/qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [iqinghu API keys page](https://www.iqinghu.com/workbench/dashboard/api-keys)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON CLI payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guides qhkit setup, pre-submit confirmation, credit disclosure, asynchronous task polling, and final video URL delivery.]

## Skill Version(s):

0.1.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
