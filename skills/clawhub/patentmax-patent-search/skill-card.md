## Description:

PatentMax helps agents search, inspect, compare, and analyze global patents and company patent portfolios through the iprdb patent-data API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ip930](https://clawhub.ai/user/ip930)

### License/Terms of Use:

MIT

## Use Case:

External users, developers, and patent analysts use this skill to run patent searches, review individual patent records, find similar patents, analyze citations, inspect legal-status data, and summarize company or technology-area patent portfolios. The skill is a search and analysis aid, not a source of legal opinions on patentability, infringement, validity, freedom to operate, or licensing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: An untrusted PatentMax base URL could receive the API key and sensitive patent-search queries.

Mitigation: Use the default PatentMax endpoint and do not set PATENTMAX_BASE_URL unless the endpoint is fully trusted.

Risk: Live patent searches can expose unpublished inventions, formulas, source code, or trade secrets to the PatentMax service.

Mitigation: Use a dedicated low-balance or test key where possible and avoid submitting confidential technical material unless the user accepts that disclosure.

Risk: Patent search results can be mistaken for legal conclusions about patentability, infringement, invalidity, or freedom to operate.

Mitigation: Present search scope, sources, dates, and uncertainty clearly, and direct legal conclusions to qualified review and official patent-office records.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/ip930/skills/patentmax-patent-search)
- [PatentMax API Platform](https://api.ip930.com/features/api-platform)
- [README](README.md)
- [Install Guide](INSTALL.md)
- [API Reference](references/api-reference.md)
- [Search Workflow](references/search-workflow.md)
- [Query Syntax](references/query-syntax.md)
- [FAQ](references/faq.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a PatentMax API key; live searches and analysis calls may incur per-call charges.]

## Skill Version(s):

1.3.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
