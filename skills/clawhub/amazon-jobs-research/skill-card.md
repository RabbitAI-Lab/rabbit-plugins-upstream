## Description:

Researches Amazon.jobs postings through the Crawlora API, supporting public job search by keyword or category and retrieval of a single posting by job ID as normalized JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to search Amazon's public careers site, browse live job categories, and fetch full posting details through Crawlora's API.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses Crawlora as a third-party API provider and requires a Crawlora API key.

Mitigation: Use only an API key intended for this purpose, keep it in CRAWLORA_API_KEY, and do not hardcode or commit it.

Risk: Job search queries may be sent to a third-party API provider.

Mitigation: Avoid including sensitive personal information in search terms or job lookup requests.

Risk: The skill is limited to public Amazon.jobs research and may reflect changes or removals in public postings.

Mitigation: Treat results as current public job data, verify important postings before acting on them, and respect Amazon's terms.

## Reference(s):

- [Amazon Jobs endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [ClawHub skill page](https://clawhub.ai/crawlora-org/skills/amazon-jobs-research)

## Skill Output:

**Output Type(s):** [JSON, Shell commands, Guidance]

**Output Format:** [JSON responses with Markdown guidance and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY; queries public Amazon.jobs data through documented Crawlora endpoints.]

## Skill Version(s):

1.0.17 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
