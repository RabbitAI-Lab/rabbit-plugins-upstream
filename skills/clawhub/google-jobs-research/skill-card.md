## Description:

Searches Google's public careers site (careers.google.com) via the Crawlora API and pulls single job postings by id, returning clean JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to search Google Careers postings by role and location, retrieve full job details by numeric job id, and track postings over time through Crawlora.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends the Crawlora API key and job-search queries, including roles, locations, and job IDs, to Crawlora.

Mitigation: Use only when sharing that data with Crawlora is acceptable, keep the key in CRAWLORA_API_KEY, and avoid putting secrets or personal notes into query parameters.

## Reference(s):

- [Endpoint Reference](reference/endpoints.md)
- [ClawHub Skill Page](https://clawhub.ai/crawlora-org/skills/google-jobs-research)
- [Crawlora](https://crawlora.net)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY and returns public Google Careers posting data via Crawlora.]

## Skill Version(s):

1.0.14 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
