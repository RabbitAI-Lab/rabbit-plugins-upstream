## Description:

旅行保险智能推荐与理赔指南，提供场景化保险推荐、条款白话解读和理赔流程指引。

This skill is ready for commercial/non-commercial use.

## Publisher:

[travel-skills](https://clawhub.ai/user/travel-skills)

### License/Terms of Use:

MIT-0

## Use Case:

External Chinese-speaking travelers use this skill to compare travel insurance options, understand policy terms in plain language, and follow claims steps for medical, flight delay, baggage, cancellation, and similar travel scenarios.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requests PROXY_TOKEN while describing itself as a zero-configuration knowledge-base skill.

Mitigation: Review the skill before installing and only provide a proxy token if the deployment has a documented need for it.

Risk: Insurance recommendations, prices, channels, and claims steps may not match current insurer terms or a user's specific eligibility.

Mitigation: Verify official insurer policy terms, exclusions, purchase pages, and claims requirements before relying on the output.

Risk: The skill provides general travel-insurance information rather than licensed personalized insurance advice.

Mitigation: Treat outputs as informational guidance and consult qualified insurance or legal professionals for binding decisions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/travel-skills/skills/travel-insurance-smart-buy)
- [Publisher profile](https://clawhub.ai/user/travel-skills)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Markdown-style plain text with structured recommendations, checklists, links, and step-by-step guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include insurance purchase-channel links and should be reviewed against official insurer terms before use.]

## Skill Version(s):

2.0.2 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
