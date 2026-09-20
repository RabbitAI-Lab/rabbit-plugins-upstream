## Description:

Searches and pulls postings from Meta's public careers site (metacareers.com) via the Crawlora API -- full catalog listing, filtered search by team/technology/location/employment-type, and single-posting detail -- returning clean JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, recruiters, and research agents use this skill to search Meta public job openings, enumerate the open requisition catalog, track changes over time, or retrieve a single posting by id.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends job-search requests through Crawlora, a third-party API provider.

Mitigation: Install only if third-party Crawlora API use is acceptable and review Crawlora terms before scheduled tracking.

Risk: A Crawlora API key is required for requests.

Mitigation: Keep CRAWLORA_API_KEY in the environment and do not hardcode, commit, or pass it in job-query parameters.

Risk: Job-query parameters could include private information.

Mitigation: Use only non-sensitive search terms and avoid placing private information in job-query parameters.

## Reference(s):

- [Meta Jobs endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)

## Skill Output:

**Output Type(s):** [shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands; API responses are JSON.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY; uses public Meta Careers data through Crawlora.]

## Skill Version(s):

1.0.16 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
