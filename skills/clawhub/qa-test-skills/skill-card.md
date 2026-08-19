## Description:

Automatically generates structured test cases from requirement documents by coordinating requirement review, risk analysis, scenario design, boundary and combination testing, regression planning, AI output critique, and reporting.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kokxi](https://clawhub.ai/user/kokxi)

### License/Terms of Use:

MIT-0

## Use Case:

QA engineers, developers, and product teams use this skill to turn PRDs, requirement files, or requirement URLs into traceable test cases, coverage reports, risk areas, and test reports. It is intended for functional, boundary, combination, regression, API, mobile, agent, performance, security, and exploratory testing workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may automatically read provided requirement files or referenced requirement documents.

Mitigation: Run it in a controlled workspace and avoid pointing it at sensitive unrelated directories.

Risk: The skill can fetch supplied URLs during requirement intake.

Mitigation: Review links before invocation and avoid internal or confidential URLs unless that access is intended.

Risk: Broad trigger phrases may start the workflow with limited user confirmation.

Mitigation: Invoke it only for intended QA generation tasks and review generated reports and CSV files before using them in a release process.

## Reference(s):

- [ClawHub qa-test-skills page](https://clawhub.ai/kokxi/skills/qa-test-skills)
- [Workflow overview](SKILL.md)
- [Enforcement requirements](references/enforcement.md)
- [Input routing rules](references/routing.md)
- [Output format guide](references/format.md)
- [Workflow detail](references/workflow-detail.md)
- [Depth benchmarks](references/depth-benchmarks.md)

## Skill Output:

**Output Type(s):** [text, markdown, configuration, guidance, files]

**Output Format:** [Markdown reports and RFC 4180 CSV test case files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Final CSV output is expected to use UTF-8 with BOM and the fixed columns: case ID, test type, module, title, priority, preconditions, steps, expected result, and risk level.]

## Skill Version(s):

1.7.0 (source: server evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
