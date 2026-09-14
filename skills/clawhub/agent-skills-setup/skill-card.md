## Description:

Use when a user wants to migrate, back up, restore, compare, or move AI-coding-agent context across Cursor, Claude Code, Codex, Cline, Copilot, Windsurf, Gemini CLI, or another supported profile, including switching computers.

This skill is ready for commercial/non-commercial use.

## Publisher:

[luckycat133](https://clawhub.ai/user/luckycat133)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to plan, preview, apply, verify, back up, restore, and compare agent context across supported AI coding tools. It focuses on reviewed skills, instructions, rules, and MCP configuration with secret redaction, rollback, and offline operation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Rollback can delete or replace user-writable files when run with an untrusted manifest.

Mitigation: Run rollback only with a manifest that was just generated and verified locally.

Risk: Broad all-installed operations can affect more agent context than intended.

Mitigation: Use plan-only mode first and review exact source and target paths before applying.

Risk: Bundles and manifests can act as sensitive local control files.

Mitigation: Treat bundles and manifests as sensitive artifacts and verify them before restore or rollback.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/luckycat133/skills/agent-skills-setup)
- [IDE registry](references/ide-registry.md)
- [Registry v2](references/registry-v2.json)
- [Migration safety](references/migration-safety.md)
- [MCP migration](references/mcp-migration.md)
- [Object migration](references/object-migration.md)
- [Verification](references/verification.md)
- [Documentation freshness checks](references/doc-freshness-checks.json)
- [Agent Skills specification](https://raw.githubusercontent.com/agentskills/agentskills/main/docs/specification.mdx)
- [Cursor rules documentation](https://docs.cursor.com/context/rules)
- [Claude Code skills documentation](https://code.claude.com/docs/en/skills)
- [GitHub Copilot CLI documentation](https://docs.github.com/en/copilot/how-tos/copilot-cli)
- [Gemini CLI skills documentation](https://github.com/google-gemini/gemini-cli/blob/main/docs/skills.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands, paths, JSON plans, manifests, and verification summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Offline workflow; writes require reviewed plans and explicit consent.]

## Skill Version(s):

0.9.3 (source: frontmatter and ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
