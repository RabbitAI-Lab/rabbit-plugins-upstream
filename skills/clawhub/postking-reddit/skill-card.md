## Description:

Build a fit-scored subreddit pool, match content to the best communities with posting angles, and rewrite posts natively for Reddit.

This skill is ready for commercial/non-commercial use.

## Publisher:

[bitsandtea](https://clawhub.ai/user/bitsandtea)

### License/Terms of Use:

MIT-0

## Use Case:

Marketing teams and agents use this skill to identify fit-scored Reddit communities for a brand, match content to appropriate subreddits with posting angles, and produce Reddit-native drafts for human review and posting.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Brand details and draft content may be sent to PostKing MCP while using credits and authentication.

Mitigation: Confirm the PostKing MCP connection, account, and credit use are acceptable before sending sensitive brand or draft content.

Risk: Generated subreddit recommendations or draft copy may not fully satisfy community rules or promotion tolerance.

Mitigation: Review the suggested rule_to_watch, promotion_mode, subreddit context, and final draft before posting.

Risk: Users may mistake the skill for an automated Reddit publishing workflow.

Mitigation: Keep a human review and posting step in the workflow; the skill prepares drafts and guidance rather than publishing on the brand's behalf.

## Reference(s):

- [PostKing: Reddit Growth on ClawHub](https://clawhub.ai/bitsandtea/skills/postking-reddit)
- [PostKing MCP endpoint](https://mcp.postking.app/mcp)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Markdown guidance with Reddit draft text, subreddit recommendations, posting angles, and rule or promotion notes.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces review-ready drafts and recommendations for a human to evaluate before posting; it does not automatically publish to Reddit.]

## Skill Version(s):

1.0.3 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
