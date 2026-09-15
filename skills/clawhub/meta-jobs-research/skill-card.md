## Description:

Searches and pulls postings from Meta's public careers site through the Crawlora API, supporting full catalog listing, filtered search, and single-posting detail as clean JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to search Meta job openings, enumerate public requisitions, monitor category or team changes over time, and retrieve details for a specific Meta posting.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Crawlora receives the Meta job search parameters or job IDs used with the helper.

Mitigation: Review Crawlora's service terms and avoid sending sensitive or unnecessary search context.

Risk: The Crawlora API key can be exposed if it is hardcoded, placed in query parameters, or committed.

Mitigation: Keep the key in CRAWLORA_API_KEY, rotate it if exposure is suspected, and avoid logging or committing secrets.

Risk: Scheduled tracking can consume Crawlora API credits over time.

Mitigation: Set an intentional schedule, monitor API usage, and cap the tracked query set.

## Reference(s):

- [Endpoint reference](artifact/reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [Meta Careers](https://metacareers.com)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY and returns public Meta job listing, search, or detail data from documented Crawlora endpoints.]

## Skill Version(s):

1.0.15 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
