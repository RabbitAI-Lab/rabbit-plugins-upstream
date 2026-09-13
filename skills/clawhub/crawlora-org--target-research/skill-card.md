## Description:

Researches Target's catalog, including categories, products, filters, prices, availability, questions, and reviews, using the Crawlora API and returning normalized JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to search and browse Target catalog data, compare prices and store availability, and summarize product Q&A or reviews through Crawlora instead of scraping Target pages.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The helper includes a POST mode that can send arbitrary caller-provided data to Crawlora, although the Target workflow uses documented GET endpoints.

Mitigation: Review before installing and use only the documented Target GET examples unless POST support is removed or restricted to explicit schemas.

Risk: Search parameters or request bodies could include private notes or secrets that would be sent to the Crawlora API.

Mitigation: Do not include secrets or private data in requests; keep CRAWLORA_API_KEY scoped to Crawlora and stored only in the environment.

## Reference(s):

- [Target endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [ClawHub skill page](https://clawhub.ai/crawlora-org/skills/target-research)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell command examples and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY; API responses are paginated and may vary by store_id.]

## Skill Version(s):

1.0.14 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
