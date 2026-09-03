## Description:

Pressure-test a rule, decision table, SOP, requirement, or business process by finding material edge cases and alternative branches that could break a happy-path specification before automation or formalization.

This skill is ready for commercial/non-commercial use.

## Publisher:

[raguets](https://clawhub.ai/user/raguets)

### License/Terms of Use:

MIT-0

## Use Case:

Employees, developers, and process owners use this skill to identify material non-happy-path branches in rules, SOPs, requirements, and business processes before automating or formalizing them.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The agent may inspect task-provided documents while resolving discoverable facts for an exception analysis.

Mitigation: Attach only documents relevant to the process being reviewed and avoid providing unrelated sensitive material.

## Reference(s):

- [Exception Lenses](references/exception-lenses.md)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Markdown table with concise follow-up sections]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Expected table columns: Condition, Expected path, Exception path, Status, and Evidence / decision needed.]

## Skill Version(s):

1.0.0 (source: server release metadata; artifact frontmatter metadata.version is 0.1.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
