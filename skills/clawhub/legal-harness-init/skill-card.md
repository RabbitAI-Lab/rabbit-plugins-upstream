## Description:

面向法律工作者初始化或增量治理 AGENTS.md/CLAUDE.md：识别当前 AI harness，区分用户级、项目级和团队级指令，生成最小法律安全基线，安全合并受管区块，并在新会话中验证权限、保密、信息缺口和回溯行为。

This skill is ready for commercial/non-commercial use.

## Publisher:

[cat-xierluo](https://clawhub.ai/user/cat-xierluo)

### License/Terms of Use:

MIT

## Use Case:

Legal professionals, legal operations teams, compliance teams, and developers supporting legal workflows use this skill to create or update persistent AGENTS.md/CLAUDE.md harness instructions with legal safety, privacy, traceability, and verification controls.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can modify persistent AGENTS.md/CLAUDE.md instruction files that affect future agent behavior across projects.

Mitigation: Use --dry-run first, inspect every proposed diff, and only apply managed-block changes after confirming the target path and privacy mode.

Risk: Legal matter details, credentials, or sensitive identifiers could be exposed if users place them directly into persistent harness files.

Mitigation: Use the strict privacy mode by default, avoid real case facts and credentials in AGENTS.md/CLAUDE.md, and keep sensitive facts in approved local or team-controlled stores.

Risk: Evidence reports that the advertised restore path failed in local Linux testing, so recovery behavior may not be reliable in every environment.

Mitigation: Verify backup and restore behavior on the intended operating system before relying on the generated configuration for active legal workflows.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/cat-xierluo/skills/legal-harness-init)
- [Project homepage](https://github.com/cat-xierluo/legal-skills)
- [Harness detection reference](references/03-harness-detection.md)
- [Audit trail contract](references/06-audit-trail-contract.md)
- [Privacy and context reference](references/18-privacy-and-context.md)
- [Activation verification reference](references/19-activation-verification.md)
- [Team layering reference](references/20-team-layering.md)
- [Scripts usage guide](scripts/README.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and generated AGENTS.md/CLAUDE.md configuration blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce dry-run diffs, verification status labels, backup metadata, and JSON output from bundled shell scripts.]

## Skill Version(s):

0.3.0 (source: frontmatter, changelog, release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
