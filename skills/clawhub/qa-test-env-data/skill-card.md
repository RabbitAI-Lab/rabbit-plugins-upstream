## Description:

Helps QA and engineering teams manage non-production test environments and test data by producing environment health checks, environment requirements, design guidance, configuration guidance, maintenance plans, and data preparation checklists.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kokxi](https://clawhub.ai/user/kokxi)

### License/Terms of Use:

MIT-0

## Use Case:

QA practitioners, developers, and DevOps engineers use this skill when test environments are unstable, insufficient, or need prepared data. It supports environment deployment and configuration management, health checks, issue triage, multi-environment planning, and routine test data preparation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Environment restarts, repairs, or configuration changes could affect the wrong or shared environment.

Mitigation: Use only authorized non-production environments, verify the exact target environment name or address, obtain explicit approval, coordinate shared-environment windows, and record the operation.

Risk: Data cleanup, reset, or archival guidance could remove data needed for testing or team workflows.

Mitigation: Confirm backups before changes, prefer dry runs in low-risk environments, start with a small scope, and verify results before broader cleanup.

Risk: Environment issues may be mistaken for code defects, or code defects may be hidden by unstable dependencies.

Mitigation: Run the environment health checklist across services, databases, caches, message queues, dependencies, network, configuration, and data readiness before remediation.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/kokxi/skills/qa-test-env-data)

## Skill Output:

**Output Type(s):** [Markdown, Configuration, Shell commands, Guidance]

**Output Format:** [Markdown checklists, tables, and structured guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include environment IDs, environment requirements, environment design, configuration guidance, maintenance plans, and data preparation or cleanup checklists.]

## Skill Version(s):

1.7.5 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
