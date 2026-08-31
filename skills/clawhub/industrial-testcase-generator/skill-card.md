## Description:

Generates standardized industrial control and smart manufacturing test cases from requirements, producing structured Excel workbooks grouped by industrial module.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kokxi](https://clawhub.ai/user/kokxi)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, QA engineers, and industrial automation teams use this skill to turn PLC, DCS, SCADA, HMI, MES, protocol, alarm, redundancy, and industrial safety requirements into traceable test cases and coverage workbooks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated test cases and coverage claims may reflect assumptions made from incomplete industrial requirements.

Mitigation: Review requirements traceability, assumptions, standards coverage, and expected results before importing the workbook into a test management or QA workflow.

Risk: The skill may create local Excel files from user-provided requirement documents.

Mitigation: Run the Python/openpyxl output step in a controlled workspace and inspect generated files before sharing or using them for release decisions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/kokxi/skills/industrial-testcase-generator)
- [Industrial domain knowledge](references/domain-knowledge.md)
- [Industrial test case format specification](references/format-spec.md)
- [Example industrial requirements](examples/requirements.md)
- [Agent Skills standard](https://agentskills.io)
- [Agent Skills reference validation](https://github.com/agentskills/agentskills/tree/main/skills-ref)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance, files]

**Output Format:** [Markdown guidance with JSON intermediate structures and locally generated XLSX workbooks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Python 3 and openpyxl for Excel output; generated workbooks are saved locally under output/.]

## Skill Version(s):

1.1.0 (source: server release, metadata version V1.1.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
