## Description:

Commerce-focused intelligence for creator-led selling, primarily TikTok Shop. Use when users need sale/goods/live/video-ad monetization signals, product detail checks, or creator commerce potential comparison with operation-level API mapping.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chengyu-xixihaha](https://clawhub.ai/user/chengyu-xixihaha)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to analyze TikTok Shop creator commerce performance across sales, products, live sessions, and video-ad activity. It supports creator monetization comparisons, product detail checks, opportunity sizing, risk notes, and pilot recommendations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: TikTok commerce identifiers and lookup parameters are sent to an external SCRUMBALL/SCData gateway.

Mitigation: Use the skill only when sending those identifiers to the gateway is acceptable for the task and data policy.

Risk: The operation runner can use local environment credentials such as SCRUMBALL_API_KEY.

Mitigation: Use a dedicated API key and keep unrelated secrets out of the .env file.

Risk: Changing SCRUMBALL_BASE_URL can redirect requests to another host.

Mitigation: Set SCRUMBALL_BASE_URL only to a trusted gateway.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chengyu-xixihaha/skills/influencer-commerce-intel)
- [API Index](references/api-index.md)
- [Request and Response Guide](references/request-response.md)
- [Operation Manifest](references/operations.json)

## Skill Output:

**Output Type(s):** [text, markdown, json, shell commands, configuration, guidance]

**Output Format:** [Markdown summaries and recommendations, JSON API responses, and shell commands for operation execution.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Expected response sections are Commerce summary, Opportunity, Risk, and Next step.]

## Skill Version(s):

1.0.0 (source: config.yaml and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
