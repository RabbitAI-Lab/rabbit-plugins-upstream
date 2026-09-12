## Description:

元真 yotta-humanize detects AI-flavored Chinese writing with rule and burstiness checks, then returns scores, reports, suggestions, and deterministic rewrites intended to preserve facts and meaning.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yottameta](https://clawhub.ai/user/yottameta)

### License/Terms of Use:

MIT

## Use Case:

Developers, writers, editors, and agents use this skill to check Chinese drafts for common AI-flavor patterns, generate Markdown or JSON reports, and apply deterministic text edits for clearer human-facing prose.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A custom installer destination can place files in an unintended agent skill directory.

Mitigation: Install only into the intended agent skill directory; prefer the npm installer or an explicit --agent or --dir target, and avoid pointing --dir at the source folder or its subfolders.

Risk: Deterministic replacements can still change tone or wording.

Mitigation: Review rewritten text, the fix list, and before-and-after scores before using the edited draft.

Risk: The AI-flavor score is an editing signal, not proof of authorship.

Mitigation: Use scores and reports to guide review rather than to make absolute claims about where the text came from.

## Reference(s):

- [24 类检测规则目录（patterns）](references/patterns.md)
- [评分公式与统计量（scoring）](references/scoring.md)
- [确定性改写规则（rewriting）](references/rewriting.md)
- [元真 FAQ / 避坑指南](references/faq.md)
- [元真复杂场景走查](references/walkthroughs.md)
- [npm package: @yottameta/yotta-humanize](https://www.npmjs.com/package/@yottameta/yotta-humanize)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Shell commands, Guidance]

**Output Format:** [Plain text, Markdown reports, and JSON from local CLI commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Deterministic local analysis and rewrite output; no model calls.]

## Skill Version(s):

0.2.0 (source: SKILL.md frontmatter, CHANGELOG.md, package.json, release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
