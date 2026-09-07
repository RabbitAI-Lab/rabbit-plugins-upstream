## Description:

QA 测试技能集 helps agents turn PRDs, requirement documents, or URLs into traceable QA test cases, coverage reports, risk areas, and test reports through a structured QA workflow.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kokxi](https://clawhub.ai/user/kokxi)

### License/Terms of Use:

MIT-0

## Use Case:

QA engineers, developers, and agents use this skill to analyze requirement inputs and generate structured test cases with coverage reporting, risk areas, and traceability. It is intended for requirement-driven QA planning across functional, boundary, combination, regression, and optional specialized testing flows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can auto-trigger broadly and read local requirement trees or fetch URLs without a clear consent step.

Mitigation: Use it in a limited project workspace, review referenced paths and links before execution, and require confirmation before URL fetches or directory traversal.

Risk: The skill has access to Bash and document-reading tools during a QA workflow.

Mitigation: Install only when comfortable with those tool permissions, and narrow triggers or tool access where the host agent supports policy controls.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/kokxi/skills/qa-test-skills)
- [Input Routing Rules](references/routing.md)
- [Workflow Detail](references/workflow-detail.md)
- [Output Format Guide](references/format.md)
- [Enforcement Requirements](references/enforcement.md)
- [Depth Benchmarks](references/depth-benchmarks.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, CSV, Guidance]

**Output Format:** [Markdown reports and RFC 4180 CSV test-case files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes test-case IDs, requirement and scenario traceability, coverage reporting, risk areas, and final test report artifacts.]

## Skill Version(s):

1.7.6 (source: server release metadata; artifact frontmatter says 1.7.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
