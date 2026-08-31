## Description:

Generates structured QA test cases from requirement documents through a 12-step workflow covering functional testing, boundary analysis, combination testing, regression strategy, AI review, coverage reporting, and traceability.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kokxi](https://clawhub.ai/user/kokxi)

### License/Terms of Use:

MIT-0

## Use Case:

QA engineers, developers, and product teams use this skill to turn PRDs, uploaded requirement documents, or requirement URLs into traceable test cases, coverage reports, risk areas, and final test reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may read requirement documents, linked subdocuments, and URLs broadly.

Mitigation: Run it in a limited workspace, review requirement files and link targets before use, and avoid broad or sensitive directories unless explicitly intended.

Risk: Generated coverage claims can be misleading when the provided requirements are incomplete.

Mitigation: Treat coverage as scoped to existing requirement evidence and require missing modules or undefined flows to be listed as gaps.

## Reference(s):

- [Routing Rules](references/routing.md)
- [Output Format](references/format.md)
- [Enforcement Requirements](references/enforcement.md)
- [Depth Benchmarks](references/depth-benchmarks.md)
- [Workflow Detail](references/workflow-detail.md)

## Skill Output:

**Output Type(s):** [text, markdown, CSV, guidance]

**Output Format:** [Markdown reports and RFC 4180 CSV test cases]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Test cases include stable IDs, requirement traceability, scenario traceability, priority, expected results, risk level, and coverage scoped to the provided requirements.]

## Skill Version(s):

1.7.5 (source: SKILL.md frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
