## Description:

Searches Indeed job postings and pulls single job listings via the Crawlora API -- keyword and location search, location autocomplete, and job detail by job key -- returning clean JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tonywangcn](https://clawhub.ai/user/tonywangcn)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and recruiting researchers use this skill to search public Indeed postings, resolve valid Indeed location strings, page through search results, and fetch full job details by job key.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The bundled Crawlora helper can call arbitrary Crawlora API paths and POST arbitrary data, which is broader than the stated Indeed-only purpose.

Mitigation: Review the helper before installing and restrict use to the documented Indeed endpoints unless broader Crawlora access is intended.

Risk: Queries, arguments, and JSON bodies are sent to an external API and may include sensitive personal data if supplied by the user.

Mitigation: Avoid passing sensitive personal data, keep the Crawlora API key in CRAWLORA_API_KEY, and do not hardcode, query-parametrize, or commit the key.

## Reference(s):

- [Endpoint reference](reference/endpoints.md)
- [Crawlora API](https://api.crawlora.net/api/v1)
- [Crawlora](https://crawlora.net)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands that return JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses CRAWLORA_API_KEY and returns normalized JSON for Indeed location suggestions, job search results, and job detail lookups.]

## Skill Version(s):

1.0.4 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
