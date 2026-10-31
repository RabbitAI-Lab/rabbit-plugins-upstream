## Description:

Publish and schedule social media posts to Instagram, TikTok, X (Twitter), Threads, LinkedIn, Facebook Pages, YouTube Shorts and Bluesky from OpenClaw, Hermes, Claude Code or Codex. One post adapted to each network's limits, cross-posted now or scheduled up to 30 days ahead, with a per-network delivery receipt, via the 1Social MCP server (OAuth, no API key). Use to post on social media, cross-post, schedule posts, plan a content calendar, or check what was published.

This skill is ready for commercial/non-commercial use.

## Publisher:

[sultanlive](https://clawhub.ai/user/sultanlive)

### License/Terms of Use:

MIT-0

## Use Case:

Social media managers and creators use this skill to adapt, cross-post, schedule, and check posts across their connected social accounts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Uploading a local media file creates a public link immediately, even if the post is later declined.

Mitigation: Show the user the exact files and get approval before uploading; explain that some networks may require manual deletion.

Risk: Publishing is public, and some networks cannot be deleted through 1Social.

Mitigation: Preview the post and get clear user approval before publishing; report per-network delivery and deletion limits accurately.

Risk: Retrying a delivery consumes quota and may create a duplicate if delivery status is unknown.

Mitigation: Check the network with the user and confirm delivery status before retrying an unknown result.

## Reference(s):

- [1Social MCP setup and documentation](https://1social.dev/mcp?ref=skill)
- [1Social MCP documentation](https://1social.dev/mcp)

## Skill Output:

**Output Type(s):** [Text, Guidance, API Calls, Shell commands, Configuration instructions]

**Output Format:** [Social post drafts and publishing status receipts, with setup instructions in Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Post content may be adapted per network; publishing results are reported per network.]

## Skill Version(s):

1.0.1 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
