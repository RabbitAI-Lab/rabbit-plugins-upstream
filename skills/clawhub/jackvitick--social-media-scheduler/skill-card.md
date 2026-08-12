## Description:

Schedule, publish, and cross-post social media posts to X, LinkedIn, Instagram, Facebook, TikTok, Threads, YouTube, and Bluesky.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jackvitick](https://clawhub.ai/user/jackvitick)

### License/Terms of Use:

MIT-0

## Use Case:

External users and content teams use this skill to plan content calendars, draft platform-specific social posts, and schedule or publish them through authorized Socialync-connected accounts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can prepare, schedule, or publish posts to real social accounts connected through Socialync.

Mitigation: Review each draft before approval and use autonomous recurring posting only for content streams where unattended publishing is acceptable.

Risk: A batch can fail or partially publish if quota, platform connection health, or profile eligibility is not checked first.

Mitigation: Run list_profiles, check_quota, and list_connections before scheduling or publishing a batch.

Risk: A retry after a network timeout can misreport publish state or create confusion about whether a post shipped.

Mitigation: Check get_post_history or get_scheduled_posts before retrying or reporting status.

## Reference(s):

- [Socialync Homepage](https://www.socialync.io)
- [Socialync MCP Endpoint](https://mcp.socialync.io/mcp)
- [ClawHub Skill Page](https://clawhub.ai/jackvitick/skills/social-media-scheduler)
- [Publisher Profile](https://clawhub.ai/user/jackvitick)
- [Platform Playbook](artifact/platform-playbook.md)
- [Publishing Reference](artifact/publishing.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration instructions, API Calls, Guidance]

**Output Format:** [Markdown tables, prose guidance, inline shell commands, and Socialync MCP tool calls]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May draft posts without an account; publishing requires user-authorized Socialync accounts and explicit approval unless the user has configured autonomous recurring posting.]

## Skill Version(s):

1.0.3 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
