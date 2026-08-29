## Description:

Provides agent access to Bitbucket through OOMOL's `oo` connector for reading, creating, updating, and deleting repository data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and teams use this skill to let an agent inspect and manage Bitbucket workspaces, repositories, branches, commits, pull requests, pipelines, snippets, users, projects, runners, and legacy issues through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can read and change Bitbucket repository data through a connected account.

Mitigation: Install it only when agent-operated Bitbucket access is intended, and confirm the workspace, repository, action, and payload before write operations.

Risk: Destructive actions can delete repositories, branches, or pipeline variables.

Mitigation: Require explicit approval for destructive commands after the exact target and effect are clear.

Risk: Pull request merges, declines, pipeline stops, and pipeline variable changes can affect delivery workflows.

Mitigation: Review these requests carefully and approve them only when the requested state change matches the user's intent.

## Reference(s):

- [ClawHub Bitbucket skill listing](https://clawhub.ai/oomol/skills/oo-bitbucket)
- [Bitbucket homepage](https://bitbucket.org)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [State-changing and destructive actions require confirmation before execution.]

## Skill Version(s):

1.0.0 (source: evidence release and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
