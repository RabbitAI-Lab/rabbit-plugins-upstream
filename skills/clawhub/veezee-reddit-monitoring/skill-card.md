## Description:

Continuously monitor Reddit for new posts and comments mentioning a topic, brand, or competitor, deduped across polls.

This skill is ready for commercial/non-commercial use.

## Publisher:

[veezee-build](https://clawhub.ai/user/veezee-build)

### License/Terms of Use:

MIT-0

## Use Case:

External teams, developers, and operators use this skill to monitor Reddit for new brand, topic, or competitor mentions and to report only new deduplicated posts or comments across polling cycles.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses Veezee as an external service and may require an API key or sign-in.

Mitigation: Confirm the user is willing to use Veezee, mint or configure the key deliberately, and avoid placing credentials in shared outputs.

Risk: Continuous monitoring can consume paid credits if cadence and scope are left unattended.

Mitigation: Check usage before starting a loop, set max_credits on calls, and use an intentional poll cadence and watch list.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/veezee-build/skills/veezee-reddit-monitoring)
- [Veezee Reddit MCP Server](https://mcp.veezee.io/reddit)
- [Veezee All Platforms MCP Server](https://mcp.veezee.io/all)
- [Veezee API Key Mint Endpoint](https://api.veezee.io/v1/keys/mint)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with setup steps, API or CLI examples, and periodic mention summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Summaries include source type, subreddit, author, excerpt, created_at, permalink, and total credits spent.]

## Skill Version(s):

1.0.0 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
