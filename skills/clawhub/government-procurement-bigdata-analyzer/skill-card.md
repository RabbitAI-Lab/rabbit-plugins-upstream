## Description:

Searches and analyzes Chinese public-procurement notices, awards, suppliers, and market trends using Zhiliaobiaoxun data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhiliaobiaoxun](https://clawhub.ai/user/zhiliaobiaoxun)

### License/Terms of Use:

MIT-0

## Use Case:

Procurement, sales, and market-research teams use this skill to find Chinese public-sector tenders and awards, identify prospective buyers, compare suppliers, and review spending and pricing trends.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Automatic registration sends the operating-system type, CPU architecture, and a hashed MAC-derived identifier to Zhiliaobiaoxun and stores an API key locally.

Mitigation: Obtain explicit consent before registration; use a preconfigured ZLBX_API_KEY to avoid it, and protect the locally stored key.

Risk: Data queries can consume account credits, and free-tier contact numbers may be masked.

Mitigation: Check available credits before extensive querying, and do not attempt to reconstruct masked contact numbers.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/zhiliaobiaoxun/skills/government-procurement-bigdata-analyzer)
- [Zhiliaobiaoxun skill documentation](https://ai.zhiliaobiaoxun.com/docs/skill)
- [Search API reference](artifact/references/api-search.md)
- [Market analysis API reference](artifact/references/api-market.md)
- [Automatic registration and privacy guidance](artifact/references/auto-register.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Analysis, Guidance]

**Output Format:** [Markdown summaries and tables with links to procurement notices]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results require API access and may include masked contact details.]

## Skill Version(s):

1.0.9 (source: frontmatter, release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
