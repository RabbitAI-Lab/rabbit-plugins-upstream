## Description:

Build a requirements-based software shortlist using Crawlora product discovery, public vendor pages, and review samples.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Employees, external buyers, and procurement teams use this skill to compare software vendors against must-have requirements, pricing assumptions, integrations, public evidence, and demo questions before a buying decision.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends API requests, search terms, selected vendor or product identifiers, scrape URLs, and the Crawlora API key to Crawlora.

Mitigation: Keep highly confidential procurement details out of queries unless sharing them with Crawlora is intended, and provide the API key through the documented environment variable.

Risk: Sparse reviews, marketing pages, unknown pricing, or incomplete integration evidence can lead to overconfident vendor rankings.

Mitigation: Separate claims, review observations, and inferences; preserve source URLs and collection dates; mark unknowns as conditional and use demos or trials to resolve ranking-changing gaps.

## Reference(s):

- [Endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [Crawlora API](https://api.crawlora.net/api/v1)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown with tables, sourced findings, and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes a requirements matrix, justified shortlist, price scenarios, rejected or conditional candidates, and demo or trial checklist.]

## Skill Version(s):

1.0.7 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
