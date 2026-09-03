## Description:

Compares two or more materials on the same topic or event before publication to identify mismatched numbers, product names, fact wording, terminology, source attributions, structural promises, and cross-platform expression drift.

This skill is ready for commercial/non-commercial use.

## Publisher:

[haiyangchenbj](https://clawhub.ai/user/haiyangchenbj)

### License/Terms of Use:

MIT-0

## Use Case:

Editorial, communications, product marketing, and publication teams use this skill to compare related drafts across formats and platforms before release. It produces a consistency audit report with severity ratings and unified wording recommendations while leaving original materials unchanged.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill needs access to the documents selected for comparison, which may include unpublished or sensitive publication materials.

Mitigation: Use it only on materials the agent is permitted to read, and avoid adding documents outside the intended audit scope.

Risk: Unified wording recommendations may be incorrect if the designated reference source is outdated or itself contains an error.

Mitigation: Review P0 and P1 recommendations with the responsible human owner before applying changes or publishing.

Risk: Complex embedded content such as charts or images with text may not be fully parsed.

Mitigation: Provide extracted text or request manual review for embedded visual claims before treating the audit as complete.

## Reference(s):

- [Consistency Checklist Reference](artifact/references/consistency-checklist.md)
- [Replay References](artifact/references/replay-references.md)
- [ClawHub Skill Page](https://clawhub.ai/haiyangchenbj/skills/cross-material-consistency-auditor-skill)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, guidance]

**Output Format:** [Markdown audit reports, Markdown diff matrices, JSON claim extraction, and JSON unified wording records]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only analysis; original source materials are not modified.]

## Skill Version(s):

1.0.4 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
