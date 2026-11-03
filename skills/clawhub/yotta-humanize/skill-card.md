## Description:

分析中文草稿中的 AI 腔，并给出可逐项核对的确定性改写。

This skill is ready for commercial/non-commercial use.

## Publisher:

[yottameta](https://clawhub.ai/user/yottameta)

### License/Terms of Use:

MIT

## Use Case:

External writers, editors, and writing agents use this skill to assess and polish existing Chinese drafts, review detected patterns, and decide whether to apply suggested changes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Automatic rewrites can change quantities, certainty, or quotations despite the stated preservation promise.

Mitigation: Prefer analysis or suggestion mode; compare every proposed rewrite with the source and verify facts, figures, quotations, and technical terms before saving.

Risk: An unpinned npm installer command may fetch code outside the assessed release bundle.

Mitigation: Pin the installer to the reviewed version, choose one installation destination, preview with --dry-run, and retain customized installation files before upgrading.

## Reference(s):

- [Detection patterns](references/patterns.md)
- [Scoring method](references/scoring.md)
- [Rewrite behavior](references/rewriting.md)
- [FAQ](references/faq.md)
- [ClawHub skill page](https://clawhub.ai/yottameta/skills/yotta-humanize)
- [Project homepage](https://github.com/YottaMeta/yotta-humanize)
- [npm package](https://www.npmjs.com/package/@yottameta/yotta-humanize)

## Skill Output:

**Output Type(s):** [Analysis, Text, Markdown, JSON]

**Output Format:** [Plain text, Markdown reports, suggestions, or JSON, depending on the selected command]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Chinese text scoring and rule-based rewrite output may include a repair list and before/after scores.]

## Skill Version(s):

0.2.4 (source: frontmatter, CHANGELOG, package.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
