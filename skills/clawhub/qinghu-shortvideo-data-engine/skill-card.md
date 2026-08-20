## Description:

青虎AI 短视频数据引擎批量处理抖音、小红书、B 站视频长链接，抓取播放、点赞、分享、收藏、评论等数据并导出 Excel，用于监测自有与竞品带货视频表现。

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External operators, marketers, and agents use this skill to batch collect short-video metrics, compare videos, quote Qinghu credit cost before submission, and deliver the resulting Excel file from a Qinghu workflow.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup path may install or upgrade a global Node package and can modify the host environment.

Mitigation: Ask for user confirmation before global npm installation or upgrade, and prefer a scoped or temporary execution environment where practical.

Risk: Qinghu credentials may be persisted in a fixed root-scoped config file.

Mitigation: Prefer managed secrets or environment variables over long-lived root config files, and avoid exposing tokens in logs or chat.

Risk: Submitting a Qinghu workflow can consume credits.

Mitigation: Run the estimate command first, report the returned credits and balance status, and wait for user confirmation before generating.

## Reference(s):

- [@iqinghu/qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [ClawHub skill page](https://clawhub.ai/autoagc/skills/qinghu-shortvideo-data-engine)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON parameter examples; completed workflows return XLSX file links.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses qhkit workflow commands, requires Qinghu credentials, quotes credits before submission, and can process up to 20 long-form video links per run.]

## Skill Version(s):

0.1.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
