## Description:

Uses qhkit video-edit remove_watermark to remove watermarks, logos, or corner marks from batches of up to 10 videos while keeping the output clear.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to configure qhkit, submit video watermark-removal jobs, poll task status, and return processed video URLs. It is intended for videos the user owns or has rights to modify.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Videos may be uploaded to a third-party service for processing.

Mitigation: Use only non-sensitive footage or footage approved for third-party processing.

Risk: The qhkit API token could be exposed if pasted into chat or logs.

Mitigation: Configure the token locally with qhkit or an environment variable, keep it secret, and rotate it if exposed.

Risk: Removing watermarks from videos without appropriate rights can create legal or policy risk.

Mitigation: Use the skill only for videos the user owns or has permission to modify.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/autoagc/skills/linkpix-video-watermark-remove)
- [qhkit npm Package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [LinkPix/qhkit API Key Dashboard](https://www.iqinghu.com/workbench/dashboard/api-keys)
- [API Key Setup Guide](https://xcnzsfe4uxrw.feishu.cn/wiki/KJ0Ywsyw8iAXmRkz5l4cddDbn6g)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline bash commands and JSON command parameters]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces qhkit installation, configuration, generate, estimate, and status commands; final media URLs are returned by the qhkit service.]

## Skill Version(s):

0.1.4 (source: evidence.release.version)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
