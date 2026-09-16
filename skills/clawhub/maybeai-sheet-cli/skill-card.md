## Description:

Guides agents in using the mbs CLI to inspect, import, edit, verify, export, and share MaybeAI spreadsheets.

This skill is ready for commercial/non-commercial use.

## Publisher:

[no7dw](https://clawhub.ai/user/no7dw)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and spreadsheet automation agents use this skill to choose safe MaybeAI spreadsheet workflows, discover supported mbs commands at runtime, and generate command sequences or configuration for reads, writes, imports, formulas, SQL, dashboards, and sharing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A MaybeAI API token can authorize workbook changes, deletion, sharing, and editor grants.

Mitigation: Use a restricted token where possible, review the exact target, and require explicit confirmation before destructive or access-changing operations.

Risk: Unpinned or mismatched maybeai-sheet-cli versions can change the command surface or semantics.

Mitigation: Pin and verify the mbs version before use, then rely on local runtime help for supported commands and flags.

Risk: Local-file imports and command execution may expose unrelated workspace files or environment secrets.

Mitigation: Run the skill in a constrained workspace and avoid exposing unrelated secrets in the environment.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/no7dw/skills/maybeai-sheet-cli)
- [Project homepage](https://github.com/OmniMCP-AI/maybeai-uni)
- [README](artifact/README.md)
- [Skill definition](artifact/SKILL.md)
- [CLI Command Reference](artifact/references/cli-commands.md)
- [Read/Write Reference](artifact/references/read-write.md)
- [File Management Reference](artifact/references/file-management.md)
- [Formulas and SQL Reference](artifact/references/formulas-sql.md)
- [Permission And Sharing Reference](artifact/references/permission-sharing.md)
- [Errors and Recovery Reference](artifact/references/errors-recovery.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Code, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires MAYBEAI_API_TOKEN and the maybeai-sheet-cli mbs command; generated commands should be checked against local runtime help before execution.]

## Skill Version(s):

v0.21.8 (source: artifact/SKILL.md frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
