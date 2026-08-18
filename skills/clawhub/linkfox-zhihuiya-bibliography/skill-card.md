## Description:

Queries Zhihuiya patent bibliography records by patent ID or publication number and helps an agent present patent metadata such as titles, applicants, inventors, classifications, citations, abstracts, and estimated expiry dates.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, patent researchers, and IP operations teams use this skill when they already have patent IDs or publication numbers and need factual bibliography data from Zhihuiya. It supports retrieval and presentation of structured patent metadata, not open-ended patent search, legal analysis, valuation, or freedom-to-operate assessment.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can guide credential onboarding and API-key setup.

Mitigation: Use a scoped LinkFox API key where possible, avoid sharing phone or SMS verification details unless intended, and review any shell profile changes before persisting credentials.

Risk: Billing recovery can list paid plans and create payment orders.

Mitigation: Require explicit user confirmation before selecting a plan, creating an order, or presenting payment QR codes or payment URLs.

Risk: Patent query responses and cache files may be stored locally.

Mitigation: Run the skill from an appropriate workspace, review the generated linkfox data and cache directories, and remove saved response files when they are no longer needed.

Risk: The skill may submit automatic feedback about functionality or user reactions.

Mitigation: Review feedback content before submission and avoid sending sensitive user, credential, or patent information in feedback.

Risk: Each bibliography result consumes LinkFox credits and batch requests can multiply cost.

Mitigation: Confirm the patent list and expected credit use before running batch lookups, and rely on the 24-hour cache for repeated identical requests.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-zhihuiya-bibliography)
- [Zhihuiya bibliography API reference](artifact/references/api.md)
- [Authentication and billing onboarding reference](artifact/references/onboarding.md)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON API responses, concise summaries for large responses, and saved JSON data files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Accepts patentId or patentNumber values for up to 100 patents per request; full responses are written under a linkfox session data directory, large responses are summarized in stdout, and successful or failed calls may be cached for 24 hours.]

## Skill Version(s):

1.0.8 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
