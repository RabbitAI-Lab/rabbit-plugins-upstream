## Description:

Searches and analyzes SHEIN keyword data from 极鲸云, including demand trends, supply, competition, pricing, categories, market timing, and keyword opportunities.

This skill is ready for commercial/non-commercial use.

## Publisher:

[geekbi](https://clawhub.ai/user/geekbi)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers, ecommerce analysts, and agent users use this skill to research SHEIN keywords, compare demand against supply and competition, and identify keyword opportunities for further market validation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Saved GeekBI login state may be reused across multiple GeekBI/OpenClaw skills and mirrored across local stores.

Mitigation: Install only when shared-session behavior is acceptable, and reset access with the provided clear command or by removing the auth state when isolation is required.

Risk: Keyword search results can be incomplete when pagination is unfinished or when matches exceed the accessible sorted result window.

Mitigation: Label unfinished results as samples, preserve pagination scope, and narrow filters before drawing conclusions about full-market distributions.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/geekbi/skills/geekbi-shein-keyword-search-skill)
- [Server-Resolved GitHub Provenance](https://github.com/geekbi/geekbi-shein-keyword-search-skill)
- [SHEIN Keyword Search Method](references/SHEIN关键词搜索.md)
- [SHEIN Keyword Search API](references/SHEIN关键词搜索接口.md)
- [SHEIN Keyword Ranking Presets](references/SHEIN关键词榜单预设.md)
- [Query Pause and Resume Flow](references/查询暂停与恢复流程.md)

## Skill Output:

**Output Type(s):** [analysis, markdown, shell commands, guidance]

**Output Format:** [Markdown with concise conclusions, data scope, linked keyword names, and occasional shell commands when execution is needed]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses real returned data only; marks site, filters, sort order, pagination scope, sample size, update time, missing values, and unfinished pagination when relevant.]

## Skill Version(s):

0.1.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
