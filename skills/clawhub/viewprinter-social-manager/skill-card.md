## Description:

ViewPrinter Social Manager helps an agent operate a connected ViewPrinter account for social posting workflows, including scheduling or publishing posts, media handling, account groups, and performance reads.

This skill is ready for commercial/non-commercial use.

## Publisher:

[1vmgm](https://clawhub.ai/user/1vmgm)

### License/Terms of Use:

MIT-0

## Use Case:

External users and operators use this skill to manage social posts through connected ViewPrinter workspaces, including choosing accounts or groups, uploading and confirming media, scheduling posts, amending or canceling pending posts, and reading follower or post performance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A scheduled or immediate post can publish to real public social accounts and cannot be recalled by this skill after platform publishing begins.

Mitigation: Before scheduling or publishing, state the content, destination accounts, and exact time, then require explicit user confirmation and report only the outcome returned by ViewPrinter.

Risk: Deleting media permanently removes stored bytes and can break queued posts that reference the file.

Mitigation: Check pending posts that reference the media, name the affected file and dependencies, and wait for an explicit yes before calling media_delete.

Risk: Listing media, posts, accounts, or groups can read across all ViewPrinter workspaces available to the connected account.

Mitigation: Use listing tools only when relevant to the user's request and summarize workspace-scoped results without implying they were limited to a single item.

Risk: Retrying a scheduling request without idempotency handling can create duplicate posts.

Mitigation: Reuse the original idempotency_key on retry, or inspect posts_list before scheduling again.

Risk: OAuth account connection requires the user's browser session and platform consent; the agent cannot complete it inside the conversation.

Mitigation: Provide the connection link or documented OpenClaw MCP commands, then wait for the user to finish sign-in before continuing.

## Reference(s):

- [Posting workflow reference](references/posting.md)
- [Media workflow reference](references/media.md)
- [Accounts and groups reference](references/accounts.md)
- [ViewPrinter MCP endpoint](https://viewprinter.tech/api/mcp)
- [OpenClaw OAuth client metadata](https://viewprinter.tech/.well-known/openclaw-client.json)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, text]

**Output Format:** [Markdown with inline tool names and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include user-facing confirmations, absolute scheduling times, per-destination status reports, and ViewPrinter connection steps.]

## Skill Version(s):

1.1.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
