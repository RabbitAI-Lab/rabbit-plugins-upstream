## Description:

Searches and pulls postings from Meta's public careers site (metacareers.com) via the Crawlora API: full catalog listing, filtered search by team, technology, location, employment type, and single-posting detail, returning clean JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tonywangcn](https://clawhub.ai/user/tonywangcn)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, recruiters, and research analysts use this skill to search Meta public job openings, monitor changes in open requisitions, and retrieve a specific posting by id.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The included helper is a general Crawlora API wrapper and can use the user's Crawlora key on endpoints beyond the documented Meta Jobs endpoints.

Mitigation: Install only if broader Crawlora API access is acceptable, or restrict the helper to /meta-jobs/list, /meta-jobs/search, and /meta-jobs/job before use.

Risk: The skill depends on a Crawlora API key stored in the runtime environment.

Mitigation: Keep the key in CRAWLORA_API_KEY only; do not hardcode it, pass it in query parameters, or commit it to source control.

## Reference(s):

- [Endpoint reference](reference/endpoints.md)
- [Crawlora API](https://api.crawlora.net/api/v1)
- [Crawlora](https://crawlora.net)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell command examples and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY and returns public Meta Careers job data through Crawlora endpoints.]

## Skill Version(s):

1.0.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
