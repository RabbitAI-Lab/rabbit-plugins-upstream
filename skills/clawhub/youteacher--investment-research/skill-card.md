## Description:

Helps users retrieve company filings or XBRL facts and generate cited, non-prescriptive risk analysis or investment research reports from platform-sourced evidence.

This skill is ready for commercial/non-commercial use.

## Publisher:

[youteacher](https://clawhub.ai/user/youteacher)

### License/Terms of Use:

MIT-0

## Use Case:

Analysts, researchers, and developers use this skill to query company disclosure data through the AI Skills platform, then create cited risk summaries or investment research reports that avoid buy, sell, hold, price-target, timing, or guaranteed-return instructions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires an API key and can be pointed at an alternate AI_SKILLS_API_URL.

Mitigation: Keep INVESTMENT_RESEARCH_API_KEY private and use only a trusted AI Skills endpoint.

Risk: Research reports could be mistaken for personalized investment advice or trading instructions.

Mitigation: Treat outputs as informational research only; do not use them for automated trading, order execution, guaranteed returns, or buy, sell, hold, price-target, or timing instructions.

Risk: Disclosure data may be incomplete, delayed, partial, or limited to the specific query results.

Mitigation: Use only succeeded or evidence-backed partial source tasks, preserve citations and timestamps, and explain missing or partial evidence instead of inferring that a fact does not exist.

## Reference(s):

- [AI Skills Platform](https://ai-skills.open-idea.net)
- [API Key Configuration](https://ai-skills.open-idea.net/skill-docs/investment-research/API-KEY.md)
- [Operations Contract](https://ai-skills.open-idea.net/skill-docs/investment-research/OPERATIONS.md)
- [HTTP Requests and Task Polling](https://ai-skills.open-idea.net/skill-docs/investment-research/HTTP-REQUESTS.md)
- [Sources, Evidence, and Investment Safety Rules](https://ai-skills.open-idea.net/skill-docs/investment-research/BEHAVIOR-RULES.md)
- [ClawHub Skill Page](https://clawhub.ai/youteacher/skills/investment-research)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands, JSON request examples, cited risk analysis, and research report text.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires INVESTMENT_RESEARCH_API_KEY; outputs are informational and source-backed, not investment advice or trading instructions.]

## Skill Version(s):

1.5.2 (source: server release metadata and skill metadata.packageVersion)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
