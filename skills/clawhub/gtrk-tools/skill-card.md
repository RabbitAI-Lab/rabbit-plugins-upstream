## Description:

Guides an agent in choosing and running gtrk image, video, and audio tools, then explaining their outputs and costs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[gitruck](https://clawhub.ai/user/gitruck)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to select gtrk single-purpose media tools and have an agent run them with clear guidance about inputs, outputs, and charges.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Some operations upload media, voice references, or local project paths to Gitruck Cloud.

Mitigation: Explain upload requirements and check the task's price before submission; protect API credentials.

Risk: Cloud operations may incur charges, and resubmitting after a timeout can duplicate work and billing.

Mitigation: Check the price before running a task and recover timed-out work using its task ID before submitting again.

Risk: Voice cloning can use a person's voice reference.

Mitigation: Obtain the speaker's permission before starting a voice-cloning task.

## Reference(s):

- [gtrk CLI 使用教程](https://hocassian.feishu.cn/wiki/HCFpwoF7SivIFbkKosgcFMcEnxk)
- [Gitruck CLI project](https://github.com/Gitruck/cli)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance, Media files, JSON results]

**Output Format:** [Markdown guidance and CLI commands; tool-dependent media files and structured JSON results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated files and result details vary by selected tool and input.]

## Skill Version(s):

1.3.9 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
