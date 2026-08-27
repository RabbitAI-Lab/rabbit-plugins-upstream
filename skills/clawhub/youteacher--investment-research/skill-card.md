## Description:

Investment Research retrieves company filings and XBRL facts through the AI Skills service, then produces cited risk analysis or investment research reports without investment instructions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[youteacher](https://clawhub.ai/user/youteacher)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to query company disclosure evidence, analyze disclosed risks, and create cited research reports. It is intended for information and research workflows, not trading instructions, target prices, guarantees, or personalized investment advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The required INVESTMENT_RESEARCH_API_KEY could be exposed through logs, shared shell history, reports, or copied configuration.

Mitigation: Treat INVESTMENT_RESEARCH_API_KEY as a secret and keep it out of logs, JSON payloads, citations, reports, and shared command history.

Risk: Changing AI_SKILLS_API_URL can route requests and credentials to an untrusted endpoint.

Mitigation: Use the default AI Skills endpoint unless the exact alternate service endpoint is trusted.

Risk: Research outputs based on filings or XBRL facts can be mistaken for personalized investment advice or trading instructions.

Mitigation: Keep outputs informational, cite source task evidence, include the investment-advice disclaimer, and refuse buy, sell, hold, target-price, timing, guarantee, or return-assurance instructions.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/youteacher/skills/investment-research)
- [AI Skills Platform](https://ai-skills.open-idea.net)
- [API Key Configuration](artifact/references/API-KEY.md)
- [Operations Contract](artifact/references/OPERATIONS.md)
- [HTTP Requests and Task Polling](artifact/references/HTTP-REQUESTS.md)
- [Source, Evidence, and Investment Safety Rules](artifact/references/BEHAVIOR-RULES.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and structured API response guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires INVESTMENT_RESEARCH_API_KEY and may call the hosted AI Skills investment-research API.]

## Skill Version(s):

1.3.0 (source: server release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
