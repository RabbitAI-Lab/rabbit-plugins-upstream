## Description:

Searches Google's public careers site (careers.google.com) via the Crawlora API and pulls single job postings by id, returning clean JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to search Google Careers postings by role or location, retrieve a single posting by numeric job id, and track public postings over time.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Job search queries and the Crawlora API key are sent to Crawlora.

Mitigation: Use a dedicated Crawlora key and avoid placing sensitive personal data in search terms.

Risk: Results are based on public careers.google.com postings that can change or close over time.

Mitigation: Refresh important postings by numeric job id and treat returned job data as time-sensitive.

## Reference(s):

- [Google Jobs Endpoint Reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [ClawHub Skill Page](https://clawhub.ai/crawlora-org/skills/google-jobs-research)

## Skill Output:

**Output Type(s):** [JSON, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY; helper supports only documented GET routes for Google Jobs search and single-posting lookup.]

## Skill Version(s):

1.0.16 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
