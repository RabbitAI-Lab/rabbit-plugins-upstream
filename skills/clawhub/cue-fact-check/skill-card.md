## Description:

用 Cue 穿透待核查资讯的表层表述，通过独立信源交叉验证与底层数据复核，精准识别时间错位、数据偏差及误导性信息，产出包含原文对照与纠偏证据的结构化事实核查报告。

This skill is ready for commercial/non-commercial use.

## Publisher:

[panting09266-ai](https://clawhub.ai/user/panting09266-ai)

### License/Terms of Use:

MIT-0

## Use Case:

面向需要核实新闻、研报、尽调资料或市场传言的用户，逐条比对原文与独立信源，形成带纠偏证据和来源链接的事实核查报告。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: 技能会自动更新并运行外部代码，该代码可能访问已保存的 Cue API Key。

Mitigation: 使用经过审查且固定到提交版本的 runner；更新前明确审批，并使用专用 Cue Key、限制 runner 的文件访问范围。

Risk: 提交给 Cue 的材料以及可分享的报告可能包含不适合公开的信息。

Mitigation: 只提交允许发送给 Cue 的材料；分享前检查报告链接的访问权限，并留意积分消耗。

## Reference(s):

- [Cue 平台](https://cuecue.cn)
- [Cue API Key 管理](https://cuecue.cn/api-key?src=clawhub-fact-check)
- [ClawHub 技能发布页](https://clawhub.ai/panting09266-ai/skills/cue-fact-check)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, Guidance]

**Output Format:** [结构化 Markdown 核查报告，包含待核查原文、逐条结论、纠偏证据、独立信源对照、偏差分析和来源链接]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [核查结论标注属实、偏差或无法核实；来源和报告链接取自实际运行结果。]

## Skill Version(s):

1.0.11 (source: server release metadata; artifact frontmatter reports 1.1.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
