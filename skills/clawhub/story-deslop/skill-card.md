## Description:

story-deslop helps an agent detect and reduce AI-style patterns in Chinese web-novel drafts while preserving plot, character intent, and narrative function.

This skill is ready for commercial/non-commercial use.

## Publisher:

[worldwonderer](https://clawhub.ai/user/worldwonderer)

### License/Terms of Use:

MIT-0

## Use Case:

Writers and editing agents use this skill to review Chinese fiction for formulaic AI-writing patterns, produce a concise AI-flavor report, and rewrite affected passages when requested. In file mode it can edit manuscript files directly; in detect-only mode it reports issues without rewriting.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: File mode can rewrite manuscript files.

Mitigation: Use explicit detect-only wording when only a report is wanted, and keep version control or backups before allowing file edits.

Risk: Style rewrites can accidentally remove plot, character, or continuity details.

Mitigation: Review diffs for preserved narrative function, especially when deletion limits or [需复核] markers are reported.

Risk: AI-flavor findings may be mistaken for objective authorship or detector-score claims.

Mitigation: Treat findings as style-editing guidance only; do not present the output as a guarantee such as 0% AI or 100% human.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/worldwonderer/skills/story-deslop)
- [OpenClaw source metadata](https://github.com/worldwonderer/oh-story-claudecode)
- [Anti-AI writing guide](references/anti-ai-writing.md)
- [Banned words and patterns](references/banned-words.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown reports, edited prose, and inline shell commands for deterministic checks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May write changes to manuscript files in file mode; detect-only requests should produce reports without file edits.]

## Skill Version(s):

1.1.16 (source: ClawHub release evidence; artifact frontmatter says 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
