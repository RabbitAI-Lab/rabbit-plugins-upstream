## Description:

Searches Google's public careers site (careers.google.com) via the Crawlora API and pulls single job postings by id, returning clean JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, recruiters, researchers, and agents use this skill to search public Google Careers postings by role and location, retrieve details for a numeric Google job id, or monitor public postings over time.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Job queries, requested locations, posting IDs, and the Crawlora API key are sent to Crawlora.

Mitigation: Use a dedicated Crawlora API key, keep it in CRAWLORA_API_KEY, do not hardcode or commit it, and only send data intended for the documented Google Jobs API workflow.

Risk: Requests outside the documented Google Jobs endpoints could expose unrelated account or API surfaces.

Mitigation: Run the bundled helper only for /google-jobs/search and /google-jobs/job as documented by the endpoint reference.

## Reference(s):

- [Endpoint reference](reference/endpoints.md)
- [ClawHub skill page](https://clawhub.ai/crawlora-org/skills/google-jobs-research)
- [Crawlora](https://crawlora.net)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, JSON, Guidance]

**Output Format:** [Markdown guidance with shell commands and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses CRAWLORA_API_KEY from the environment and limits helper calls to the documented Google Jobs endpoints.]

## Skill Version(s):

1.0.15 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
