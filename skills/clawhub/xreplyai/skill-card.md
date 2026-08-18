## Description:

Generate, schedule, and publish posts across 15 platforms in the user's voice using AI, while managing preferences and tracking billing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jmoon90](https://clawhub.ai/user/jmoon90)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to let an agent generate social posts, create and edit drafts, schedule or publish content across connected accounts, upload media, manage posting preferences, and check billing or quota status.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: An agent can publish or schedule public social content on connected accounts.

Mitigation: Require a final user check of the content, account, platform, and timing before publishing, scheduling, or creating recurring plans.

Risk: XREPLY_TOKEN grants access to the user's XReplyAI account through the MCP server.

Mitigation: Keep XREPLY_TOKEN secret, provide it only through the intended environment variable, and avoid exposing it in prompts, logs, or shared files.

Risk: Media upload tools can read local file paths supplied to the agent.

Mitigation: Pass only intended media file paths and verify the selected file before upload.

Risk: Generation, batch, recurring plan, and premium model settings can affect quota or prepaid AI balance.

Mitigation: Check billing or quota status and get user confirmation before large generation runs or switching to premium AI models.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/jmoon90/skills/xreplyai)
- [XReplyAI homepage](https://xreplyai.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with mcporter and npx shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires XREPLY_TOKEN and either mcporter or npx; some actions depend on connected social accounts, paid plan status, quota, filesystem access, and platform-specific media support.]

## Skill Version(s):

0.3.25 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
