## Description:

Helps analyze procurement notices, winning bids, companies, competitors, and market opportunities using natural-language queries.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhiliaobiaoxun](https://clawhub.ai/user/zhiliaobiaoxun)

### License/Terms of Use:

MIT-0

## Use Case:

Procurement teams, suppliers, and market analysts use this skill to search Chinese tender and award notices, assess potential opportunities, and summarize company and market activity.

### Deployment Geography for Use:

Global (focused on Chinese procurement data)

## Known Risks and Mitigations:

Risk: Procurement queries are sent to Zhiliaobiaoxun's cloud service.

Mitigation: Use only if sharing those queries with the service is acceptable.

Risk: Automatic account registration collects platform, architecture, and a MAC-derived hash and stores an API key locally.

Mitigation: Prefer setting ZLBX_API_KEY through normal secret management; if using automatic registration, confirm the device-feature collection prompt first and protect the stored key.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/zhiliaobiaoxun/skills/ai-tender-bid-analyst)
- [Skill documentation](https://ai.zhiliaobiaoxun.com/docs/skill)
- [Search API reference](references/api-search.md)
- [Market analysis API reference](references/api-market.md)
- [Account registration reference](references/auto-register.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown summaries and tables with source links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include tender statistics, company comparisons, and opportunity assessments.]

## Skill Version(s):

1.0.7 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
