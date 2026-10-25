## Description:

Build, audit, and repair web content against WCAG 2.2, including reproducible accessibility checks and AAA evidence preparation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[turbolego](https://clawhub.ai/user/turbolego)

### License/Terms of Use:

MIT

## Use Case:

Developers use this skill to build and remediate accessible web pages, run reproducible accessibility audits, and prepare manual test records and evidence for WCAG 2.2 targets.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Consequential form testing could trigger live transactions or change real data.

Mitigation: Use staging and synthetic data; separately authorize any live transaction or data change.

Risk: Browser-based CI audits may run without sufficient isolation.

Mitigation: Run CI audits in an isolated environment or retain Chrome sandboxing.

Risk: Referenced accessibility-tool dependencies may be unresolved because package manifests are absent.

Mitigation: Resolve and review dependency versions before installation.

## Reference(s):

- [WCAG 2.2 Quick Reference](https://www.w3.org/WAI/WCAG22/quickref/)
- [Validator workflow](references/validator-workflow.md)
- [AAA evidence matrix](references/aaa-evidence-matrix.md)
- [Manual test protocol](references/manual-test-protocol.md)

## Skill Output:

**Output Type(s):** [Guidance, Analysis, Code, Shell commands, Configuration, Files]

**Output Format:** [Markdown guidance, code examples, shell commands, and accessibility audit or test evidence]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include proposed accessibility changes and validation steps; human review is needed for conformance claims.]

## Skill Version(s):

2.0.14 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
