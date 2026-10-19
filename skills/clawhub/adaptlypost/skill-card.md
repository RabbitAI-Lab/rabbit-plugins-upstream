## Description:

Helps agents draft, schedule, publish, and review posts and analytics for social accounts connected to AdaptlyPost.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tarasshyn](https://clawhub.ai/user/tarasshyn)

### License/Terms of Use:

MIT-0

## Use Case:

People and teams with an AdaptlyPost account use this skill to manage posts on their connected social accounts, check publication status, and review engagement analytics.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A broad-privilege token can publish across connected accounts or change ongoing schedules.

Mitigation: Use a dedicated Contributor token for drafts; grant Editor or Admin access only when necessary and limit connected accounts.

Risk: Posts, recurring schedules, and retries can have lasting public effects.

Mitigation: Review the content, accounts, visibility, and timing before confirming each action; prefer drafts when uncertain.

Risk: Uploaded media and webhook changes can expose content or affect external notifications.

Mitigation: Confirm specific files before upload and review webhook changes before approving them.

## Reference(s):

- [AdaptlyPost on ClawHub](https://clawhub.ai/tarasshyn/skills/adaptlypost)
- [AdaptlyPost](https://adaptlypost.com)
- [AdaptlyPost API Reference](references/api-reference.md)
- [Platform-Specific Configs Reference](references/platform-configs.md)

## Skill Output:

**Output Type(s):** [Text, Shell commands, JSON, Guidance]

**Output Format:** [Markdown with API request examples and response summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May report per-platform publication status and engagement metrics.]

## Skill Version(s):

1.16.0 (source: skill frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
