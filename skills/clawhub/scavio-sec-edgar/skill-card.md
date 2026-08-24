## Description:

Resolve a ticker to a CIK, then pull SEC EDGAR filer profiles, filings, XBRL financial concepts and full-text search across 2001-today. 6 endpoints, 1 credit each, structured JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[scavio-ai](https://clawhub.ai/user/scavio-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, and agent builders use this skill to query Scavio's SEC EDGAR API for CIK lookup, filer profiles, filings, XBRL facts and concepts, and filing full-text search. It supports investment research, fundamentals datasets, filing monitoring, and regulatory document analysis workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: SEC research queries and identifiers are sent to Scavio and authenticated with SCAVIO_API_KEY.

Mitigation: Keep the API key in an environment variable or secret store and avoid sending sensitive internal research terms unless that use is approved.

Risk: Each endpoint call consumes Scavio credits.

Mitigation: Plan lookup, pagination, and history requests before execution, and monitor the returned credits_used and credits_remaining fields.

Risk: Financial facts, filing results, and search matches can be misread or overgeneralized.

Mitigation: Use the skill's guardrails: resolve CIKs first, discover exact XBRL tags with facts before concept calls, cite the filing behind reported numbers, and avoid presenting public regulatory data as investment advice.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/scavio-ai/skills/scavio-sec-edgar)
- [Scavio SEC EDGAR documentation](https://scavio.dev/docs/sec-edgar-lookup)
- [Scavio rate limits](https://scavio.dev/docs/rate-limits)

## Skill Output:

**Output Type(s):** [Guidance, Code, Shell commands, Configuration, API Calls, JSON]

**Output Format:** [Markdown guidance with inline shell commands, Python and JavaScript examples, API request shapes, and JSON response descriptions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses SCAVIO_API_KEY for authenticated Scavio API calls; responses are structured JSON envelopes with data, timing, credits used, and credits remaining.]

## Skill Version(s):

1.0.3 (source: server release metadata; artifact frontmatter reports 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
