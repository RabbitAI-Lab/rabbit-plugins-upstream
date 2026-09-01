## Description:

Generates standardized, traceable machine-vision test cases from requirements documents or descriptions, organized by vision module and delivered as structured Excel workbooks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kokxi](https://clawhub.ai/user/kokxi)

### License/Terms of Use:

MIT-0

## Use Case:

QA engineers, machine-vision engineers, and test leads use this skill to turn vision-system requirements into module-grouped Excel test-case workbooks with traceability, priority coloring, coverage statistics, and standard-compliance checks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated test cases may contain incorrect assumptions when source requirements are incomplete or ambiguous.

Mitigation: Review assumptions, expected results, and coverage statistics before using the workbook for acceptance testing or importing it into a test-management platform.

Risk: Generated Excel workbooks may be unsuitable for downstream test-management systems if local schema or field conventions differ.

Mitigation: Validate the workbook against the target platform's import rules and adjust mappings before bulk import.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/kokxi/skills/vision-testcase-generator)
- [Vision domain knowledge](references/domain-knowledge.md)
- [Vision test-case format specification](references/format-spec.md)
- [Example requirements](examples/requirements.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance, files]

**Output Format:** [Markdown planning and generated Excel workbook with test-case and coverage-statistics sheets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Excel output uses a fixed 15-column test-case schema, module separator rows, priority coloring, and coverage statistics.]

## Skill Version(s):

1.1.0 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
