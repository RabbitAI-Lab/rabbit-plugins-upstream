## Description:

基于已保存的 Amazon 商品快照、确定性 diff 和已有评论计数，按已支持的周或日周期输出单个 ASIN 的变化摘要；不承诺实时价格、销量、库存、广告、订单或真实退货率，也不自动调用付费 LLM。

This skill is ready for commercial/non-commercial use.

## Publisher:

[funewa](https://clawhub.ai/user/funewa)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to list, create, pause, resume, delete, and summarize supported Amazon ASIN watch records. It is intended for deterministic snapshot-change monitoring and watch digests, not real-time marketplace intelligence or paid AI weekly reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The release is advertised as a narrow ASIN change monitor, but the bundled ARI CLI also exposes broader paid analytics, export, and account-management commands.

Mitigation: Use the documented watch commands only, review autoconfirm settings before execution, and invoke broader paid or account-changing ARI commands only when the user intentionally requests those features.

Risk: The skill requires an ARI API key, so command execution can expose account access if the key is mishandled.

Mitigation: Keep the ARI API key private, avoid sharing command transcripts that include credentials, and use the official ARI endpoint unless a custom endpoint has been explicitly configured and approved.

Risk: Users may confuse deterministic watch digests with AI weekly reports or real-time product intelligence.

Mitigation: State that watch digest is limited to saved snapshot changes and that AI weekly reports, real-time prices, sales, inventory, ads, orders, and true return rates are outside this workflow.

## Reference(s):

- [Amazon ASIN 变化监控 专用监控参考](artifact/references/reference.md)
- [Amazon ASIN 变化监控 专用监控工作流](artifact/references/watch-workflow.md)
- [ClawHub Skill Page](https://clawhub.ai/funewa/skills/asin-change)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and deterministic watch digest summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Watch digest output is deterministic for saved product snapshots; documented digest behavior reports creditsUsed: 0, while AI weekly reports require a separate workflow and explicit confirmation.]

## Skill Version(s):

1.4.5 (source: server release evidence, skill frontmatter, and _meta.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
