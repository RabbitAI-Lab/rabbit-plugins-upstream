## Description:

元阁 yotta-skills routes agent tasks to YottaMeta skill combinations, lists and inventories installed skills, and provides a one-command installer/updater with pre-install checks and runtime hook adaptation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yottameta](https://clawhub.ai/user/yottameta)

### License/Terms of Use:

MIT

## Use Case:

Developers and agent operators use this skill to decide which YottaMeta skills fit a task, inspect installed skills, and install or update selected skills after user confirmation. It is useful for managing skill-family deployments across supported agent environments without bundling the individual skill bodies.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Downloaded verifier, setup, and doctor code can run with the user's privileges during installation or health checks.

Mitigation: Install only trusted YottaMeta packages, keep pinned versions enabled, and review package-provided lifecycle behavior before approving execution.

Risk: The installer can modify agent skill directories and maintain local state under ~/.yottaskills.

Mitigation: Use dry-run and route outputs to preview changes, choose the target agent or directory explicitly, and keep snapshots available for rollback.

Risk: Using --range or --skip-scan can reduce reproducibility or bypass normal verification.

Mitigation: Prefer the default pinned install mode and reserve --range or --skip-scan for reviewed, intentional exceptions.

Risk: MCP configuration or global-memory writes can change agent behavior beyond a single command.

Mitigation: Approve those writes only after reviewing the target path, exact content, and expected effect.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/yottameta/skills/yotta-skills)
- [npm package](https://www.npmjs.com/package/@yottameta/yotta-skills)
- [Orchestration guide](references/orchestration.md)
- [Install flow](references/install-flow.md)
- [Skill list](references/skill-list.md)
- [Tutorial](references/tutorial.md)
- [FAQ](references/faq.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown text, command examples, and optional JSON from CLI or MCP commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include candidate skill combinations, confidence, evidence, installed or missing status, install commands, inventory results, hook decisions, and local configuration snippets.]

## Skill Version(s):

0.19.5 (source: frontmatter, package.json, CHANGELOG, release evidence; released 2026-09-15)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
