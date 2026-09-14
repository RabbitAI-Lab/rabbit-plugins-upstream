## Description:

一键去除视频水印，保持视频画质清晰，适用于素材整理及二次创作。

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External users and creators use this skill to remove visible watermarks, logos, or corner marks from one or more videos through the qhkit video-edit remove_watermark workflow. Users should apply it only to video content they own or are authorized to edit.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow may upload local videos to the external Qinghu/qhkit service.

Mitigation: Use it only for videos the user owns or is authorized to edit, and confirm that external upload is acceptable before processing sensitive media.

Risk: The skill directs agents to install or upgrade a mutable global npm CLI.

Mitigation: Prefer a pinned, local, isolated qhkit install and review the package before execution, especially in environments that contain unrelated secrets.

Risk: The qhkit workflow requires an API token or configured credentials.

Mitigation: Use a narrowly scoped token, avoid exposing it in shared logs or shell history, and run the workflow in an environment with only the required credentials.

Risk: Removing watermarks from third-party copyrighted video can create infringement risk.

Mitigation: Process only self-owned or properly licensed footage, and warn users when the requested use appears unauthorized.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/qinghu-video-watermark-remove)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON command parameters]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return task IDs, polling status, output video URLs, and credit usage from qhkit responses.]

## Skill Version(s):

0.1.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
