## Description:

Helps agents design repeatable test-data generation, masking, cleanup, and management workflows for QA and automated testing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kokxi](https://clawhub.ai/user/kokxi)

### License/Terms of Use:

MIT-0

## Use Case:

QA engineers, test automation developers, and data-focused testers use this skill to plan bulk test-data creation, safe masking of sensitive production-like data, cleanup routines, and traceable data-management practices.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated data or cleanup guidance could be applied to an unauthorized or production environment.

Mitigation: Require explicit authorization, confirm a non-production target, and verify backups or rollback before running inserts, deletes, API calls, or masking pipelines.

Risk: Use of production-derived data for testing could expose sensitive information if masking controls are incomplete.

Mitigation: Prefer synthetic data where possible, identify sensitive fields before use, and validate masking rules against approved privacy controls.

Risk: Database cleanup examples could delete unintended rows if executed without scope checks.

Mitigation: Preview affected row counts, use transactions for harmless validation, require clear test-data markers such as is_test, and consult a DBA when scope is uncertain.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/kokxi/skills/qa-test-data-engineering)

## Skill Output:

**Output Type(s):** [guidance, markdown, code, shell commands, configuration]

**Output Format:** [Markdown guidance with structured sections and inline SQL or code examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Expected outputs include traceable data strategies, generation approaches, masking rules, and management workflows.]

## Skill Version(s):

1.7.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
