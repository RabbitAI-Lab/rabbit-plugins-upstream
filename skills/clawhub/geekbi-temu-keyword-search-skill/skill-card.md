## Description:

Uses GeekBI's real Temu keyword data to search and analyze Temu keywords, demand trends, supply, competition, pricing, market timing, categories, and keyword opportunities.

This skill is ready for commercial/non-commercial use.

## Publisher:

[geekbi](https://clawhub.ai/user/geekbi)

### License/Terms of Use:

MIT-0

## Use Case:

External cross-border sellers and market researchers use this skill to query Temu keywords, compare demand and supply signals, and identify hot, blue-ocean, new, or opportunity keywords for further validation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill contacts GeekBI and may send keyword, site, category, and filter parameters to the GeekBI service.

Mitigation: Install and run it only in workspaces where sending those research queries to GeekBI is approved.

Risk: The skill can reuse or create a local GeekBI login session and stores GeekBI auth state locally.

Mitigation: Avoid sharing or committing hidden .geekbi credential files, and use the documented pause and resume flow instead of exposing tokens or raw auth state.

Risk: Market conclusions can be misleading if partial pages, zero values, missing values, stale data, or narrow samples are treated as complete market evidence.

Mitigation: Require the response to state the site, filters, pagination scope, sample size, update time, and any missing or zero values before drawing conclusions.

## Reference(s):

- [Server-resolved GitHub source repository](https://github.com/geekbi/geekbi-temu-keyword-search-skill)
- [ClawHub skill page](https://clawhub.ai/geekbi/skills/geekbi-temu-keyword-search-skill)
- [Temu 关键词搜索](references/Temu关键词搜索.md)
- [Temu 关键词搜索接口](references/Temu关键词搜索接口.md)
- [Temu 关键词榜单预设](references/Temu关键词榜单预设.md)
- [查询暂停与恢复流程](references/查询暂停与恢复流程.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown text with concise conclusions, data scope, keyword tables or lists, clickable keyword links, and supporting analysis.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include site, filters, sorting, pagination scope, sample size, update time, missing-value notes, risk notes, and pause or resume prompts from GeekBI.]

## Skill Version(s):

0.1.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
