## Description:

Draft, schedule, publish, and review posts and analytics for social accounts connected to AdaptlyPost.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tarasshyn](https://clawhub.ai/user/tarasshyn)

### License/Terms of Use:

MIT-0

## Use Case:

People managing AdaptlyPost-connected social accounts use this skill to draft, schedule, or publish posts, upload post media, check delivery, and review account analytics.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Publishing or scheduling to the wrong account can make unintended content public.

Mitigation: Use a dedicated low-privilege token, confirm content, accounts, timing, and visibility before each post, and prefer drafts when uncertain.

Risk: Uploaded media is available at a public URL even before a post is published.

Mitigation: Confirm each named file before upload and do not upload private files or unrelated local content.

Risk: A token with broad workspace access can affect multiple connected accounts.

Mitigation: Limit connected accounts and use a Contributor token for draft-only work; stop and report permission denials rather than bypassing them.

## Reference(s):

- [AdaptlyPost skill on ClawHub](https://clawhub.ai/tarasshyn/skills/adaptlypost)
- [AdaptlyPost](https://adaptlypost.com)
- [AdaptlyPost API reference](references/api-reference.md)
- [Platform configurations](references/platform-configs.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration instructions]

**Output Format:** [Markdown with API examples and post or analytics summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an AdaptlyPost API token and connected social accounts.]

## Skill Version(s):

1.12.0 (source: skill frontmatter and ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
