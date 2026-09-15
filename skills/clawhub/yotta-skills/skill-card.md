## Description:

元阁 yotta-skills helps agents route tasks across the YottaMeta skill family, inventory installed skills, and install or update selected yotta-* skills with explicit user confirmation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yottameta](https://clawhub.ai/user/yottameta)

### License/Terms of Use:

MIT

## Use Case:

Developers and agent operators use this skill to inspect the YottaMeta skill family, choose skill combinations for a task, and install, update, inventory, or route skills in local agent environments.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can fetch packages and change local agent skill directories with the user's privileges.

Mitigation: Install only from trusted YottaMeta/npm sources, avoid running as root or administrator, prefer pinned or locally reviewed versions, and review package lifecycle scripts before sensitive use.

Risk: Automatic updates, range-based installs, skipped scans, custom registry/npm flags, and verifier overrides can reduce installation assurance.

Mitigation: Use the default pinned workflow for normal installs, reserve update --auto, --range, --skip-scan, and override flags for reviewed cases, and keep verifier gate, dry-run, doctor, and rollback checks in the workflow.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/yottameta/skills/yotta-skills)
- [README](README.md)
- [Orchestration guide](references/orchestration.md)
- [Install flow](references/install-flow.md)
- [Skill list](references/skill-list.md)
- [FAQ](references/faq.md)
- [Tutorial](references/tutorial.md)
- [npm package](https://www.npmjs.com/package/@yottameta/yotta-skills)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown, plain text, and JSON-capable CLI output with inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include route recommendations, install or update commands, inventory summaries, hook evaluation results, and local status or rollback guidance.]

## Skill Version(s):

0.19.3 (source: frontmatter, package.json, release evidence; released 2026-09-13)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
