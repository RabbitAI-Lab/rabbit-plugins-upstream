## Description:

Consolidate daily session logs into L2 topic files and a compact MEMORY.md index, in three bounded phases with backups, lifecycle and secret guards.

This skill is ready for commercial/non-commercial use.

## Publisher:

[lzyling](https://clawhub.ai/user/lzyling)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to consolidate OpenClaw Markdown memory from daily logs into durable topic files, a compact MEMORY.md index, and a dream-log record. It supports manual runs and scheduled daily consolidation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill rewrites durable memory files and can change what future agent sessions recall.

Mitigation: Run the first consolidation manually, review the write plan, and confirm backups exist before allowing scheduled runs.

Risk: The ClawHub security review flags unsafe shell/path patterns and a home-configuration read outside the workspace.

Mitigation: Avoid enabling the cron workflow until the heredoc append and audit path containment issues are fixed; keep runs limited to the documented memory paths.

Risk: Daily logs may contain untrusted text or credentials that should not be promoted into curated memory.

Mitigation: Use the documented secret guard, omit credential values, review any flagged source file manually, and treat the audit helper as advisory rather than full DLP.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/lzyling/skills/signal-dreaming)
- [Publisher Profile](https://clawhub.ai/user/lzyling)
- [Signal Dreaming Full Protocol](references/dream-protocol.md)
- [Signal Dreaming Version History](references/changelog.md)
- [Dream Audit Helper](references/dream-audit.sh)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and cron configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces workspace memory updates in MEMORY.md, memory/*.md, and memory/dream-log.md when an agent follows the protocol.]

## Skill Version(s):

5.0.2 (source: evidence release version, SKILL.md version note, changelog)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
