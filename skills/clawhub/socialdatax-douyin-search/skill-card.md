## Description:

Searches Douyin hot lists and video or image/text posts by keyword to support content research, competitor analysis, and trend review.

This skill is ready for commercial/non-commercial use.

## Publisher:

[devinchen2014](https://clawhub.ai/user/devinchen2014)

### License/Terms of Use:

MIT-0

## Use Case:

External social media researchers and marketers can use the skill to review Douyin hot searches and find video or image/text posts for content research, competitor analysis, and trend monitoring.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Search terms may be sent to SocialDataX when requesting Douyin data.

Mitigation: Avoid sending sensitive or identifying terms; use queries appropriate to share with the service.

Risk: CLI data calls rely on a SocialDataX API key.

Mitigation: Keep the key private and use the documented local credential handling; do not put it in chat or project files.

## Reference(s):

- [SocialDataX API access](https://socialdatax.com/ai?from=clawhub)
- [ClawHub skill release](https://clawhub.ai/devinchen2014/skills/socialdatax-douyin-search)

## Skill Output:

**Output Type(s):** [JSON, Text, Markdown]

**Output Format:** [JSON search results with concise Markdown or text summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Search results may include video and image/text posts; paginated searches provide a continuation token.]

## Skill Version(s):

0.1.24 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
