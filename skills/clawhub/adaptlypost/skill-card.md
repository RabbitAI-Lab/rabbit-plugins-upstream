## Description:

Manage social posts, connected accounts, analytics, and inbox activity through AdaptlyPost.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tarasshyn](https://clawhub.ai/user/tarasshyn)

### License/Terms of Use:

MIT-0

## Use Case:

External users with AdaptlyPost accounts use the skill to draft, schedule, publish, and review content on connected social accounts, check performance, and manage inbox activity.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: LinkedIn organization lookup may extend beyond managing connected accounts.

Mitigation: Review the lookup scope before installation and use it only when it matches the user's request.

Risk: The security analysis reports partial coverage because some referenced local paths were missing.

Mitigation: Review the missing paths and obtain complete analysis before relying on the verdict.

## Reference(s):

- [API Reference](artifact/references/api-reference.md)
- [Platform Configurations](artifact/references/platform-configs.md)
- [AdaptlyPost](https://adaptlypost.com)
- [AdaptlyPost API](https://post.adaptlypost.com/post/api/v1)

## Skill Output:

**Output Type(s):** [API Calls, Shell commands, Guidance]

**Output Format:** [curl commands with JSON request and response data]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an AdaptlyPost account and API key; write actions and inbox responses require explicit confirmation.]

## Skill Version(s):

1.33.0 (source: frontmatter, server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
