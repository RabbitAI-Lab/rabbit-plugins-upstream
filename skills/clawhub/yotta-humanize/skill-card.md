## Description:

元真 yotta-humanize helps agents detect and reduce AI-flavored patterns in Chinese writing with deterministic rules, scoring, suggestions, and rewrites.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yottameta](https://clawhub.ai/user/yottameta)

### License/Terms of Use:

MIT

## Use Case:

Developers, writers, and agents use this skill to score, analyze, report on, suggest edits for, and deterministically rewrite Chinese text that contains common AI-style phrasing while preserving facts, names, quotes, and author intent.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installer commands may copy the skill into broader agent skill directories than intended.

Mitigation: Install only into skill directories you intend to modify, prefer a clear --agent target or npm/Node installer, and avoid broad global installs unless that scope is intended.

Risk: Rule-based rewrites can change wording without fully understanding context.

Mitigation: Review the fix list and rewritten text before use, especially for facts, data, proper nouns, quotes, tone, and cases where the tool provides suggestions instead of automatic rewrites.

Risk: AI-flavor scores are heuristic signals, not proof of text origin.

Mitigation: Use scores as review guidance and compare before/after reports rather than treating the score as a definitive authorship judgment.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/yottameta/skills/yotta-humanize)
- [npm package](https://www.npmjs.com/package/@yottameta/yotta-humanize)
- [FAQ](references/faq.md)
- [24 detection rules](references/patterns.md)
- [Scoring formula and statistics](references/scoring.md)
- [Deterministic rewriting rules](references/rewriting.md)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, guidance]

**Output Format:** [Plain text, Markdown reports, and optional JSON emitted by CLI commands.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Deterministic rule-based output; score --gate can return exit code 1 when the configured threshold is met.]

## Skill Version(s):

0.1.3 (source: frontmatter, package.json, CHANGELOG, release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
