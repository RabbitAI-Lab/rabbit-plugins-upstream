## Description:

Use this skill when a bug recurs, a production defect needs post-incident analysis, or a recurring issue needs a systemic fix; it guides agents from symptoms through 5 Why, cause-and-effect, and fishbone-style analysis to distinguish direct, indirect, and systemic causes and improve test design.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kokxi](https://clawhub.ai/user/kokxi)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, QA engineers, and incident reviewers use this skill to analyze recurring software defects, map symptoms to likely technical causes, validate root-cause hypotheses, and propose fixes and prevention measures.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Bug investigation inputs may contain production logs, customer identifiers, payment details, screenshots, financial records, or other sensitive data.

Mitigation: Use the skill in controlled environments and redact or mask sensitive data before sharing inputs.

Risk: The skill may suggest bash commands or local diagnostic steps that touch logs, monitoring tools, or workspace files.

Mitigation: Review commands before execution and run them only against approved systems and data.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/kokxi/skills/qa-bug-root-cause-analysis)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown with structured root-cause analysis, tables, checklists, and optional shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include root-cause IDs, contributing factors, impact assessment, fix suggestions, prevention measures, and test-design improvements.]

## Skill Version(s):

1.7.5 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
