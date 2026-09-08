## Description:

This skill helps QA teams design bulk test data generation, data masking, compliance checks, cleanup, and data-factory workflows for test environments.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kokxi](https://clawhub.ai/user/kokxi)

### License/Terms of Use:

MIT-0

## Use Case:

QA engineers and developers use this skill to plan traceable test-data construction, masking rules, data cleanup, lifecycle management, and repeatable data-factory practices. It is most relevant when teams need large volumes of test data or need to prepare production-derived data safely for test use.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Production-derived or sensitive data may be mishandled when preparing test data.

Mitigation: Use approved test environments, prefer synthetic data, validate masking before export, and follow documented permission requirements.

Risk: Generated SQL DELETE, API mutation, Docker, or Bash examples could alter data or systems if run without review.

Mitigation: Manually review commands before execution, confirm the target is a test environment, preview affected rows, and use transactions or DBA review for database cleanup.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/kokxi/skills/qa-test-data-engineering)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with structured sections, checklists, tables, and inline SQL, Python, Bash, or configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include DATA-XXXX traceability identifiers, data strategy, generation approach, masking rules, and data management process guidance.]

## Skill Version(s):

1.7.6 (source: server release metadata; artifact frontmatter says 1.7.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
