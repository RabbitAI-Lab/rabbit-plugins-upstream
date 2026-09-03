## Description:

Resolve a ticker to a CIK, then pull SEC EDGAR filer profiles, filings, XBRL financial concepts and full-text search across 2001-today.

This skill is ready for commercial/non-commercial use.

## Publisher:

[scavio-ai](https://clawhub.ai/user/scavio-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, and agents use this skill to resolve SEC company identifiers, retrieve filer profiles and filings, inspect XBRL financial facts, and search filing text for investment research or filing-monitoring workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires a third-party Scavio API key and can consume paid credits after the free allowance.

Mitigation: Store SCAVIO_API_KEY in an environment or secret store, monitor credit usage, and confirm billing expectations before broad deployment.

Risk: Financial data returned from filings can be misread or used without sufficient verification.

Mitigation: Verify material figures against the source SEC filing before relying on them for analysis or decisions.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/scavio-ai/skills/sec-edgar-api)
- [Scavio SEC EDGAR Documentation](https://scavio.dev/docs/sec-edgar-lookup)
- [Scavio Rate Limits](https://scavio.dev/docs/rate-limits)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Code, API calls, JSON]

**Output Format:** [Markdown guidance with shell and code blocks plus structured JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SCAVIO_API_KEY; endpoints use Scavio credits and return public SEC EDGAR data.]

## Skill Version(s):

1.0.1 (source: server release evidence; artifact frontmatter is 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
