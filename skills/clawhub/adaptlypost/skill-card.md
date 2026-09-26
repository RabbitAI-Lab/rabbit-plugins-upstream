## Description:

Helps agents draft, schedule, publish, and review social posts and analytics for accounts connected to AdaptlyPost.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tarasshyn](https://clawhub.ai/user/tarasshyn)

### License/Terms of Use:

MIT-0

## Use Case:

People and teams with an AdaptlyPost account use this skill to prepare and manage posts on connected social accounts, check publishing outcomes, and review engagement analytics.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A mistaken schedule or live post can publish unwanted content to connected public accounts.

Mitigation: Confirm the exact content, accounts, timing, and visibility before each post; default to a draft when uncertain.

Risk: Uploaded media becomes publicly accessible before a post is published.

Mitigation: Confirm the exact file with the user before upload and upload only media they explicitly named.

Risk: Broad API permissions or exposed connect links and webhooks can affect social accounts or persistent integrations.

Mitigation: Use a dedicated, revocable token with the lowest suitable role; review connect-link, webhook, and deletion requests and keep access links private.

## Reference(s):

- [AdaptlyPost on ClawHub](https://clawhub.ai/tarasshyn/skills/adaptlypost)
- [AdaptlyPost](https://adaptlypost.com)
- [AdaptlyPost API reference](artifact/references/api-reference.md)
- [AdaptlyPost platform configurations](artifact/references/platform-configs.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown with API request examples and plain-language status or analytics summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Publishing outcomes are reported per platform; analytics availability varies by network.]

## Skill Version(s):

1.9.1 (source: release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
