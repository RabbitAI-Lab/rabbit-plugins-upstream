## Description:

Write, plan and schedule social media posts in a business's own voice with Buzzmark's MCP server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[buzzmark](https://clawhub.ai/user/buzzmark)

### License/Terms of Use:

MIT-0

## Use Case:

Founders, small businesses, and social media teams use this skill to draft, adapt, plan, schedule, and review social posts in their brand voice across connected social accounts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The optional BUZZMARK_API_KEY is a bearer credential used to authenticate requests.

Mitigation: Keep the key in a trusted agent's secret store, avoid sharing it in prompts or logs, and revoke it from Buzzmark's AI apps page if exposed.

Risk: Linked pages and setup destinations were outside the security scan scope.

Mitigation: Check that a linked destination is trusted before opening it or entering account credentials.

## Reference(s):

- [Buzzmark AI apps setup guide](https://buzzmark.ai/ai-apps)
- [Buzzmark MCP tools and inputs](https://buzzmark.ai/ai-apps/mcp)
- [Buzzmark API apps and key management](https://buzzmark.ai/app/ai-apps)
- [Buzzmark settings](https://buzzmark.ai/app/settings)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Social post drafts, platform adaptations, weekly content plans, and performance summaries in text or Markdown.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Content is tailored to the selected brand profile, social accounts, and schedule; posts are scheduled for later publication rather than posted immediately.]

## Skill Version(s):

1.0.2 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
