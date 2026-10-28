## Description:

将课程、直播、播客或访谈等长视频通过 gtrk 语义选段和跳剪，生成多条可在 gtrk、剪映和 Premiere Pro 中继续编辑的短片工程。

This skill is ready for commercial/non-commercial use.

## Publisher:

[gitruck](https://clawhub.ai/user/gitruck)

### License/Terms of Use:

MIT-0

## Use Case:

外部视频创作者和编辑可用此 skill 将课程、直播、播客或访谈等长视频拆成多条高光短片，并获得可继续精修的 gtrk、剪映和 Premiere Pro 工程。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Audio is uploaded to cloud services by default; split-screen processing also uploads compressed video.

Mitigation: Use only media the user is comfortable sending to the cloud, and explain the additional video upload before enabling split-screen processing.

Risk: Cloud processing may incur fees based on uploaded audio duration.

Mitigation: Review the CLI's price estimate before submission and confirm long-video jobs with the user.

Risk: The workflow uses a Gitruck API key and may invoke companion skills with separate workflows.

Mitigation: Protect the API key and assess companion skills separately before enabling their workflows.

## Reference(s):

- [Gitruck CLI](https://github.com/Gitruck/cli)
- [ClawHub skill page](https://clawhub.ai/gitruck/skills/gtrk-long2short)

## Skill Output:

**Output Type(s):** [Files, Shell commands, Configuration, Guidance]

**Output Format:** [Editable gtrk, Jianying, and Premiere Pro project files, with JSON reports and Markdown summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [One project directory with a content-dependent number of clip subprojects; available project formats can be selected.]

## Skill Version(s):

1.3.9 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
