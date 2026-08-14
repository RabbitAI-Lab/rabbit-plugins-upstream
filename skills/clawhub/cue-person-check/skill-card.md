## Description:

用 Cue 跑「人物核查」场景的深度研究：穿透人物的全生命周期工商与司法轨迹，映射其商业控制版图。覆盖个人背调底稿、基金经理言行核查、企业管理层风险体检、实控人关联穿透、关键人物批量核查等核心搭子，批量核验失信、限高、被执行、行政处罚、股权冻结等公开风险，逐人定级排序，产出合作或准入前可用的背调底稿。

This skill is ready for commercial/non-commercial use.

## Publisher:

[wangxiaoxu](https://clawhub.ai/user/wangxiaoxu)

### License/Terms of Use:

MIT-0

## Use Case:

External users and due-diligence analysts use this skill to run Cue person-check research for public-record background checks, management risk reviews, beneficial-owner association tracing, and batch screening of key people before cooperation or admission decisions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may install or update a third-party Cue runner before use.

Mitigation: Review the runner source and install it only from the documented Cue repositories before executing research commands.

Risk: The workflow reads a local Cue API key and sends queried person or organization details to Cue.

Mitigation: Use an appropriate Cue account, avoid submitting unnecessary sensitive details, and confirm the query is suitable for public-record due diligence.

Risk: Deep research consumes Cue credits and important conclusions may be incomplete or incorrect.

Mitigation: Require explicit credit confirmation before running and independently verify material findings against the report's cited sources.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wangxiaoxu/skills/cue-person-check)
- [Cue playbook API](https://cuecue.cn/api/playbook)
- [Cue runner GitHub repository](https://github.com/sensedeal/cue-skills)
- [Cue runner Gitee mirror](https://gitee.com/sensedeal/cue-skills)

## Skill Output:

**Output Type(s):** [guidance, shell commands, markdown, configuration]

**Output Format:** [Markdown report with source links and inline shell commands for running Cue research]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Research runs can consume Cue credits, require a Cue API key, and may take several minutes before a final sourced report is available.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
