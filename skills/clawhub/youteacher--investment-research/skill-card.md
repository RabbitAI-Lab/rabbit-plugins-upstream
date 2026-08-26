## Description:

Investment Research helps agents query public filing and XBRL fact evidence, then produce cited risk analysis or investment research reports without investment instructions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[youteacher](https://clawhub.ai/user/youteacher)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to retrieve company filings or XBRL facts from the AI Skills platform and create cited, informational research outputs. It is intended for evidence-based risk summaries and reports, not trading decisions or personalized investment advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Company identifiers, filing filters, and query parameters are sent to the AI Skills platform.

Mitigation: Confirm the platform is trusted for the intended company research workflow before installation or use.

Risk: The skill requires an API key that could expose account access if shared in chats, logs, code, or reports.

Mitigation: Store INVESTMENT_RESEARCH_API_KEY in environment configuration and do not echo or persist the full key.

Risk: Generated research could be mistaken for personalized investment advice or a trading recommendation.

Mitigation: Treat outputs as informational, keep the required non-advisory disclaimer, and refuse buy, sell, hold, target-price, guaranteed-return, or automated-trading requests.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/youteacher/skills/investment-research)
- [AI Skills Homepage](https://ai-skills.open-idea.net)
- [API Key Configuration](references/API-KEY.md)
- [Operations Contract](references/OPERATIONS.md)
- [HTTP Requests and Task Polling](references/HTTP-REQUESTS.md)
- [Evidence and Investment Safety Rules](references/BEHAVIOR-RULES.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with JSON and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires INVESTMENT_RESEARCH_API_KEY; outputs must preserve source, timestamp, accession, filing date, period, and unit when available.]

## Skill Version(s):

1.2.0 (source: server release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
