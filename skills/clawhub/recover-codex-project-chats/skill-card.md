## Description:

Diagnose and safely repair Codex Desktop projects that show "No chats/没有聊天" when conversations still appear under Recent or local history data needs provider, assignment, path, database, or backup recovery.

This skill is ready for commercial/non-commercial use.

## Publisher:

[songhonglei](https://clawhub.ai/user/songhonglei)

### License/Terms of Use:

MIT

## Use Case:

Developers and support engineers use this skill to diagnose missing Codex Desktop project chats, classify the underlying local state problem, and carry out a targeted recovery while preserving backups and conversation data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Repair commands can rewrite local Codex history metadata and copy sensitive chat or configuration data into backup folders.

Mitigation: Run diagnosis first, confirm provider compatibility before repair, quit Codex Desktop before mutation, and keep the generated backup until recovered chats open correctly.

## Reference(s):

- [Codex project-chat recovery patterns](references/incident-patterns.md)
- [ClawHub skill page](https://clawhub.ai/songhonglei/skills/recover-codex-project-chats)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and diagnostic summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May reference local backup paths, database row counts, rollout coverage, changed files, and unrecovered thread IDs.]

## Skill Version(s):

1.0.1 (source: server release metadata and SKILL.md)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
