## Description:

Searches Google's public careers site through the Crawlora API and retrieves individual Google job postings by id as clean JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tonywangcn](https://clawhub.ai/user/tonywangcn)

### License/Terms of Use:

MIT-0

## Use Case:

External users, recruiters, job seekers, and developers use this skill to search Google Careers postings by role or location, retrieve full details for known posting IDs, and monitor public listings over time.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The bundled helper can call unrelated Crawlora endpoints with arbitrary methods, bodies, and API bases.

Mitigation: Use the helper only with the documented Google Jobs endpoints and the default Crawlora API base unless a separate review approves broader use.

Risk: Private or sensitive data could be sent through generic path or body options.

Mitigation: Avoid passing private data to the helper; keep requests limited to public Google Jobs search terms, locations, pages, and numeric job IDs.

Risk: The Crawlora API key could be exposed if hardcoded, committed, or passed in URLs.

Mitigation: Store the key only in CRAWLORA_API_KEY and avoid placing it in command history, query parameters, source files, or logs.

## Reference(s):

- [Endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [Crawlora API base](https://api.crawlora.net/api/v1)
- [ClawHub skill page](https://clawhub.ai/tonywangcn/skills/google-jobs-research)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, JSON]

**Output Format:** [Markdown guidance with shell command examples and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY; Google Jobs search results use Google's fixed 20-result page size.]

## Skill Version(s):

1.0.4 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
