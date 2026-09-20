## Description:

元真 yotta-humanize detects AI-flavored Chinese text with rule and statistics-based scoring, then provides deterministic rewrites to make writing read more naturally without changing facts or intent.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yottameta](https://clawhub.ai/user/yottameta)

### License/Terms of Use:

MIT

## Use Case:

Developers, writers, editors, and content teams use this skill to score Chinese drafts for AI-flavored wording, review matched patterns, and apply or inspect deterministic style rewrites before publishing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installer scripts copy the skill into a selected agent skills directory and the skill persists there until removed.

Mitigation: Use a pinned npm version or reviewed source checkout, review the installer target before using --dir or agent selection, and remove the installed skill when it is no longer needed.

Risk: Deterministic rewrites may change phrasing in ways that need author review.

Mitigation: Review rewrite output, fix lists, and suggestions before publishing, especially for judgment-heavy edits.

Risk: AI-flavor scores are style signals, not proof of a text's origin.

Mitigation: Treat scores as advisory and review the matched rules and context before making editorial or workflow decisions.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/yottameta/skills/yotta-humanize)
- [Project Homepage](https://github.com/YottaMeta/yotta-humanize)
- [24 类检测规则目录](references/patterns.md)
- [评分公式与统计量](references/scoring.md)
- [确定性改写规则](references/rewriting.md)
- [元真 FAQ / 避坑指南](references/faq.md)
- [元真复杂场景走查](references/walkthroughs.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Shell commands, Guidance]

**Output Format:** [Plain text, Markdown reports, and JSON CLI output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Deterministic rule-based scoring and rewriting for Chinese text; no model calls.]

## Skill Version(s):

0.2.1 (source: server release metadata, SKILL.md frontmatter, package.json, CHANGELOG.md)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
