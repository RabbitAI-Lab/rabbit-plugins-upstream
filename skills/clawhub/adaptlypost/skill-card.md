## Description:

Schedule, publish, and review social posts and analytics for accounts connected to AdaptlyPost.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tarasshyn](https://clawhub.ai/user/tarasshyn)

### License/Terms of Use:

MIT-0

## Use Case:

People using an AdaptlyPost account use this skill to draft, schedule, publish, edit, and review social posts and analytics for their connected accounts. It is intended for account-specific requests and requires explicit confirmation before publishing or sensitive account actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Uploaded media is stored on hosted storage and may be accessible through public URLs.

Mitigation: Confirm the exact user-selected file and that public URL access is acceptable before uploading it.

Risk: The security review is partial and medium-confidence because some local references could not be resolved.

Mitigation: Review the complete skill and its references before relying on the scan verdict.

Risk: Posts are public and can be difficult to take back; account and webhook changes can also have lasting effects.

Mitigation: Get explicit user confirmation of post content, accounts, timing, and visibility before publishing, and confirm separately before destructive or connection actions.

## Reference(s):

- [AdaptlyPost API Reference](references/api-reference.md)
- [Platform Configurations](references/platform-configs.md)
- [AdaptlyPost Homepage](https://adaptlypost.com)
- [ClawHub Release Page](https://clawhub.ai/tarasshyn/skills/adaptlypost)

## Skill Output:

**Output Type(s):** [JSON, Text]

**Output Format:** [API request and response data, with social post content and concise status or analytics summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include post status, per-platform results, and account analytics.]

## Skill Version(s):

1.27.3 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
