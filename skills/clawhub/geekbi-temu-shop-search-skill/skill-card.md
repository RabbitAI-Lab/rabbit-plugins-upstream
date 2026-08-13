## Description:

Searches and analyzes Temu shops using GeekBI real-time data, with filters for shop name or ID, site, trusted category ID, hosting mode, sales, revenue, ratings, reviews, product count, followers, price, opening date, growth, sell-through metrics, and ranking use cases.

This skill is ready for commercial/non-commercial use.

## Publisher:

[geekbi](https://clawhub.ai/user/geekbi)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers, marketplace researchers, and commerce analysts use this skill to find Temu shops, compare competitor shops, study top or new shops, and assess shop-level scale, growth, sell-through efficiency, reputation, and operating mode. The skill is focused on shop-level research and does not provide item-level details.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: GeekBI login state is persisted and can be reused across GeekBI Temu skills, which broadens access beyond this shop-search workflow.

Mitigation: Use the skill only in trusted workspaces, prefer a virtual environment or dedicated workspace, and clear GeekBI auth state when shared session reuse is no longer desired.

## Reference(s):

- [Server-resolved source repository](https://github.com/geekbi/geekbi-temu-shop-search-skill)
- [ClawHub skill page](https://clawhub.ai/geekbi/skills/geekbi-temu-shop-search-skill)
- [Temu 店铺搜索](references/Temu店铺搜索.md)
- [Temu 店铺搜索接口](references/Temu店铺搜索接口.md)
- [Temu 店铺榜单查询预设](references/Temu店铺榜单预设.md)
- [查询暂停与恢复流程](references/查询暂停与恢复流程.md)

## Skill Output:

**Output Type(s):** [Markdown, Shell commands, Guidance, Analysis]

**Output Format:** [Chinese Markdown with shop links, data-scope notes, concise business conclusions, and occasional shell commands for local GeekBI queries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results should distinguish returned data from analysis, include sample and pagination limits, and avoid exposing tokens, raw headers, raw error JSON, or internal request details unless needed for troubleshooting.]

## Skill Version(s):

0.1.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
