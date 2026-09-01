## Description:

Use when users ask to sync, restore, apply, back up, push, or roll back local agent instructions, rules, or skills for Codex, Claude Code, OpenCode, Grok Build, CodeBuddy Code, WorkBuddy, or another Agent Skills-compatible platform.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ferbylv](https://clawhub.ai/user/ferbylv)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to inspect, back up, apply, restore, push, and roll back selected local agent instructions, rules, and skills through a Git remote. It is intended for filesystem-capable agent environments where Python and Git are available.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Applying or restoring from a remote can replace selected local agent instructions, rules, or skills.

Mitigation: Review the generated plan, including platform, action, root, assets, backup directory, remote, and branch, before approving any command that uses --yes.

Risk: Pushing selected local assets can publish unintended instruction changes to the configured Git remote.

Mitigation: Confirm the selected assets and destination branch before push; the skill stages only selected paths and does not force-push.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/ferbylv/skills/agentdots-sync)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and command output summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill defaults to read-only inspection and requires explicit approval before mutating local assets or pushing to a remote.]

## Skill Version(s):

0.1.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
