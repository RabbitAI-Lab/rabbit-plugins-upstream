## Description:

Search the UK Companies House register by name, then pull a company's full register entry, its officers, and its filing history as structured JSON. 4 endpoints, 1 credit each.

This skill is ready for commercial/non-commercial use.

## Publisher:

[scavio-ai](https://clawhub.ai/user/scavio-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, compliance teams, and agent builders use this skill to search UK Companies House records, retrieve company profiles, list current and resigned officers, and inspect filing history for KYB, due diligence, and B2B data workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Companies House search terms and company numbers are sent to Scavio.

Mitigation: Use the skill only for authorized lookups and avoid submitting unnecessary confidential context with search requests.

Risk: Officer records can include public but sensitive personal information such as correspondence addresses and month-and-year birth dates.

Mitigation: Return only the officer fields needed for the user's task and avoid compiling profiles of private individuals beyond the requested Companies House lookup.

Risk: The skill requires a Scavio API key and each endpoint call consumes credits.

Mitigation: Store SCAVIO_API_KEY in the environment, do not expose it in prompts or logs, and page through results deliberately to control credit usage.

Risk: Broad name searches are capped at page 50 and cannot prove exhaustive coverage of every matching company.

Mitigation: Narrow broad queries and describe search results as the returned Scavio/Companies House matches rather than a guaranteed exhaustive list.

## Reference(s):

- [Scavio Companies House documentation](https://scavio.dev/docs/companies-house-search)
- [Scavio rate limits](https://scavio.dev/docs/rate-limits)
- [ClawHub skill page](https://clawhub.ai/scavio-ai/skills/scavio-companies-house)

## Skill Output:

**Output Type(s):** [guidance, code, shell commands, configuration, JSON]

**Output Format:** [Markdown with bash, Python, and JavaScript examples plus JSON response descriptions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SCAVIO_API_KEY and describes Scavio API calls that return structured JSON.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
