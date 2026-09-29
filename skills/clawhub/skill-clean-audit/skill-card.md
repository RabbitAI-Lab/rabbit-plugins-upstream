## Description:

Audits user-selected WorkBuddy skill scripts and Python code for comprehension cost and change risk, producing an evidence-backed, red/amber/green maintainability report without editing the code.

This skill is ready for commercial/non-commercial use.

## Publisher:

[elisabeth15501](https://clawhub.ai/user/elisabeth15501)

### License/Terms of Use:

MIT-0

## Use Case:

Developers audit their own WorkBuddy skill scripts or Python code for readability and maintainability, using file-and-line evidence to prioritize incremental cleanup.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Audit findings or cleanup priorities may be inaccurate or misleading.

Mitigation: Check each file-and-line citation against the code and review recommendations before making changes.

Risk: Generated report and checklist files are written to the current workspace.

Mitigation: Review the output paths and generated contents before sharing or retaining the files.

## Reference(s):

- [Clean code audit sample](references/clean_code_audit_sample.md)
- [Code smells crosswalk](references/smells_crosswalk.md)
- [ClawHub skill listing](https://clawhub.ai/elisabeth15501/skills/skill-clean-audit)

## Skill Output:

**Output Type(s):** [Markdown, HTML]

**Output Format:** [Markdown audit report and reusable HTML checklist]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports cite file and line evidence, score findings red/amber/green, and are saved with the checklist in the current workspace.]

## Skill Version(s):

1.1.1 (source: frontmatter, CHANGELOG, ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
