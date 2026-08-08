## Description:

Detects and searches similar US utility and invention patents from product information to help sellers identify patent similarity, validity, and TRO enforcement indicators before listing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers and agent operators use this skill to run product-title and product-description based patent similarity searches for US marketplace risk review. It supports factual review of patent results and TRO indicators, but it does not provide legal advice or infringement conclusions.

### Deployment Geography for Use:

Global; patent search coverage is currently limited to the United States.

## Known Risks and Mitigations:

Risk: Product titles and descriptions are sent to LinkFox/Ruiguan for patent search.

Mitigation: Avoid submitting confidential pre-launch product details unless disclosure to the service is acceptable.

Risk: The skill uses LinkFox API credentials and may guide phone/SMS onboarding or payment flows.

Mitigation: Prefer official LinkFox web onboarding for credentials and billing, and verify payment actions before proceeding.

Risk: Patent results, cache files, metadata, and payment QR artifacts may be stored locally.

Mitigation: Review and clean generated linkfox response, cache, and QR files after use, especially on shared systems.

Risk: Patent similarity and TRO indicators are risk signals, not legal conclusions.

Mitigation: Use results for factual triage and consult a patent attorney before making infringement or launch decisions.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/linkfox-ai/skills/linkfox-ruiguan-utility-patent-detection)
- [API Reference](references/api.md)
- [Authentication and Billing Onboarding](references/onboarding.md)
- [LinkFox Skills](https://skill.linkfox.com/)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, configuration, guidance]

**Output Format:** [Markdown summaries and tables, JSON API responses, and shell commands for LinkFox authentication or billing setup.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Patent queries use productTitle, productDescription, region, and topNumber; full API responses may be saved locally while large responses are summarized.]

## Skill Version(s):

1.0.5 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
