## Description:

使用极鲸云按明确的 Temu 商品 ID 查询真实评论，并分析评分结构、卖点、痛点、规格差异、近期反馈和产品改良方向。

This skill is ready for commercial/non-commercial use.

## Publisher:

[geekbi](https://clawhub.ai/user/geekbi)

### License/Terms of Use:

MIT-0

## Use Case:

External users and commercial operators use this skill to inspect a specific Temu product's returned review data, summarize customer sentiment, and turn evidence-backed feedback into sourcing, quality-control, listing, and product-improvement actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill contacts GeekBI services and depends on a local GeekBI login token for Temu review searches.

Mitigation: Install and run it only when service access and local token reuse are intended, and avoid exposing tokens, request headers, device codes, callback credentials, or auth state files in prompts, logs, examples, or command-line arguments.

Risk: Authentication state may be mirrored into user config, the skill directory, and the current working directory under .geekbi/agent-auth.json.

Mitigation: Keep those paths private, do not copy or share the auth files manually, and remove stale local auth state when the workspace is no longer trusted.

Risk: Review analysis can be misleading if empty, partial, filtered, or paginated data is treated as complete market evidence.

Mitigation: Report data boundaries, filters, page coverage, deduplicated totals, and sample limitations, and do not infer missing comments or media content beyond what GeekBI returns.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/geekbi/skills/geekbi-temu-review-search-skill)
- [Server-resolved GitHub provenance](https://github.com/geekbi/geekbi-temu-review-search-skill)
- [Temu 评论搜索](references/Temu评论搜索.md)
- [Temu 评论搜索接口](references/Temu评论搜索接口.md)
- [查询暂停与恢复流程](references/查询暂停与恢复流程.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Chinese Markdown with concise summaries, evidence scope, tables or bullet lists when useful, and JSON from helper scripts during execution.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs should identify the product ID, filters, pagination scope, deduplicated totals, sample limitations, and whether conclusions are based on full or partial returned review data.]

## Skill Version(s):

0.1.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
