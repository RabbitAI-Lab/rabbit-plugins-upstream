## Description:

Compares multiple materials about the same topic or event before publication to find mismatched numbers, product names, fact wording, terminology, source attributions, structural promises, and cross-platform expression drift, then produces severity-rated audit artifacts and unified wording recommendations without modifying originals.

This skill is ready for commercial/non-commercial use.

## Publisher:

[haiyangchenbj](https://clawhub.ai/user/haiyangchenbj)

### License/Terms of Use:

MIT-0

## Use Case:

Editors, PR teams, product marketers, and content reviewers use this skill to compare drafts, press releases, slide decks, web pages, white papers, and social posts for consistency before publication. It supports human review by producing a diff matrix, an audit report, and source-grounded unified wording recommendations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill reads user-selected materials and writes audit artifacts to the selected output location.

Mitigation: Run it only on intended materials and review generated artifacts before sharing them.

Risk: Unified wording recommendations can affect publication decisions if applied without review.

Mitigation: Review P0/P1 findings and confirm source-grounded wording before making any edits outside the skill.

Risk: Embedded charts, images, or unreadable materials may not be fully comparable as text.

Mitigation: Treat unparseable content as a manual review item or provide extracted text before relying on the audit.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/haiyangchenbj/skills/cross-material-consistency-auditor-skill)
- [Consistency Checklist Reference](references/consistency-checklist.md)
- [Replay References](references/replay-references.md)
- [Audit Report Template](templates/audit-report.template.md)
- [Diff Matrix Template](templates/diff-matrix.template.md)
- [Unified Wording Template](templates/unified-wording.template.json)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Guidance]

**Output Format:** [Markdown audit report, Markdown diff matrix, JSON claim extraction, and JSON unified wording records]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only workflow; source materials are not modified automatically.]

## Skill Version(s):

1.0.3 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
