## Description:

上传商品素材自动生成带货短视频，支持 AI 脚本、配音、字幕及转场，适用于 TikTok、抖音等平台。

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, commerce teams, and agents use this skill to generate short product sales videos from product images, selling points, and optional reference media. It guides setup, estimation, task submission, polling, and delivery through Qinghu qhkit.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may install or upgrade network-fetched qhkit or Node tooling persistently, including @latest upgrades and PATH or shell profile changes.

Mitigation: Confirm each npm install, Node install, PATH change, ~/.bashrc edit, and @latest upgrade before execution; prefer pinned versions or an isolated environment.

Risk: The skill requires Qinghu/qhkit access for product media uploads and API-token-based operation.

Mitigation: Use it only when Qinghu/qhkit is acceptable for the media involved, and grant the minimum necessary token access in the intended environment.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/qinghu-sales-video)
- [@iqinghu/qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [Qinghu API key dashboard](https://www.iqinghu.com/workbench/dashboard/api-keys?urlCode=1788417429126)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with inline bash commands and JSON CLI parameters]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guidance includes qhkit setup, media upload parameters, credit estimates, status polling, and final video URL delivery.]

## Skill Version(s):

0.1.1 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
