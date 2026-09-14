## Description:

Researches Amazon.jobs postings via the Crawlora API by searching Amazon's public careers site by keyword or job category and fetching full posting details by job id as clean JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, recruiters, and job researchers use this skill to search Amazon.jobs postings, browse Amazon job categories, and retrieve full public posting details by Amazon job id.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Amazon.jobs search terms, job ids, and the Crawlora API key are sent to Crawlora.

Mitigation: Use the skill only when that data sharing is acceptable, keep CRAWLORA_API_KEY in the environment, and review Crawlora's terms and privacy posture for the intended use case.

Risk: Hardcoding or committing the Crawlora API key could expose the credential.

Mitigation: Store the key only in CRAWLORA_API_KEY as documented and avoid placing it in command arguments, source files, or committed configuration.

## Reference(s):

- [Endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [Crawlora API base](https://api.crawlora.net/api/v1)
- [ClawHub skill page](https://clawhub.ai/crawlora-org/skills/amazon-jobs-research)
- [Publisher profile](https://clawhub.ai/user/crawlora-org)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, API calls, JSON]

**Output Format:** [Markdown guidance with shell commands; API responses are JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses CRAWLORA_API_KEY and the documented Crawlora Amazon Jobs endpoints; search results are paginated.]

## Skill Version(s):

1.0.15 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
