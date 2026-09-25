## Description:

生成某家企业的公开公告口径债务画像，覆盖债务规模、关联债权人与债务人、公告时间线、保证人与抵押物，并由智收云MCP提供数据与服务。

This skill is ready for commercial/non-commercial use.

## Publisher:

[ninjaliang](https://clawhub.ai/user/ninjaliang)

### License/Terms of Use:

MIT-0

## Use Case:

External users, analysts, and agents use this skill to build a public-notice debt profile for a named enterprise, including debt scale, related creditors and debtors, notice timelines, guarantors, collateral, and source links.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The fallback path can send enterprise queries and guest-auth metadata to agent.debtop.com and cache a short-lived guest token plus persistent device ID locally.

Mitigation: Use the skill only for expected public enterprise debt lookup, keep requests on the documented agent.debtop.com domain, and protect or clear ~/.cache/debtop according to local credential-handling policy.

Risk: Bulk scraping or repeated high-volume queries can exceed shared guest-access limits and misuse the public-notice service.

Mitigation: Keep calls serial, respect the documented 1 QPS posture and daily limits, and avoid using the skill for bulk export or long-term archival collection.

Risk: Public debt notices can be mistaken for a complete credit report or a creditworthiness determination.

Mitigation: Present outputs as public-announcement evidence only, include source links and query time, and avoid unsupported legal, causal, repayment-capacity, or credit-rating conclusions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/ninjaliang/skills/debtop-enterprise-profile)
- [Guest access reference](references/guest-access.md)
- [Tool parameters and return fields](references/tools-and-fields.md)
- [Error handling reference](references/errors.md)
- [Client source identifiers](references/client-source-ids.md)
- [Profile report template](templates/profile-report.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown profile report with source links; may include shell command snippets for guest-access setup or troubleshooting.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only public-notice debt analysis; cited enterprise and notice links should include a stable client source marker.]

## Skill Version(s):

1.0.1 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
