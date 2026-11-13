## Description:

Manages social posts, connected accounts, analytics, and inbox interactions through AdaptlyPost across supported social platforms.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tarasshyn](https://clawhub.ai/user/tarasshyn)

### License/Terms of Use:

MIT-0

## Use Case:

Social media managers and account owners use this skill to draft, schedule, publish, and review content for accounts connected to AdaptlyPost, check analytics, and handle incoming comments and messages. It requires explicit user approval for consequential posting and inbox actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can act on connected social accounts, including posting publicly and handling inbox items.

Mitigation: Connect only the accounts needed, use a role with limited permissions, and require explicit approval for posts and inbox actions that change or publish content.

Risk: The security scan is marked partial, with unresolved local references and an undeclared LinkedIn organization lookup.

Mitigation: Review the LinkedIn lookup behavior and unresolved references before enabling the skill, and grant account access only if those actions fit the intended use.

## Reference(s):

- [AdaptlyPost API reference](artifact/references/api-reference.md)
- [Platform configuration reference](artifact/references/platform-configs.md)
- [AdaptlyPost OpenClaw plugin](https://github.com/adaptlypost/adaptlypost-openclaw/tree/main/openclaw-plugin)
- [AdaptlyPost](https://adaptlypost.com)

## Skill Output:

**Output Type(s):** [Text, JSON, Shell commands, Guidance]

**Output Format:** [JSON API request bodies and concise text summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include post content, publishing status, analytics, and summaries of inbox items for connected accounts.]

## Skill Version(s):

1.32.0 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
