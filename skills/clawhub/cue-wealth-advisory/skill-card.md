## Description:

用 Cue 跑「财富投顾」场景的深度研究：自动汇总隔夜政策与外盘动态，生成即插即用的客户早报与配置建议。

This skill is ready for commercial/non-commercial use.

## Publisher:

[wangxiaoxu](https://clawhub.ai/user/wangxiaoxu)

### License/Terms of Use:

MIT-0

## Use Case:

Wealth advisors, financial content teams, and investment-advisory agents use this skill to run Cue research workflows that prepare market briefings, allocation commentary, client talking points, cross-border tax compliance guidance, and bond-risk monitoring summaries.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow may clone or update third-party runner code in the user's home directory.

Mitigation: Review the runner source and pin or approve the runner version before use in controlled financial environments.

Risk: The workflow uses a local Cue API key, contacts Cue services, and can consume Cue credits.

Mitigation: Run only after explicit user confirmation, use appropriate account controls, and keep the API key out of shared logs or transcripts.

Risk: Generated wealth-advisory content may be used in client-facing financial workflows.

Mitigation: Preserve cited sources and require professional compliance, suitability, and due-diligence review before relying on outputs with clients.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wangxiaoxu/skills/cue-wealth-advisory)
- [Cue playbook API](https://cuecue.cn/api/playbook)
- [Cue skills runner repository](https://github.com/sensedeal/cue-skills)
- [Cue skills runner mirror](https://gitee.com/sensedeal/cue-skills)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown reports and concise agent guidance with inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports should preserve source links and should not fabricate results when the Cue runner returns empty output.]

## Skill Version(s):

1.0.1 (source: evidence.release.version)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
