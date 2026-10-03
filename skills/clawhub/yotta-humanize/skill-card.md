## Description:

Detects formulaic patterns in Chinese writing and suggests or applies rule-based edits to make the text read more naturally.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yottameta](https://clawhub.ai/user/yottameta)

### License/Terms of Use:

MIT-0

## Use Case:

Writers, editors, and agents use this skill to check Chinese drafts for formulaic AI-style language, review rewrite suggestions, and make mechanical edits while preserving facts and author intent.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The installer persists files in agent skill directories for future sessions.

Mitigation: Pin and review the npm package version; use --dry-run or --list before installation.

Risk: Rule-based edits or style scores may not reflect author intent or reliably establish a text's origin.

Mitigation: Review the revised text and score in context; preserve facts, quotations, and intended tone.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/yottameta/skills/yotta-humanize)
- [Project homepage](https://github.com/YottaMeta/yotta-humanize)
- [Detection rules](references/patterns.md)
- [Scoring method](references/scoring.md)
- [Rewriting rules](references/rewriting.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Guidance]

**Output Format:** [Plain text, Markdown reports, or JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [0–100 style score, pattern matches, rewrite suggestions, and rewritten text with a change list and before/after scores; optional CI threshold gate.]

## Skill Version(s):

0.2.2 (source: ClawHub release, frontmatter, package.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
