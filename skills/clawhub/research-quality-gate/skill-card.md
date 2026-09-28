## Description:

Reviews research and intelligence reports for traceable sources, appropriately bounded conclusions, counterevidence, source interests, and reproducible claims.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhaoxinghua09-cell](https://clawhub.ai/user/zhaoxinghua09-cell)

### License/Terms of Use:

All rights reserved (skill text); code-only MIT terms do not apply to this documentation-only package

## Use Case:

Researchers, analysts, and their agents use this skill to check a report's evidence trail before delivery. It returns a pass checklist or a list of unsupported claims and requested evidence, rather than rewriting the report.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad activation keywords may invoke the quality gate for unrelated requests.

Mitigation: Limit activation to explicit research-report review tasks.

Risk: The skill is Chinese-first and may be misapplied by readers who cannot review its instructions.

Mitigation: Review the instructions with a qualified Chinese-language reader before deployment.

Risk: The listed license conflicts with the package's reserved-rights notice for its text.

Mitigation: Confirm permission before publishing or redistributing the skill text.

Risk: Self-assessed report quality can overstate the share of claims grounded in source material.

Mitigation: Have a person independently check consequential claims against original sources.

## Reference(s):

- [Research Quality Gate on ClawHub](https://clawhub.ai/zhaoxinghua09-cell/skills/research-quality-gate)
- [Calibration log (publisher-provided)](artifact/calibration-log.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown checklist or issue list]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [PASS or FAIL verdict with evidence pointers and suggested follow-up for failed checks]

## Skill Version(s):

1.0.2 (source: ClawHub release; artifact frontmatter says 1.7.1, manifest says 1.7.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
