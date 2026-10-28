## Description:

Build, audit, and repair web content against WCAG 2.2. Use when: (1) creating accessible HTML/CSS/JS, (2) remediating accessibility defects, (3) running reproducible automated audits, (4) preparing WCAG 2.2 AAA evidence and human-test records, or (5) running the optional AI-WCAG-Gauntlet benchmark.

This skill is ready for commercial/non-commercial use.

## Publisher:

[turbolego](https://clawhub.ai/user/turbolego)

### License/Terms of Use:

MIT

## Use Case:

Web developers and accessibility specialists use this skill to build accessible pages, identify and fix WCAG 2.2 issues, and document automated and manual test evidence. It supports baseline, AA, and AAA work while requiring human review and interaction testing for claims that automated tools cannot establish.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Chrome may run without its sandbox in some audit environments.

Mitigation: Use isolated CI workers when the sandbox is disabled, or keep it enabled with the documented override.

Risk: Saved HTML and audit reports may include content from private pages.

Mitigation: Protect saved HTML and reports from unauthorized access.

Risk: Dependency changes can affect audit behavior.

Mitigation: Select dependency versions explicitly.

## Reference(s):

- [WCAG 2.2 Quick Reference](https://www.w3.org/WAI/WCAG22/quickref/)
- [Validator workflow](references/validator-workflow.md)
- [AAA evidence matrix](references/aaa-evidence-matrix.md)
- [Manual test protocol](references/manual-test-protocol.md)
- [Dynamic-state test protocol](references/dynamic-state-test-protocol.md)

## Skill Output:

**Output Type(s):** [Guidance, Analysis, Code, Shell commands]

**Output Format:** [Markdown guidance, code snippets, shell commands, and accessibility audit reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include HTML, CSS, or JavaScript changes and automated findings or manual test evidence.]

## Skill Version(s):

2.0.20 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
