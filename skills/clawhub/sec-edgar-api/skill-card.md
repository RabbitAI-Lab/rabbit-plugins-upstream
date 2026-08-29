## Description:

Resolve a ticker to a CIK, then pull SEC EDGAR filer profiles, filings, XBRL financial concepts and full-text search across 2001-today.

This skill is ready for commercial/non-commercial use.

## Publisher:

[scavio-ai](https://clawhub.ai/user/scavio-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, and agents use this skill to resolve SEC tickers and company names to CIKs, retrieve filer profiles and filings, inspect XBRL concepts, and search EDGAR filing text for investment research or filing-monitoring workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: SEC query details and the Scavio API key are sent to Scavio's hosted API.

Mitigation: Keep SCAVIO_API_KEY in environment variables or a secret store, and avoid placing keys in prompts, source files, or shared logs.

Risk: Returned public filing data may be over-interpreted as investment advice.

Mitigation: Treat responses as research input, cite the underlying filing behind reported numbers, and do not present figures as recommendations.

Risk: Guessed CIKs, accession numbers, filing dates, or XBRL tags can produce wrong or empty results.

Mitigation: Resolve identifiers with the lookup endpoint, discover XBRL tags with the facts endpoint, and report which filing supplied any quoted value.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/scavio-ai/skills/sec-edgar-api)
- [Scavio SEC EDGAR lookup documentation](https://scavio.dev/docs/sec-edgar-lookup)
- [Scavio rate limits](https://scavio.dev/docs/rate-limits)

## Skill Output:

**Output Type(s):** [Guidance, API Calls, Code, Shell commands, Configuration instructions]

**Output Format:** [Markdown guidance with JSON API request patterns and Python or JavaScript code examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses SCAVIO_API_KEY and describes structured JSON responses from Scavio SEC EDGAR endpoints.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
