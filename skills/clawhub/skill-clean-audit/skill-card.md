## Description:

Audits user-selected Python code and WorkBuddy skill scripts for comprehension cost and change risk, producing a red/amber/green report backed by file-and-line evidence.

This skill is ready for commercial/non-commercial use.

## Publisher:

[elisabeth15501](https://clawhub.ai/user/elisabeth15501)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to review their own Python code or WorkBuddy skill scripts for readability and maintainability, prioritize evidence-backed findings, and document scoped technical debt without changing source code.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Audits read the local code supplied by the user and create report and checklist files in the workspace root.

Mitigation: Choose the target files deliberately and request inline-only output if workspace files are unwanted.

Risk: Some bundled audit guidance is Chinese-first and may not match the reader's preferred language.

Mitigation: Specify the preferred language when requesting the report.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/elisabeth15501/skills/skill-clean-audit)
- [Clean Code audit sample](references/clean_code_audit_sample.md)
- [Code smells crosswalk](references/smells_crosswalk.md)

## Skill Output:

**Output Type(s):** [Markdown, HTML, Guidance]

**Output Format:** [Evidence-backed Markdown audit report and interactive HTML checklist]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Creates clean_code_audit_<target>.md and clean_code_checklist.html in the workspace root; findings cite file:line locations.]

## Skill Version(s):

1.1.0 (source: frontmatter, ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
