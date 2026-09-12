## Description:

linear-native-node helps agents use a local Node.js helper to read Linear workspace data and, after explicit approval, create or update Linear issues, comments, projects, statuses, priorities, standup summaries, and branch names.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jwestburg](https://clawhub.ai/user/jwestburg)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to query Linear workspaces, summarize assigned work, create branch names, and perform explicitly approved Linear issue or project updates from an agent session.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses LINEAR_API_KEY to access Linear workspace data, and command output can include workspace-sensitive issue, project, user, email, description, and URL content.

Mitigation: Install only when agent access to the Linear workspace is intended, use the least-privileged Linear key available, scope reads with --team or LINEAR_DEFAULT_TEAM where possible, and redact workspace content before sharing logs or examples.

Risk: Approved write commands can create or modify Linear projects, issues, comments, workflow status, or priority.

Mitigation: Run write commands only with the --execute flag after the exact Linear action, target, and intended mutation are named and approved.

## Reference(s):

- [Linear GraphQL API endpoint](https://api.linear.app/graphql)
- [Linear API key settings](https://linear.app/settings/api)
- [ClawHub skill page](https://clawhub.ai/jwestburg/skills/linear-native-node)

## Skill Output:

**Output Type(s):** [text, JSON, shell commands, configuration, guidance]

**Output Format:** [Plain text or JSON command output, with Markdown setup and usage guidance in the skill instructions.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read commands may return workspace-sensitive Linear content; write commands require the --execute flag after explicit approval.]

## Skill Version(s):

1.0.22 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
