## Description:

Helps agents draft, schedule, publish, and review social posts and analytics for accounts connected to AdaptlyPost.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tarasshyn](https://clawhub.ai/user/tarasshyn)

### License/Terms of Use:

MIT-0

## Use Case:

AdaptlyPost users and their agents prepare and manage posts for connected social accounts, check publication status, and review account and post analytics.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A broadly privileged token can post to, delete from, or otherwise affect connected accounts.

Mitigation: Use a dedicated, revocable token and connect only needed accounts; prefer Contributor for drafts and Editor only when publishing is required.

Risk: Posts can go live immediately or recur beyond the current conversation.

Mitigation: Confirm content, accounts, timing, and visibility before each publication; review recurring-post requests and use drafts when approval is unavailable.

Risk: Webhooks can continue sending event data after the conversation ends.

Mitigation: Review webhook destinations and persistence before authorizing them.

## Reference(s):

- [AdaptlyPost skill on ClawHub](https://clawhub.ai/tarasshyn/skills/adaptlypost)
- [AdaptlyPost](https://adaptlypost.com)
- [API reference](references/api-reference.md)
- [Platform configurations](references/platform-configs.md)
- [AdaptlyPost OpenClaw plugin](https://github.com/adaptlypost/adaptlypost-openclaw/tree/main/openclaw-plugin)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Guidance]

**Output Format:** [Markdown with API request examples and human-readable status or analytics summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Publishing and scheduling act on connected accounts; delivery results require a follow-up check.]

## Skill Version(s):

1.14.0 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
