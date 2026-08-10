## Description:

睿观-外观专利检测 helps agents check product images against Ruiguan design patent data across 25+ regions and return similarity, TRO, and radar-analysis results for patent risk review.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External e-commerce sellers, IP professionals, and agent operators use this skill to submit product images and related product context for design patent similarity checks, TRO history review, and risk-oriented patent result summaries. It is for design patent screening and does not replace professional legal advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Product images and metadata are sent to LinkFox/Ruiguan for analysis, and local image files may be uploaded to a publicly accessible URL.

Mitigation: Use the skill only for images and product details that are acceptable to share with the service; avoid unreleased, confidential, or sensitive listings unless this data flow has been approved.

Risk: The skill can guide API-key setup, phone-based onboarding, and paid credit purchase flows.

Mitigation: Confirm account ownership, payment authorization, and expected credit consumption before login, ordering, or analysis calls.

Risk: Full API responses are stored locally and may include patent results, product context, and analysis details.

Mitigation: Run the skill in an appropriate workspace and review local retention requirements for the generated linkfox session data.

Risk: Design patent similarity and radar outputs are screening signals, not legal determinations.

Mitigation: Present results faithfully, include the professional IP attorney reminder, and avoid treating the output as legal advice.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/linkfox-ai/skills/linkfox-ruiguan-detection-patent-design)
- [Publisher profile](https://clawhub.ai/user/linkfox-ai)
- [睿观-外观专利检测 API reference](artifact/references/api.md)
- [Authentication and billing onboarding guide](artifact/references/onboarding.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with shell commands and JSON patent detection results saved to local files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Calls a paid LinkFox/Ruiguan service, may upload local images to a public 24-hour URL, caches repeated requests for 24 hours, and stores full API responses under a local linkfox session directory.]

## Skill Version(s):

1.0.5 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
