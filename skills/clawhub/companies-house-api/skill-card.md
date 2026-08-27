## Description:

Search the UK Companies House register by name, then retrieve a company's full register entry, officers, and filing history as structured JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[scavio-ai](https://clawhub.ai/user/scavio-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and analysts use this skill to look up UK companies, verify company status and identifiers, inspect officers and filings, and support KYB or due-diligence workflows using structured API responses.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses a Scavio API key and consumes credits for Companies House queries.

Mitigation: Load SCAVIO_API_KEY from a secure environment or secret store, keep it out of source control, and account for the documented credit cost before repeated or paginated calls.

Risk: Officer records can include partial dates of birth and correspondence addresses.

Mitigation: Use returned personal data only for the requested business lookup or due-diligence task, and avoid compiling profiles of private individuals beyond that purpose.

Risk: Broad company searches are capped and may not provide an exhaustive register-wide result set.

Mitigation: Narrow the query instead of paging beyond the documented search cap, and verify returned company numbers alongside company names.

## Reference(s):

- [Scavio Companies House Search Documentation](https://scavio.dev/docs/companies-house-search)
- [ClawHub Skill Page](https://clawhub.ai/scavio-ai/skills/companies-house-api)

## Skill Output:

**Output Type(s):** [Guidance, Code, Shell commands, API Calls, Configuration]

**Output Format:** [Markdown with JSON, Python, JavaScript, and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses structured JSON API responses and requires SCAVIO_API_KEY.]

## Skill Version(s):

1.0.0 (source: skill frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
