## Description:

基于已保存的 Amazon 商品快照、确定性 Diff 和已有评论计数，按已支持的周或日周期输出单个 ASIN 变化摘要。

This skill is ready for commercial/non-commercial use.

## Publisher:

[funewa](https://clawhub.ai/user/funewa)

### License/Terms of Use:

MIT-0

## Use Case:

External users and operators use this skill to manage Amazon ASIN snapshot watches and read deterministic daily or weekly change digests for a single ASIN. It is suited to product field and review-count change monitoring, not real-time price, inventory, sales, advertising, order, or return-rate analysis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The package is described as a narrow ASIN watch monitor but includes a broader ARI CLI surface with paid AI, export, credential, and account-mutation workflows.

Mitigation: Install only after reviewing the broader CLI capabilities and deciding whether this package should receive ARI account access beyond watch digest commands.

Risk: ARI API keys could be exposed if requests are redirected to an untrusted custom API host.

Mitigation: Use the default ARI service unless a custom base URL is intentional; the release evidence notes that custom ARI_BASE_URL use requires ARI_ALLOW_CUSTOM_BASE=1.

Risk: Paid AI weekly report workflows are separate from the deterministic watch digest flow.

Mitigation: Keep watch digest usage separate from AI weekly reports and require an explicit quote and confirmation before any paid AI operation.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/funewa/skills/asin-change)
- [Publisher Profile](https://clawhub.ai/user/funewa)
- [Amazon ASIN 变化监控 专用监控参考](references/reference.md)
- [Amazon ASIN 变化监控 专用监控工作流](references/watch-workflow.md)
- [ARI service](https://ari.funewa.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with CLI commands and deterministic watch digest output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an ARI API key. Watch digest is described by the skill as zero-credit deterministic output; paid AI weekly reports are outside this workflow and require separate confirmation.]

## Skill Version(s):

1.4.3 (source: server release evidence, skill frontmatter, _meta.json, script VERSION)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
