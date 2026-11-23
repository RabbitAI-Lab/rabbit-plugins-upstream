## Description:

Manage social posts, analytics, connected accounts, and inbox interactions across social platforms through AdaptlyPost.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tarasshyn](https://clawhub.ai/user/tarasshyn)

### License/Terms of Use:

MIT-0

## Use Case:

External users with an AdaptlyPost account use the agent to draft, schedule, publish, and review content on their connected social accounts, check analytics, and manage inbox interactions. The skill also documents account and workspace administration through AdaptlyPost.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill documents consequential actions such as deleting posts, accounts, workspaces, and members.

Mitigation: Follow the skill's explicit confirmation rules and use a dedicated API key with only the role and connected accounts needed.

Risk: The security review was partial because some local references could not be resolved; its benign verdict is not a guarantee of safety.

Mitigation: Review the available API and platform references and the security guidance before enabling the skill for an account.

## Reference(s):

- [AdaptlyPost API Reference](artifact/references/api-reference.md)
- [Platform Configurations](artifact/references/platform-configs.md)
- [AdaptlyPost](https://adaptlypost.com)
- [OpenClaw plugin approval rules](https://github.com/adaptlypost/adaptlypost-openclaw/tree/main/openclaw-plugin)

## Skill Output:

**Output Type(s):** [API Calls, Text, JSON, Configuration, Shell commands, Guidance]

**Output Format:** [Agent responses and AdaptlyPost API actions, with Markdown guidance and JSON request examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an AdaptlyPost API key; high-impact actions require explicit user confirmation.]

## Skill Version(s):

1.36.0 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
