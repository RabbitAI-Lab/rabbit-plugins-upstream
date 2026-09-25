## Description:

Compares two or more materials on the same topic before publication to identify mismatched numbers, product names, fact wording, terminology, source attributions, structural promises, and cross-platform expression drift.

This skill is ready for commercial/non-commercial use.

## Publisher:

[haiyangchenbj](https://clawhub.ai/user/haiyangchenbj)

### License/Terms of Use:

MIT-0

## Use Case:

Editorial, PR, product, and localization teams use this skill to compare related materials before publication and produce a consistency audit with severity-rated differences and recommended unified wording.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated P0/P1 recommendations may be incomplete or incorrect for publication-critical materials.

Mitigation: Review the audit report and unified wording recommendations before editing or publishing source materials.

Risk: Embedded charts, images, or unreadable files may not be fully compared.

Mitigation: Provide extracted text or perform a manual check for complex embedded content that the skill flags as unparseable.

Risk: A wrong or outdated reference source can lead to incorrect unified wording.

Mitigation: Confirm the designated reference source and resolve obvious reference-source errors before applying recommendations.

## Reference(s):

- [Consistency Checklist Reference](artifact/references/consistency-checklist.md)
- [Replay References](artifact/references/replay-references.md)
- [ClawHub skill page](https://clawhub.ai/haiyangchenbj/skills/cross-material-consistency-auditor-skill)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Guidance]

**Output Format:** [Markdown reports and JSON files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only audit outputs; original materials are not modified.]

## Skill Version(s):

1.0.6 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
