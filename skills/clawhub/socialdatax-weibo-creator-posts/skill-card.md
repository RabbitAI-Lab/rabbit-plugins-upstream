## Description:

Helps agents retrieve and summarize Weibo creator posts for recent publishing reviews, content research, and creator analysis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[devinchen2014](https://clawhub.ai/user/devinchen2014)

### License/Terms of Use:

MIT-0

## Use Case:

Creators, researchers, and analysts use this skill to review Weibo creator posts, compare publishing patterns, and summarize content and engagement.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requests an unpinned package at runtime, so its behavior may change between uses.

Mitigation: Use a pinned, vetted version of socialdatax-skills where possible.

Risk: The agent process needs a SocialDataX API key to retrieve data.

Mitigation: Provide only the required SOCIALDATAX_API_KEY and avoid exposing unrelated local secrets.

## Reference(s):

- [SocialDataX API access and product information](https://socialdatax.com/ai?from=clawhub)
- [ClawHub skill release](https://clawhub.ai/devinchen2014/skills/socialdatax-weibo-creator-posts)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands]

**Output Format:** [Markdown summaries of creator posts, with optional shell commands for JSON retrieval]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include post IDs, content, publication times, media links, and interaction counts when available.]

## Skill Version(s):

0.1.19 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
