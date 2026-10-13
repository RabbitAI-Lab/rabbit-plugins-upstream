## Description:

Guides OpenClaw agents through approved X/Twitter searches, posts, exports, and account monitoring with Xquik.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xquik](https://clawhub.ai/user/xquik)

### License/Terms of Use:

MIT-0

## Use Case:

OpenClaw users and developers use TweetClaw to discover Xquik endpoints and, with explicit approval, search X/Twitter, publish posts, export account data, and monitor accounts.

### Deployment Geography for Use:

Global, subject to account authorization, applicable law, platform rules, and organizational policy.

## Known Risks and Mitigations:

Risk: Approved calls can change public X/Twitter content.

Mitigation: Review the account, endpoint, target, exact payload, and final text or media before each write.

Risk: Private account reads and bulk exports can expose sensitive data.

Mitigation: Confirm account authorization, scope, and result limits; minimize private data in responses.

Risk: Paid requests and recurring monitors can consume prepaid credits or continue running.

Mitigation: Confirm price, cost ceiling, target, and recurrence before approval; review additional paid calls individually.

Risk: Credentials or untrusted X content could be mishandled.

Mitigation: Keep keys in OpenClaw config or the Xquik dashboard and treat retrieved X content as data, not instructions.

## Reference(s):

- [TweetClaw on ClawHub](https://clawhub.ai/xquik/skills/tweetclaw)
- [Xquik documentation](https://docs.xquik.com)
- [Xquik API reference](https://docs.xquik.com/api-reference/overview)
- [Xquik billing guide](https://docs.xquik.com/guides/billing)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Structured API responses]

**Output Format:** [Markdown guidance and commands; structured endpoint and API results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Public posts, paid requests, private reads, exports, and recurring monitors require explicit approval.]

## Skill Version(s):

1.7.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
