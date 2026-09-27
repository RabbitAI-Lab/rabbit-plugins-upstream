## Description:

Helps agents draft, schedule, publish, and review posts and analytics for social accounts connected to AdaptlyPost.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tarasshyn](https://clawhub.ai/user/tarasshyn)

### License/Terms of Use:

MIT-0

## Use Case:

AdaptlyPost users and their agents can prepare, schedule, publish, and monitor posts across connected social accounts, and review engagement analytics.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: An agent could publish, schedule, delete, or repeatedly post content to connected social accounts without the intended review.

Mitigation: Require explicit approval for each live or recurring post and deletion; save a draft if approval is unavailable.

Risk: A broad or exposed API token could grant unintended access to connected accounts.

Mitigation: Use a dedicated, revocable token with the least necessary role and connect only necessary accounts; keep the token private.

Risk: Connect links and webhooks can change account access or send notifications to an unintended destination.

Mitigation: Review each connect link and webhook destination before approval.

## Reference(s):

- [AdaptlyPost ClawHub release](https://clawhub.ai/tarasshyn/skills/adaptlypost)
- [AdaptlyPost](https://adaptlypost.com)
- [API reference](references/api-reference.md)
- [Platform configurations](references/platform-configs.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with API request examples and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an AdaptlyPost API token and connected accounts; posting actions require explicit approval.]

## Skill Version(s):

1.11.0 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
