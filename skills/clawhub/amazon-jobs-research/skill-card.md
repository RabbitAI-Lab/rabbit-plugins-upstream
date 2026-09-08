## Description:

Researches Amazon.jobs postings via the Crawlora API by searching public careers listings by keyword or job category and fetching a single posting's description and qualifications as clean JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tonywangcn](https://clawhub.ai/user/tonywangcn)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to search public Amazon.jobs postings by keyword, country, category, or recency, and to fetch a single posting's description and qualifications by job id.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The helper script can send the Crawlora API key to an API base selected through CRAWLORA_API_BASE.

Mitigation: Keep CRAWLORA_API_BASE unset unless a trusted endpoint is required, and use a limited, rotatable Crawlora key.

Risk: The bundled Crawlora helper is broader than the Amazon.jobs research purpose.

Mitigation: Review or restrict helper usage to the documented /amazon-jobs/search and /amazon-jobs/job endpoints before shared or automated use.

Risk: Results cover public Amazon.jobs postings and may change as roles are updated or closed.

Mitigation: Verify job details against the current public Amazon.jobs listing before making employment, compliance, or operational decisions.

## Reference(s):

- [Amazon Jobs endpoint reference](artifact/reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [ClawHub skill page](https://clawhub.ai/tonywangcn/skills/amazon-jobs-research)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, JSON]

**Output Format:** [Markdown guidance with inline shell commands and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY; search results are paginated and limited to public Amazon.jobs data.]

## Skill Version(s):

1.0.8 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
