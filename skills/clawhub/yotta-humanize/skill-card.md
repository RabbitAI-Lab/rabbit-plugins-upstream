## Description:

元真 yotta-humanize helps agents detect AI-like patterns in Chinese writing, score the text, and apply deterministic rewrites for common cliches, jargon, chat residue, and punctuation issues.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yottameta](https://clawhub.ai/user/yottameta)

### License/Terms of Use:

MIT

## Use Case:

External users, developers, and writing teams use this skill to review Chinese drafts for AI-like style markers, generate score or analysis reports, and apply or inspect deterministic rewrite suggestions while preserving the author's facts and intent.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installer commands can copy the skill into multiple agent skill directories.

Mitigation: Install only to the intended agent or explicit directory, review the destination path first, and avoid global or no-argument installation unless that scope is intended.

Risk: Mechanical rewrites may alter tone or wording in ways the author does not want.

Mitigation: Review the fix list and rewritten text before publication, especially for factual, legal, brand, or quoted material.

Risk: A high AI-flavor score is a style signal, not proof of text origin.

Mitigation: Use scores and findings as editing guidance rather than as a definitive authorship judgment.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/yottameta/skills/yotta-humanize)
- [24 detection rule classes](references/patterns.md)
- [Scoring formula and statistics](references/scoring.md)
- [Deterministic rewrite rules](references/rewriting.md)
- [FAQ and usage boundaries](references/faq.md)

## Skill Output:

**Output Type(s):** [text, markdown, json, shell commands, guidance]

**Output Format:** [Plain text, Markdown reports, JSON analysis, and rewritten Chinese text with fix lists]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return before-and-after scores, rule findings, contextual snippets, prioritized suggestions, and CI-style gate exit codes.]

## Skill Version(s):

0.1.4 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
