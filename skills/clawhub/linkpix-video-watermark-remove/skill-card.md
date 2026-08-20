## Description:

Uses the qhkit CLI package @iqinghu/qhkit to submit LinkPix video watermark-removal jobs for one to ten local files or public video URLs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill when they need an agent to remove visible watermarks, logos, or corner marks from videos through the LinkPix/Qinghu qhkit service. It helps configure the CLI, submit video-edit tasks, poll for completion, and return generated video URLs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected videos may be uploaded to the LinkPix/Qinghu service for processing.

Mitigation: Use videos the user owns or is authorized to edit, and avoid private or third-party copyrighted videos unless the privacy and legal implications are understood.

Risk: The CLI uses a configured service token and may consume service credits.

Mitigation: Confirm token configuration, report task IDs, and disclose credit estimates or actual credit usage when the service provides them.

Risk: Watermark removal can be misused for copyrighted or unauthorized media.

Mitigation: Remind users to process only owned or authorized material, especially for commercial use.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/linkpix-video-watermark-remove)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [Qinghu API keys dashboard](https://www.iqinghu.com/workbench/dashboard/api-keys)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance, Text]

**Output Format:** [Markdown with bash commands and JSON CLI arguments]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return task IDs, polling status, generated video URLs, and credit usage reported by the qhkit service.]

## Skill Version(s):

0.1.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
