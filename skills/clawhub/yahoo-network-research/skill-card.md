## Description:

Research Yahoo editorial stories, shopping features, and sports data through Crawlora and return structured results.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Researchers and developers use this skill to retrieve Yahoo story feeds, full articles, news comments, shopping deals, and sports scores or standings for summaries and analysis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: User-selected queries and URLs are sent to the third-party Crawlora API.

Mitigation: Do not submit private or sensitive URLs, search strings, or identifiers.

Risk: Exposing the Crawlora API key could allow unauthorized use.

Mitigation: Keep CRAWLORA_API_KEY in the environment and do not commit it to files.

## Reference(s):

- [Yahoo Network Research on ClawHub](https://clawhub.ai/crawlora-org/skills/yahoo-network-research)
- [Endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)

## Skill Output:

**Output Type(s):** [Text, JSON]

**Output Format:** [Markdown summaries or normalized JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results depend on the availability of public Yahoo content and Crawlora API access.]

## Skill Version(s):

1.0.16 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
