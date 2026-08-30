## Description:

Lead Intelligence helps users search companies or contacts with compliance-oriented filters, score leads from submitted observable signals, and generate local lead research reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[youteacher](https://clawhub.ai/user/youteacher)

### License/Terms of Use:

MIT-0

## Use Case:

Sales, growth, and operations users use this skill to find companies or contacts under bounded filters, score submitted leads using deterministic observable criteria, and create concise local lead reports. It requires a Lead Intelligence API key before use.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The API key and submitted lead data are sensitive.

Mitigation: Store the API key only in the OpenClaw environment setting, avoid pasting it into chat or logs, and confirm trust in ai-skills.open-idea.net before submitting company, domain, title, or lead data.

Risk: The skill handles company and people search data and could be misused for contact enrichment or outreach workflows.

Mitigation: Do not submit passwords, cookies, sessions, regulated personal data, or CRM and outreach actions unless separately authorized; do not infer email addresses or phone numbers from availability indicators.

Risk: Repeated POST requests may create inconsistent task or billing behavior if idempotency is ignored.

Mitigation: Use a unique Idempotency-Key for each new logical POST request and reuse the same key and JSON body only for retries of that same request.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/youteacher/skills/lead-intelligence)
- [AI Skills homepage](https://ai-skills.open-idea.net)
- [API Key configuration](https://ai-skills.open-idea.net/skill-docs/lead-intelligence/API-KEY.md)
- [Operations contract](https://ai-skills.open-idea.net/skill-docs/lead-intelligence/OPERATIONS.md)
- [HTTP requests and task queries](https://ai-skills.open-idea.net/skill-docs/lead-intelligence/HTTP-REQUESTS.md)
- [Privacy, scoring, and error rules](https://ai-skills.open-idea.net/skill-docs/lead-intelligence/BEHAVIOR-RULES.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, API calls, JSON, Markdown]

**Output Format:** [Markdown guidance with shell commands, HTTP request examples, JSON responses, deterministic scores, and local report summaries.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Company and people searches return structured result records and pagination; lead scoring returns points, scores, and reasons; report creation returns aggregate lead-report fields.]

## Skill Version(s):

1.2.1 (source: release evidence and package metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
