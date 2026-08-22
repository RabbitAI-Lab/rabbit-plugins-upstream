## Description:

Provides Amazon SP-API Customer Feedback lookups through LinkFox for item and browse-node review topics, review trends, return topics, return trends, and item browse-node discovery.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Amazon sellers, marketplace operators, and analysts use this skill to retrieve customer feedback topics and trends for ASINs and browse nodes. It helps compare review and return signals such as mentions and star-rating impact across supported marketplaces.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill mediates Amazon feedback calls through LinkFox services.

Mitigation: Use it only when the user accepts LinkFox-mediated access, and verify seller, region, marketplace, ASIN, and browse-node inputs before each call.

Risk: Full API responses may be stored locally in plaintext under LinkFox session output folders.

Mitigation: Review saved files for sensitive business data and remove them when they are no longer needed.

Risk: The artifact includes onboarding flows for SMS login, API-key retrieval, payment ordering, and billing status.

Mitigation: Prefer creating or retrieving API keys directly from the provider site and avoid sharing SMS codes through an agent unless necessary.

Risk: LINKFOX_* base URL overrides can redirect requests away from the default LinkFox endpoints.

Mitigation: Check environment variables before use and reject overrides that point to untrusted hosts.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-amazon-store-customer-feedback)
- [Artifact API reference](references/api.md)
- [Artifact onboarding reference](references/onboarding.md)
- [Amazon Customer Feedback API guide](https://developer-docs.amazon.com/sp-api/docs/customer-feedback-api-v2024-06-01-use-case-guide)
- [getItemReviewTopics](https://developer-docs.amazon.com/sp-api/reference/getitemreviewtopics)
- [getItemBrowseNode](https://developer-docs.amazon.com/sp-api/reference/getitembrowsenode)
- [getBrowseNodeReturnTrends](https://developer-docs.amazon.com/sp-api/reference/getbrowsenodereturntrends)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance, JSON files]

**Output Format:** [Markdown guidance, shell commands, and JSON response summaries or files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Full API responses are saved under a LinkFox session directory; large responses print a summary unless inline output is requested.]

## Skill Version(s):

1.0.7 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
