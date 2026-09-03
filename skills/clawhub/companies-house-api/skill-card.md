## Description:

Search the UK Companies House register by name, then pull a company's full register entry, its officers, and its filing history as structured JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[scavio-ai](https://clawhub.ai/user/scavio-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, and compliance teams use this skill to search UK company records, inspect company status and filings, and support KYB or due-diligence checks with structured registry data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill depends on Scavio as a third-party API provider for Companies House data and requires an API key.

Mitigation: Install only if the third-party provider is acceptable, store SCAVIO_API_KEY in an environment variable or secret store, and monitor credit usage.

Risk: Officer records can include personal details such as correspondence address and partial date of birth.

Mitigation: Use officer data only for the user's specific due-diligence need and avoid compiling broader profiles of private individuals.

Risk: Broad company searches are capped and paginated results can be misread as exhaustive.

Mitigation: Narrow broad search terms, respect the page-50 search cap, and verify page-one results before reporting that officers or filings are absent.

Risk: Registry identifiers, officer names, dates, and filing codes could be misreported if the agent fills gaps from assumptions.

Mitigation: Return only data received from the API and include the company number alongside the company name for user verification.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/scavio-ai/skills/companies-house-api)
- [Scavio Companies House API documentation](https://scavio.dev/docs/companies-house-search)
- [Scavio rate limits](https://scavio.dev/docs/rate-limits)

## Skill Output:

**Output Type(s):** [Guidance, Code, Shell commands, Configuration, JSON]

**Output Format:** [Markdown guidance with inline shell commands, code examples, and structured JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SCAVIO_API_KEY; API responses include Companies House data returned through Scavio.]

## Skill Version(s):

1.0.2 (source: server release evidence; artifact frontmatter says 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
