## Description:

Resolve a ticker to a CIK, then pull SEC EDGAR filer profiles, filings, XBRL financial concepts and full-text search across 2001-today. 6 endpoints, 1 credit each, structured JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[scavio-ai](https://clawhub.ai/user/scavio-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, and agent builders use this skill to resolve SEC filer identities, retrieve EDGAR filing metadata, inspect XBRL facts and concepts, and run full-text filing searches for research or filing-monitoring workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: SEC filing queries are sent to Scavio and each endpoint call consumes credits.

Mitigation: Confirm the integration and credit model are acceptable before installing or using the skill.

Risk: The skill requires SCAVIO_API_KEY.

Mitigation: Store the API key as a credential and avoid exposing it in prompts, logs, or generated files.

Risk: EDGAR data can support financial research but does not provide investment recommendations.

Mitigation: Treat returned filing data as public regulatory information and avoid presenting results as investment advice.

## Reference(s):

- [Scavio SEC EDGAR Lookup Documentation](https://scavio.dev/docs/sec-edgar-lookup)
- [Scavio Rate Limits](https://scavio.dev/docs/rate-limits)

## Skill Output:

**Output Type(s):** [Guidance, Code, Shell commands, Configuration, API calls, JSON]

**Output Format:** [Markdown guidance with bash, Python, and JavaScript examples; API responses use structured JSON.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SCAVIO_API_KEY and uses one Scavio credit per endpoint call.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
