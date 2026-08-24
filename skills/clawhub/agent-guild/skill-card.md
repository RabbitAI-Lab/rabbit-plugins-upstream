## Description:

Agent Guild lets local AI agents share identity, rules, memory, focus, handoff messages, and learning ledgers through a local Markdown/JSON workspace.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dqsjqian](https://clawhub.ai/user/dqsjqian)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and power users who run multiple local agents use this skill to let those agents read and update shared profile, rules, project state, handoffs, daily logs, and cross-agent learnings on one machine.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Local agents may share plaintext profile, rules, logs, inboxes, and memory through the same workspace.

Mitigation: Use the skill only with trusted local agents, do not store secrets or raw transcripts, and keep sensitive data out of shared memory unless the user explicitly consents.

Risk: Apply-mode commands can move, symlink, update, or persist files across shared skills, tools, MCP configuration, and memory locations.

Mitigation: Require explicit user approval before adopt --apply, upgrade --apply, or persistent memory writes, and review dry-run output before applying filesystem changes.

Risk: Shared skills, MCP servers, plugins, and tools can become available to multiple joined agents on the machine.

Mitigation: Keep shared capabilities trusted, review and scan them before deployment, and avoid pipe-to-shell installation when a safer reviewable install path is available.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dqsjqian/skills/agent-guild)
- [Publisher profile](https://clawhub.ai/user/dqsjqian)
- [Project homepage](https://github.com/dqsjqian/agent-guild)
- [Agent Guild specification](https://github.com/dqsjqian/agent-guild/blob/main/docs/SPEC.md)
- [Agent Guild onboarding guide](https://github.com/dqsjqian/agent-guild/blob/main/docs/ONBOARDING.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands, JSON and Markdown file paths, and Python CLI usage]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create, move, symlink, edit, or append local Markdown and JSON files under ~/.agent-guild/ when apply-mode commands are explicitly run; shared data is plaintext on the user's machine.]

## Skill Version(s):

3.5.0 (source: server release metadata, frontmatter, manifest.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
