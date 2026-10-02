## Description:

Audits user-selected source code for comprehension cost and change risk, producing a red/amber/green report with file-and-line evidence.

This skill is ready for commercial/non-commercial use.

## Publisher:

[elisabeth15501](https://clawhub.ai/user/elisabeth15501)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to review explicitly selected source files for readability and maintainability, prioritize evidence-backed findings, and identify documented, scoped technical debt without editing source code.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workspace checklist can be replaced when the skill runs.

Mitigation: Review or back up an existing clean_code_checklist.html before using the skill.

Risk: Audit reports can include locations and findings from selected source files.

Mitigation: Select only intended files and review reports before sharing them.

Risk: The bilingual skill may produce output in a language the user does not prefer.

Mitigation: Specify the preferred report language when requesting an audit.

## Reference(s):

- [Clean Code Audit Sample](artifact/references/clean_code_audit_sample.md)
- [Code Smells Crosswalk](artifact/references/smells_crosswalk.md)

## Skill Output:

**Output Type(s):** [Markdown, HTML, Guidance]

**Output Format:** [Markdown audit report and interactive HTML checklist]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports cite file:line evidence and rate findings red, amber, or green; the reusable checklist is copied to the workspace root.]

## Skill Version(s):

1.2.0 (source: frontmatter and changelog, released 2026-09-30)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
