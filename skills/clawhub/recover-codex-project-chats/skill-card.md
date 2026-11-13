## Description:

Diagnose and safely repair Codex Desktop projects that exist but show "No chats/没有聊天" while conversations may still appear under Recent.

This skill is ready for commercial/non-commercial use.

## Publisher:

[songhonglei](https://clawhub.ai/user/songhonglei)

### License/Terms of Use:

MIT

## Use Case:

Developers and engineers use this skill to diagnose and recover local Codex Desktop project chat visibility when project folders exist but chats do not appear. It supports cautious repair workflows for provider mismatches, missing project assignments, moved workspaces, archived threads, and schema-compatible database restores.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill handles local Codex databases, rollout files, global state, and backups that may contain sensitive conversation history.

Mitigation: Quit Codex Desktop before repair, keep pre-repair backups, avoid sudo, and treat generated backups as sensitive data.

Risk: Security evidence flags an unsafe SQL query path when configuration data may be untrusted.

Mitigation: Review or patch SQL handling before use in environments where config.toml or provider names may be modified by an untrusted party.

Risk: The README includes unpinned remote install guidance.

Mitigation: Install through ClawHub or from a pinned, reviewed commit.

## Reference(s):

- [Codex project-chat recovery patterns](references/incident-patterns.md)
- [ClawHub skill page](https://clawhub.ai/songhonglei/skills/recover-codex-project-chats)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and recovery checklists]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include local paths, backup locations, changed-row counts, and unrecovered thread IDs gathered during diagnosis and repair.]

## Skill Version(s):

1.0.1 (source: server release metadata and SKILL.md body)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
