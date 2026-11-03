## Description:

Draft, schedule and list social media posts on the channels a user connected in Hookpost, using the hookpost CLI. Use when the user asks to post, schedule, queue or draft something for X, LinkedIn, Threads, Facebook Pages, Discord, Slack or another channel they connected in Hookpost, to see what is scheduled, or to find the next free posting slot.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jatinder14](https://clawhub.ai/user/jatinder14)

### License/Terms of Use:

MIT-0

## Use Case:

External users with a Hookpost workspace use the skill to draft, schedule, publish, and review social posts across connected channels. It also helps them find open posting slots and check scheduled posts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The Hookpost API key authorizes actions in the user's workspace, including publishing posts.

Mitigation: Keep HOOKPOST_API_KEY private. Default to drafts, and show the exact text, channels, and time for review before scheduling or publishing.

Risk: Deleting a post group removes its copies across connected channels.

Mitigation: Delete only at the user's request; show the post and affected channels and confirm before deleting.

## Reference(s):

- [Hookpost MCP setup](https://hookpost.hookstep.in/mcp)
- [Post formatting guide](https://hookpost.hookstep.in/guides/post-to-multiple-social-media-at-once)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Guidance]

**Output Format:** [Markdown with inline CLI command examples and post text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can create drafts or schedule and publish posts in the user's Hookpost workspace; output and available channels depend on that workspace.]

## Skill Version(s):

1.0.0 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
