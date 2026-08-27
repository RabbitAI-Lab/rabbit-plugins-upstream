## Description:

Yotta-humanize helps agents detect AI-like patterns in Chinese writing, score the text, produce reports and suggestions, and apply deterministic rewrites for clearer, more natural prose.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yottameta](https://clawhub.ai/user/yottameta)

### License/Terms of Use:

MIT

## Use Case:

Developers, editors, and agent users can use this skill to review Chinese drafts for AI-like wording, generate score or analysis reports, and produce deterministic cleanup suggestions or rewrites. It is intended for text-level style editing and does not create missing content or change facts, data, names, or quotations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The installer can copy the skill into multiple agent environments when used with broad installation options.

Mitigation: Prefer a specific --agent or --dir installation target and use global installation only when broad agent availability is intended.

Risk: The shell installer removes .git metadata inside the installed target.

Mitigation: Do not point --dir at an important existing yotta-humanize checkout or any location where preserving repository metadata matters.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/yottameta/skills/yotta-humanize)
- [Rule Pattern Reference](references/patterns.md)
- [Scoring Reference](references/scoring.md)
- [Rewriting Reference](references/rewriting.md)
- [npm Package](https://www.npmjs.com/package/@yottameta/yotta-humanize)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Shell commands, Guidance]

**Output Format:** [Plain text, Markdown reports, JSON CLI output, and rewrite suggestions.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Deterministic local Python 3.8+ processing with no model calls or external dependencies.]

## Skill Version(s):

0.1.1 (source: SKILL.md frontmatter, package.json, CHANGELOG)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
