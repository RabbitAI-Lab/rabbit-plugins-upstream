## Description:

Searches LinkFox/Ruiguan for similar US utility or invention patents from product details and reports similarity, validity, and TRO-risk indicators for pre-listing patent risk review.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Cross-border e-commerce sellers and their agents use this skill to run preliminary US utility/invention patent similarity checks before listing products. It helps them prioritize active patents and TRO indicators for human review without treating the result as legal advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Product descriptions and patent-search inputs are sent to LinkFox/Ruiguan services.

Mitigation: Avoid confidential unreleased product details unless the user has reviewed the service terms and approved external processing.

Risk: The skill can use or generate a LinkFox API key, and onboarding may print credentials into logs or transcripts.

Mitigation: Treat API keys as secrets, avoid sharing transcripts that contain keys, and rotate any exposed key.

Risk: Patent checks consume paid LinkFox credits and billing flows can create payment orders.

Mitigation: Confirm user intent before repeated searches, broad result requests, or purchase/order steps.

Risk: Full API responses and cache files are saved locally and may contain product or patent-search details.

Mitigation: Review the saved ./linkfox output before sharing the workspace and delete sensitive result files when they are no longer needed.

Risk: Patent similarity results are preliminary and may be mistaken for legal conclusions.

Mitigation: Present results factually, highlight uncertainty, and recommend patent attorney review for infringement or launch decisions.

## Reference(s):

- [API reference](references/api.md)
- [Authentication and billing onboarding](references/onboarding.md)
- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-ruiguan-utility-patent-detection)
- [Publisher profile](https://clawhub.ai/user/linkfox-ai)

## Skill Output:

**Output Type(s):** [Markdown, JSON, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown tables and summaries with JSON API response files and optional shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Writes full API responses under ./linkfox/<date>/<session>/data; large responses are summarized unless inline output is requested.]

## Skill Version(s):

1.0.6 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
