## Description:

Search the UK Companies House register by name, then pull a company's full register entry, its officers, and its filing history as structured JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[scavio-ai](https://clawhub.ai/user/scavio-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and compliance teams use this skill to search UK companies, retrieve company profiles, review officers, and inspect filing history for KYB, due diligence, and business-data workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Queries and the Scavio API key are sent to Scavio.

Mitigation: Use a scoped Scavio API key, store it outside source control, and send only the business lookup data needed for the task.

Risk: Each endpoint consumes Scavio credits.

Mitigation: Plan calls before broad searches, narrow company-name queries when possible, and stop pagination on the documented empty-page signal.

Risk: Officer records may include public personal details.

Mitigation: Use officer data only for the requested company-check purpose and avoid compiling unnecessary profiles of private individuals.

## Reference(s):

- [Scavio Companies House Search Documentation](https://scavio.dev/docs/companies-house-search)
- [Scavio Rate Limits](https://scavio.dev/docs/rate-limits)
- [ClawHub Skill Page](https://clawhub.ai/scavio-ai/skills/scavio-companies-house)

## Skill Output:

**Output Type(s):** [guidance, code, shell commands, configuration, API calls, JSON]

**Output Format:** [Markdown guidance with code examples and structured JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SCAVIO_API_KEY; each endpoint consumes one Scavio credit.]

## Skill Version(s):

1.0.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
