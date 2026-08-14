## Description:

Export Codex CLI or Codex Desktop sessions to Markdown, HTML, or Obsidian notes with filtering, redaction, incremental export, interactive selection, session merging, and watch mode.

This skill is ready for commercial/non-commercial use.

## Publisher:

[sb679](https://clawhub.ai/user/sb679)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to locate Codex session logs and export selected conversations for review, sharing, documentation, or Obsidian note workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Exported transcripts may contain confidential prompts, local paths, command output, tokens, or other secrets.

Mitigation: Use --brief and --redact for external sharing, narrow the export with --since/--until, --grep, or --interactive, and manually review generated files before sending them.

Risk: Tool calls and tool outputs are included by default and may expose more local context than a plain conversation transcript.

Mitigation: Use --brief when only user and assistant messages are needed, and choose output paths deliberately before exporting or appending.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/sb679/skills/codex-export-more)
- [Development Notes](docs/DEVELOPMENT.md)
- [Publishing Notes](docs/PUBLISH.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, HTML, Files, Shell commands, Guidance]

**Output Format:** [Markdown, HTML, or Obsidian Markdown files with optional shell command snippets and status text.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports brief mode, redaction, time and keyword filters, interactive message selection, multi-session merging, incremental append, and watch mode.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
