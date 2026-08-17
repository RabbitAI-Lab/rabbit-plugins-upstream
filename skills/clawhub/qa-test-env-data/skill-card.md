## Description:

This skill helps QA and engineering teams manage non-production test environments, distinguish environment issues from code issues, and prepare test data through health checks, configuration guidance, maintenance plans, and checklists.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kokxi](https://clawhub.ai/user/kokxi)

### License/Terms of Use:

MIT-0

## Use Case:

QA engineers, developers, and DevOps practitioners use this skill to plan and maintain authorized non-production test environments, troubleshoot environment instability, and prepare or clean test data for execution workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Environment cleanup, restart, or configuration guidance could affect the wrong system if the target is not confirmed.

Mitigation: Confirm the exact target identifier, verify it is an authorized non-production environment, and obtain required team approval before acting.

Risk: Data cleanup or reset guidance could remove useful test data or shared environment state.

Mitigation: Make or verify backups, prefer a dry run in a lower-risk environment, and scope bulk actions to a small validated set before expanding.

Risk: Changes in shared test environments can disrupt other teams' testing windows.

Mitigation: Coordinate shared-environment changes with affected teams and record approvals and operation logs.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/kokxi/skills/qa-test-env-data)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown checklists and structured guidance with occasional shell command suggestions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs include environment requirement lists, environment design plans, configuration guidance, maintenance plans, health-check checklists, and test-data preparation checklists.]

## Skill Version(s):

1.7.0 (source: release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
