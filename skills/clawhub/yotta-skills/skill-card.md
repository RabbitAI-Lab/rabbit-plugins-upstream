## Description:

YuanGe (元阁) provides orchestration routing, local skill inventory, hook adaptation, and a one-command installer for the YottaMeta skill family.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yottameta](https://clawhub.ai/user/yottameta)

### License/Terms of Use:

MIT

## Use Case:

Developers and agent operators use this skill to choose YottaMeta skill combinations, install or update selected yotta-* skills, inventory local skill directories, and inspect hook capability behavior with user-confirmed actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The installer can download packages and run package-declared code with user privileges.

Mitigation: Install only when the YottaMeta npm publisher is trusted, prefer pinned versions, and review package lifecycle behavior before install or update in sensitive environments.

Risk: The tool can modify agent skill directories and local ~/.yottaskills state.

Mitigation: Use explicit --agent or --dir targets, preview with --dry-run or read-only checks when possible, and avoid install.sh -g/--global.

Risk: Using --range or --skip-scan can increase supply-chain or verification risk.

Mitigation: Keep the default pinned install behavior and avoid --skip-scan unless the user intentionally accepts an explicit unverified path.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/yottameta/skills/yotta-skills)
- [npm package @yottameta/yotta-skills](https://www.npmjs.com/package/@yottameta/yotta-skills)
- [Install flow reference](references/install-flow.md)
- [Orchestration reference](references/orchestration.md)
- [Skill list reference](references/skill-list.md)
- [FAQ](references/faq.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration, JSON]

**Output Format:** [Markdown guidance with command examples and optional JSON outputs from routing, inventory, doctor, update, and MCP workflows]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May modify selected agent skill directories and local ~/.yottaskills state when the user confirms install, update, reindex, hook, or rollback actions.]

## Skill Version(s):

0.19.5 (source: frontmatter, package.json, changelog released 2026-09-15)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
