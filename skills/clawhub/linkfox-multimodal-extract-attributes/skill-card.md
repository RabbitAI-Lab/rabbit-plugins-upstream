## Description:

Analyzes product main and additional images with LinkFox multimodal AI to extract visual attributes, image prompts, and grouped structured product data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and e-commerce operators use this skill to turn product image URLs and listing data into structured visual attributes, grouped summaries, and prompt-like descriptions for product analysis workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Product image URLs, product data, prompts, userInput, and feedback content are sent to LinkFox services.

Mitigation: Install only if this data sharing is acceptable, use official LinkFox endpoint environment variables, and avoid placing secrets or sensitive personal data in prompts or product records.

Risk: The artifact includes account login, API-key generation, billing, order creation, and payment flows.

Mitigation: Review authentication, plan, order, and payment steps before approving them, and do not auto-approve unexpected billing actions.

Risk: Complete API responses and cache entries may persist in local linkfox output directories.

Mitigation: Periodically clear local linkfox output and cache directories when retained product data is sensitive.

Risk: Multimodal image analysis may produce incorrect or incomplete visual attributes.

Mitigation: Present extracted attributes factually, keep source product identifiers visible, and have users review results before making business decisions.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/linkfox-ai/skills/linkfox-multimodal-extract-attributes)
- [API Reference](references/api.md)
- [Authentication and Billing Onboarding](references/onboarding.md)
- [LinkFox Skills](https://skill.linkfox.com/)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, configuration, guidance]

**Output Format:** [Markdown tables and summaries, shell commands, configuration guidance, and JSON response files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Writes complete API responses under a local linkfox session directory, summarizes large responses, and may use a 24-hour local cache.]

## Skill Version(s):

1.0.6 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
