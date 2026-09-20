## Description:

元阁 yotta-skills helps agents plan YottaMeta skill combinations, route tasks to suitable skills, install or update the YottaMeta skill family, inventory local skills, and adapt runtime hooks with explicit user confirmation for writes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yottameta](https://clawhub.ai/user/yottameta)

### License/Terms of Use:

MIT

## Use Case:

Developers and agent users use this skill to choose YottaMeta skill combinations for a task, preview and run pinned installs or updates, keep a local inventory of installed skills, and inspect host hook support. The skill is intended for explicit, user-confirmed installation and configuration workflows rather than silent background changes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A documented read-only health check can execute code from installed skill directories.

Mitigation: Avoid running `doctor` on project-controlled or untrusted skill directories until custom doctor execution is gated or made explicit.

Risk: Installer and updater actions can download or replace skill files across a broad skill family.

Mitigation: Install only when the YottaMeta npm package is trusted, prefer host-native OpenClaw install/update where available, and keep exact-version pinning unless a reviewed update strategy requires `--range`.

Risk: Automatic update, scan bypass, MCP config writes, global memory writes, and global install flags can expand the effect of a run.

Mitigation: Review before using `update --auto`, `--skip-scan`, MCP config writes, global memory writes, or `install.sh -g`; require explicit user confirmation for writes.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/yottameta/skills/yotta-skills)
- [Publisher profile](https://clawhub.ai/user/yottameta)
- [Homepage](https://github.com/YottaMeta/yotta-skills)
- [npm package](https://www.npmjs.com/package/@yottameta/yotta-skills)
- [Orchestration reference](references/orchestration.md)
- [Install flow reference](references/install-flow.md)
- [Skill list reference](references/skill-list.md)
- [FAQ](references/faq.md)
- [Tutorial](references/tutorial.md)
- [Walkthroughs](references/walkthroughs.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown and command-oriented guidance, with optional JSON output from CLI and MCP paths]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose install, update, route, inventory, hook, MCP configuration, and global-memory actions; documented write actions require user confirmation.]

## Skill Version(s):

0.19.13 (source: frontmatter, package.json, changelog, server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
