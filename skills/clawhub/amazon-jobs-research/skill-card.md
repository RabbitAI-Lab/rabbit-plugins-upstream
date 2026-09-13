## Description:

Researches Amazon.jobs postings via the Crawlora API by searching Amazon's public careers site by keyword or job category, then fetching a single posting's full description and qualifications by job id as clean JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and recruiting researchers use this skill to search public Amazon.jobs postings, browse Amazon job categories, sort recent postings, and retrieve full details for a specific Amazon job id.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Authenticated requests may consume Crawlora credits or make unintended calls if an agent follows untrusted instructions.

Mitigation: Use the documented Amazon Jobs routes only, keep CRAWLORA_API_KEY in the environment, and review requested paths and parameters before execution.

Risk: The server security verdict is suspicious because authenticated POST requests outside the documented job-search API scope were identified as a concern.

Mitigation: Prefer GET searches and job detail calls for /amazon-jobs/search and /amazon-jobs/job; reject or review any request body or POST use before running the helper.

Risk: Public job posting data can change or disappear as roles are edited or closed.

Mitigation: Treat returned posting data as time-sensitive and re-fetch job details before relying on availability, descriptions, or qualifications.

## Reference(s):

- [Endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [Crawlora API base](https://api.crawlora.net/api/v1)
- [ClawHub skill page](https://clawhub.ai/crawlora-org/skills/amazon-jobs-research)
- [Publisher profile](https://clawhub.ai/user/crawlora-org)

## Skill Output:

**Output Type(s):** [API Calls, Shell commands, JSON, Guidance]

**Output Format:** [JSON responses with Markdown usage guidance and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY; searches and detail lookups return public Amazon.jobs posting data.]

## Skill Version(s):

1.0.14 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
