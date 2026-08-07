## Description:

Detects and rewrites Chinese web-fiction passages to reduce AI-like phrasing while preserving plot, character intent, and narrative function.

This skill is ready for commercial/non-commercial use.

## Publisher:

[worldwonderer](https://clawhub.ai/user/worldwonderer)

### License/Terms of Use:

MIT-0

## Use Case:

External authors and writing agents use this skill to audit and polish Chinese web-fiction drafts for AI-like phrasing. It can produce a detection report, rewrite affected passages, and run local style checks for file-based drafts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: File-mode polishing may rewrite the story files supplied by the user.

Mitigation: Use detection-only mode when a report is enough, and keep drafts in version control or backups before allowing rewrites.

## Reference(s):

- [story-deslop on ClawHub](https://clawhub.ai/worldwonderer/skills/story-deslop)
- [anti-ai-writing.md](references/anti-ai-writing.md)
- [banned-words.md](references/banned-words.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown reports and rewritten Chinese prose, with optional shell commands for local checks.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May read or rewrite user-specified draft files when used in file mode.]

## Skill Version(s):

1.1.14 (source: server release metadata; artifact frontmatter reports 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
