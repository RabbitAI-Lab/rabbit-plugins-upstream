## Description:

Researches Amazon.jobs postings via the Crawlora API, including keyword or category search and single-posting detail retrieval by job id, returning clean JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tonywangcn](https://clawhub.ai/user/tonywangcn)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to search public Amazon.jobs postings, browse Amazon job categories, fetch full details for a specific posting, and review current openings as normalized JSON through Crawlora.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The bundled shell helper can call arbitrary Crawlora API paths and send arbitrary request bodies beyond the documented Amazon Jobs use case.

Mitigation: Use the helper only for the documented /amazon-jobs/search and /amazon-jobs/job endpoints, review commands before execution, and avoid sending secrets, personal data, or unrelated prompts through the helper.

## Reference(s):

- [Endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [ClawHub skill page](https://clawhub.ai/tonywangcn/skills/amazon-jobs-research)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [JSON responses with Markdown guidance and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY and returns paginated public Amazon.jobs data from Crawlora.]

## Skill Version(s):

1.0.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
