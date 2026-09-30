## Description:

Reviews research and intelligence reports for traceable sources, bounded conclusions, counterevidence, source interests, and reproducible verification.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhaoxinghua09-cell](https://clawhub.ai/user/zhaoxinghua09-cell)

### License/Terms of Use:

All Rights Reserved

## Use Case:

Researchers, analysts, and reviewers use this skill to check reports before publication, identify unsupported claims, and request evidence or independent verification.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Release and artifact licensing labels conflict, and the documentation reserves rights in its text.

Mitigation: Confirm the publisher's applicable terms before reproducing or distributing the skill text.

Risk: Broad trigger keywords may activate this review workflow unintentionally alongside other skills.

Mitigation: Narrow activation terms or invoke the skill explicitly in multi-skill setups.

Risk: Self-review can overstate how well claims are supported by sources.

Mitigation: Check key claims against original sources and seek independent or human review before relying on a PASS verdict.

## Reference(s):

- [ClawHub release: research-quality-gate](https://clawhub.ai/zhaoxinghua09-cell/skills/research-quality-gate)
- [Calibration and stability log](artifact/calibration-log.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown review checklist and PASS/FAIL findings]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [PASS records checks and a brief verdict; FAIL lists issues, unmet checks, and suggested evidence, with verification pointers for cited conclusions.]

## Skill Version(s):

1.0.3 (source: ClawHub release; artifact frontmatter: 1.7.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
