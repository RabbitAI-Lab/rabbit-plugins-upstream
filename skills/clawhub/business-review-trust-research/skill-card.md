## Description:

Researches product launches, business reputation, software reviews, startup revenue, and crowdfunding campaigns using public data returned by the Crawlora API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Researchers and buyers use this skill to compare software products, assess public business reviews and complaints, and check startup or crowdfunding activity before making decisions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Research inputs such as company names, URLs, locations, or campaign identifiers are sent to Crawlora.

Mitigation: Use only public, necessary research terms; do not submit secrets or private personal data.

Risk: An exposed API key or broad directory browsing could enable unintended access or excessive requests.

Mitigation: Keep CRAWLORA_API_KEY in the environment and limit pagination and directory searches to legitimate, targeted research.

## Reference(s):

- [Skill endpoint reference](artifact/reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [ClawHub skill listing](https://clawhub.ai/crawlora-org/skills/business-review-trust-research)

## Skill Output:

**Output Type(s):** [Text, JSON]

**Output Format:** [Research summaries with structured JSON source results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Paginated public-data results may require multiple requests.]

## Skill Version(s):

1.0.19 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
