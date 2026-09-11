## Description:

Searches and pulls postings from Meta's public careers site (metacareers.com) via the Crawlora API for catalog listing, filtered search, and single-posting detail as clean JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

External users, recruiters, analysts, and developers use this skill to search Meta public job openings, enumerate the open requisition catalog, track new postings, or retrieve one posting by job id.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Search requests are sent to Crawlora as a third-party service.

Mitigation: Use the skill only when sharing Meta job-search context with Crawlora is acceptable, and review requests before sending sensitive context.

Risk: The Crawlora API key could be exposed if it is hardcoded, committed, or passed in unsafe ways.

Mitigation: Store CRAWLORA_API_KEY only as an environment variable and use the provided helper, which keeps the key out of command-line arguments.

Risk: Results cover public Meta Careers postings and may not represent internal, expired, or non-public roles.

Mitigation: Treat returned postings as public-site data and verify important hiring decisions against Meta Careers or another authoritative source.

## Reference(s):

- [Meta Jobs endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [Skill page](https://clawhub.ai/crawlora-org/skills/meta-jobs-research)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with shell commands; API responses are JSON.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses the CRAWLORA_API_KEY environment variable and returns public Meta Careers posting data through scoped Crawlora endpoints.]

## Skill Version(s):

1.0.14 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
