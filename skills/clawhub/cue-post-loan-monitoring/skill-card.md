## Description:

用 Cue 执行贷后监测深度研究，跟踪授信客户的被执行、诉讼、评级下调、经营异动、股权质押和资产处置等公开风险信号，并产出带来源链接的预警底稿。

This skill is ready for commercial/non-commercial use.

## Publisher:

[wangxiaoxu](https://clawhub.ai/user/wangxiaoxu)

### License/Terms of Use:

MIT-0

## Use Case:

信贷、风控和贷后管理人员 use this skill to run Cue-based research on post-loan borrowers, prioritize risk alerts, and prepare evidence-backed monitoring notes from public data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Research queries and subject details may be sent to Cue services during execution.

Mitigation: Use the skill only for data that the user is permitted to process through Cue, and confirm that Cue service use is acceptable before running research.

Risk: The workflow can consume Cue credits and may run for several minutes.

Mitigation: Ask for explicit user approval before starting a credit-consuming run, including the selected research template and subject.

Risk: The skill depends on a Cue runner repository fetched or updated outside the artifact.

Mitigation: Confirm trust in the Cue and cue-skills sources before installation or update, and review the runner before using it in sensitive environments.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wangxiaoxu/skills/cue-post-loan-monitoring)
- [Cue playbook API](https://cuecue.cn/api/playbook)
- [cue-skills runner repository](https://github.com/sensedeal/cue-skills)
- [cue-skills runner mirror](https://gitee.com/sensedeal/cue-skills)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and source-linked research reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports should preserve source links; empty runner results should be reported without fabricating findings.]

## Skill Version(s):

1.0.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
