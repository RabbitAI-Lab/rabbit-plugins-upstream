## Description:

元阁 yotta-skills routes agent tasks across the YottaMeta skill family, inventories installed skills, and generates installer or update commands for selected yotta-* skills.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yottameta](https://clawhub.ai/user/yottameta)

### License/Terms of Use:

MIT

## Use Case:

Developers and agent operators use this skill to plan which YottaMeta skills fit a task, inspect installed skill inventory, and produce explicit install, update, route, or re-index commands for an agent or skills directory.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Persistent agent-memory changes could alter future sessions beyond the immediate request.

Mitigation: Do not allow automatic writes to AGENTS.md, CLAUDE.md, or other persistent memory files; require explicit user review before any persistent configuration change.

Risk: Installer and update commands can modify local agent skill directories.

Mitigation: Use explicit --dir or --agent targets, preview with --dry-run, and use --pin when reproducible installation is needed.

Risk: The CLI reports scan warnings but does not enforce a hard block for DO NOT INSTALL findings.

Mitigation: Treat any DO NOT INSTALL scan warning as a stop condition and review manually before continuing.

Risk: Automatic installation or update behavior could affect more skills than intended.

Mitigation: Avoid global installation flags, install only named skills when possible, and require confirmation before running update or update --auto.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/yottameta/skills/yotta-skills)
- [README](artifact/README.md)
- [Orchestration guide](artifact/references/orchestration.md)
- [Install flow](artifact/references/install-flow.md)
- [Skill list](artifact/references/skill-list.md)
- [FAQ](artifact/references/faq.md)
- [Walkthroughs](artifact/references/walkthroughs.md)
- [npm package](https://www.npmjs.com/package/@yottameta/yotta-skills)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown or plain-text guidance with inline shell commands, plus optional JSON output from CLI or MCP tools]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce install, update, route, inventory, re-index, and optional MCP configuration instructions; commands can affect local skill directories when run by the user or agent.]

## Skill Version(s):

0.7.0 (source: frontmatter, package.json, changelog, release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
