## Description:

Retrieves public company filings and XBRL facts through the AI Skills investment-research API, then produces cited risk analysis or investment research reports without investment instructions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[youteacher](https://clawhub.ai/user/youteacher)

### License/Terms of Use:

MIT-0

## Use Case:

External users, analysts, and developers use this skill to search public filing data, retrieve company XBRL facts, and generate source-grounded risk summaries or non-advisory research reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses INVESTMENT_RESEARCH_API_KEY to call the AI Skills investment-research API.

Mitigation: Keep the key private and do not place it in JSON payloads, logs, citations, or generated reports.

Risk: AI_SKILLS_API_URL can redirect requests to a different site root if set incorrectly.

Mitigation: Use the default AI Skills host or confirm the override points to a trusted host before sending credentials.

Risk: Investment research output could be mistaken for personalized financial advice.

Mitigation: Treat reports as informational only, preserve the non-advisory disclaimer, and avoid buy, sell, hold, target-price, guaranteed-return, or trading-timing instructions.

Risk: Public filing data can be incomplete, historical, delayed, or missing for a query.

Mitigation: Preserve source, observed_at, accession, filing date, period, and unit metadata, and describe missing results as query limitations rather than facts.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/youteacher/skills/investment-research)
- [AI Skills Homepage](https://ai-skills.open-idea.net)
- [API Key Configuration](references/API-KEY.md)
- [Operations Contract](references/OPERATIONS.md)
- [HTTP Requests and Task Polling](references/HTTP-REQUESTS.md)
- [Evidence and Investment Safety Rules](references/BEHAVIOR-RULES.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON API request/response handling]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires INVESTMENT_RESEARCH_API_KEY; generated reports preserve source metadata and include a non-advisory disclaimer.]

## Skill Version(s):

1.0.0 (source: server release metadata and packageVersion)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
