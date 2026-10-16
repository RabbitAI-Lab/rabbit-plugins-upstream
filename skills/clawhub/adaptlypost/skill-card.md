## Description:

Helps agents draft, schedule, publish, and review posts and analytics for social accounts connected to AdaptlyPost.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tarasshyn](https://clawhub.ai/user/tarasshyn)

### License/Terms of Use:

MIT-0

## Use Case:

People and teams with connected AdaptlyPost accounts use this skill to draft and publish social posts, upload media, monitor delivery, and review engagement analytics.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Publishing posts or recurring schedules to the wrong accounts can have public or lasting effects.

Mitigation: Confirm the exact content, accounts, timing, and visibility before each post; prefer drafts when uncertain and require separate consent for recurring posts.

Risk: Media uploads can expose files through public URLs before any post goes live.

Mitigation: Confirm each file and upload only user-selected media; do not upload secrets or unrelated local files.

Risk: A compromised API token could affect all connected social accounts and associated settings.

Mitigation: Use a dedicated, revocable token with the least necessary role and connect only needed accounts; reserve elevated roles for authorized publishing or administration.

## Reference(s):

- [AdaptlyPost skill release](https://clawhub.ai/tarasshyn/skills/adaptlypost)
- [AdaptlyPost](https://adaptlypost.com)
- [AdaptlyPost API reference](references/api-reference.md)
- [Platform-specific configuration reference](references/platform-configs.md)

## Skill Output:

**Output Type(s):** [Text, Shell commands, JSON]

**Output Format:** [Markdown guidance and curl commands with JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports post status and social analytics; actions require connected accounts and an AdaptlyPost API token.]

## Skill Version(s):

1.15.0 (source: skill frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
