## Description:

用 Cue 跑涉外法律场景的深度研究，定向检索目标司法辖区法律法规、核查跨境主体制裁与出口管制暴露，并生成带来源链接的可回查法律研究底稿。

This skill is ready for commercial/non-commercial use.

## Publisher:

[wangxiaoxu](https://clawhub.ai/user/wangxiaoxu)

### License/Terms of Use:

MIT-0

## Use Case:

External legal, compliance, investment, and business teams use this skill to request cross-border legal research, sanctions and export-control screening, comparative-law analysis, and cited regulatory risk checks for public-data workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses the user’s Cue account, API key, and credits to run external legal research.

Mitigation: Confirm the selected research buddy and credit spend before execution, and use an account appropriate for the data being researched.

Risk: Legal and compliance outputs may be incomplete, outdated, or unsuitable as final advice.

Mitigation: Treat the report as research support, review the cited sources, and have qualified legal or compliance professionals validate conclusions before acting.

Risk: The workflow can install or update an external Cue runner before execution.

Mitigation: Review the Cue runner source and installation path before use in environments with strict security or compliance controls.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wangxiaoxu/skills/cue-cross-border-legal)
- [Publisher profile](https://clawhub.ai/user/wangxiaoxu)
- [Cue playbook API](https://cuecue.cn/api/playbook)
- [Cue skills runner on GitHub](https://github.com/sensedeal/cue-skills)
- [Cue skills runner on Gitee](https://gitee.com/sensedeal/cue-skills)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown research report with source links and inline shell commands for setup and execution]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a Cue account API key and explicit confirmation before spending credits; outputs are research support, not legal advice.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
