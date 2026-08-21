## Description:

上传商品素材自动生成电商带货短视频，支持 AI 脚本、配音、字幕及转场，适用于 TikTok、抖音等平台。

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, sellers, and ecommerce operators use this skill to turn product images and a short selling point into short promotional videos with generated script, voiceover, subtitles, and transitions. Agents can also use it to estimate credits, confirm paid generation parameters, submit qhkit video tasks, poll status, and return generated video URLs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Video generation consumes credits and submitted tasks cannot be canceled.

Mitigation: Before generation, list the selected model or template, duration, aspect ratio, language, referenced assets, and estimated credits, then wait for explicit user approval.

Risk: The skill depends on qhkit configuration, media uploads, and an API token.

Mitigation: Install qhkit only when the user intends to use LinkPix generation, validate the masked configuration with qhkit config show, and avoid exposing token values in responses.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/autoagc/skills/linkpix-sales-video)
- [@iqinghu/qhkit npm Package](https://www.npmjs.com/package/@iqinghu/qhkit)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON parameters]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include qhkit command parameters, credit estimates, task IDs, status updates, generated video URLs, and user confirmation prompts before paid generation.]

## Skill Version(s):

0.1.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
