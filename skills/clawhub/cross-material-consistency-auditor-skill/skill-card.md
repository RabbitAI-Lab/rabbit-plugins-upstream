## Description:

Compares two or more materials on the same topic for consistency and produces severity-rated findings and unified wording recommendations without editing the originals.

This skill is ready for commercial/non-commercial use.

## Publisher:

[haiyangchenbj](https://clawhub.ai/user/haiyangchenbj)

### License/Terms of Use:

MIT-0

## Use Case:

PR, product, and editorial teams can compare related drafts or platform versions before publication. The skill highlights differences in figures, product names, wording, terminology, attribution, structure, and cross-platform expression, then prepares findings for human review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security scan was benign but partial and did not parse the manifest.

Mitigation: Review the package contents before deployment and treat the scan as one safety signal, not a guarantee.

Risk: A proposed unified wording could introduce an unsupported or misleading claim.

Mitigation: Tie recommendations to the designated or earliest authoritative source and obtain human confirmation before making edits.

Risk: Embedded charts, images, or other unreadable material may contain claims the audit cannot compare.

Mitigation: Mark unparseable content and request text extraction or manual review before relying on the comparison.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/haiyangchenbj/skills/cross-material-consistency-auditor-skill)
- [Consistency Checklist Reference](artifact/references/consistency-checklist.md)
- [Replay References](artifact/references/replay-references.md)
- [Audit Report Template](artifact/templates/audit-report.template.md)
- [Consistency Diff Matrix Template](artifact/templates/diff-matrix.template.md)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, JSON, Guidance]

**Output Format:** [Markdown audit reports and diff matrices, plus JSON extracted claims and unified wording recommendations]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Recommendations cite an authoritative source; originals remain unchanged pending human review.]

## Skill Version(s):

1.0.8 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
