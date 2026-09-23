## Description:

生成某家企业的公开债务画像：债务规模（转让/处置本金与利息）、关联债权人/债务人、公告时间线、保证人与抵押物。当用户问「XX 公司欠了多少钱 / 有多少债务 / 债务情况怎么样 / 帮我做个债务画像 / 风险画像」，或给出企业名称要求汇总其公开债务、公告与担保线索时使用。

This skill is ready for commercial/non-commercial use.

## Publisher:

[ninjaliang](https://clawhub.ai/user/ninjaliang)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to build a targeted public-notice debt profile for a Chinese enterprise, including disclosed debt scale, related parties, notice timeline, guarantors, collateral, and source links. It is intended for public-notice due diligence support, not credit scoring or legal conclusions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may contact agent.debtop.com and create or cache a read-only guest token under the local user account when connector credentials are unavailable.

Mitigation: Use the guest token only for agent.debtop.com, keep the local token cache private, and delete it after use when persistence is not needed.

Risk: Outputs summarize public notices and could be mistaken for credit reports, legal findings, or complete debt records.

Mitigation: Label every report as public-notice scope, include query time and sources, and avoid inferring undisclosed debt, solvency, credit ratings, or legal conclusions.

Risk: The guest path has shared rate limits and is not intended for bulk scraping or long-term archival collection.

Mitigation: Use targeted enterprise queries, keep calls serial with at least one second between tool calls, avoid bulk export, and back off on rate-limit responses.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/ninjaliang/skills/debtop-enterprise-profile)
- [Publisher profile](https://clawhub.ai/user/ninjaliang)
- [Guest access reference](references/guest-access.md)
- [Tools and fields reference](references/tools-and-fields.md)
- [Error handling reference](references/errors.md)
- [Client source IDs reference](references/client-source-ids.md)
- [Profile report template](templates/profile-report.md)
- [Debtop MCP endpoint](https://agent.debtop.com/mcp/debt/stream)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown report with linked source URLs; may include shell commands for guest-token fallback.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only public-notice summary. Reports should include data source, query time, scope disclaimer, and detail links with a client source parameter.]

## Skill Version(s):

1.0.0 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
