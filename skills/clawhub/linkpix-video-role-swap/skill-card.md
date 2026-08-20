## Description:

通过 qhkit CLI（npm @iqinghu/qhkit）上传原视频及新角色图，一键替换原视频中的人物角色，动作口型保持不变。

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agent operators use this skill to run LinkPix video role replacement workflows with qhkit, supplying an original video, one replacement character image, and the original video duration. It is intended for authorized likeness replacement, video face or character swapping, digital-human replacement, and localized model videos.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected videos and images are uploaded to the Qinghu/LinkPix service.

Mitigation: Use the skill only with media that may be shared with that third-party service, and avoid uploading sensitive or unauthorized content.

Risk: The workflow uses a qhkit API token and may consume account credits.

Mitigation: Configure tokens through qhkit or QHKIT_TOKEN, keep credentials out of prompts and logs, check estimates where available, and report credit or balance issues clearly to the user.

Risk: Video role replacement can modify real faces or likenesses.

Mitigation: Confirm the user is authorized to modify the depicted person or likeness, and refuse unauthorized face or likeness replacement requests.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/linkpix-video-role-swap)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [Qinghu API keys](https://www.iqinghu.com/workbench/dashboard/api-keys)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON command parameters]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include qhkit task IDs, polling guidance, generated video URLs, credit usage notes, and user-facing CLI error messages.]

## Skill Version(s):

0.1.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
