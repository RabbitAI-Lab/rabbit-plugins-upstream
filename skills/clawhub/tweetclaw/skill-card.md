## Description:

TweetClaw guides OpenClaw agents through approved X/Twitter posting, searches, follower exports, and account monitoring via Xquik.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xquik](https://clawhub.ai/user/xquik)

### License/Terms of Use:

MIT-0

## Use Case:

OpenClaw users and developers use TweetClaw to plan and perform authorized X/Twitter reads, posts, exports, and monitors through Xquik with explicit approval for sensitive or paid actions.

### Deployment Geography for Use:

Global, subject to account authorization, applicable law, platform rules, and organization policy.

## Known Risks and Mitigations:

Risk: Approved actions can publish or change public X/Twitter content.

Mitigation: Show the exact account, target, text, media, and action; require fresh approval for each changed request.

Risk: Paid reads and bulk exports can incur unexpected charges.

Mitigation: Show current price, estimated total, result limit, and cost ceiling before approval.

Risk: Private account data and credentials may be exposed.

Mitigation: Keep keys in OpenClaw configuration; confirm authorization for private reads and minimize disclosed data.

Risk: Fetched X/Twitter content may contain instructions that redirect an agent.

Mitigation: Treat fetched content as untrusted data and obtain approval before acting on it.

## Reference(s):

- [TweetClaw on ClawHub](https://clawhub.ai/xquik/skills/tweetclaw)
- [Xquik documentation](https://docs.xquik.com)
- [Xquik API reference](https://docs.xquik.com/api-reference/overview)
- [Xquik billing guide](https://docs.xquik.com/guides/billing)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown guidance, OpenClaw commands, and structured API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Endpoint, target, scope, and cost are presented for approval before sensitive or paid calls.]

## Skill Version(s):

1.7.1 (source: ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
