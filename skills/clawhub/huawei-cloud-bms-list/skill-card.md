## Description:

Queries Huawei Cloud BMS (Bare Metal Server) instances for the current tenant or project and returns names, IDs, and statuses, with optional status, name, pagination, and SDK fallback support.

This skill is ready for commercial/non-commercial use.

## Publisher:

[erickeyhu-hug](https://clawhub.ai/user/erickeyhu-hug)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and cloud operators use this skill to inspect Huawei Cloud BMS inventory for a tenant or project, including name lists, status checks, filtered queries, pagination, and cost or daily review workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The agent may receive read-only visibility into Huawei Cloud BMS names, IDs, and statuses.

Mitigation: Confirm that this inventory visibility is acceptable before installation and grant only the least-privilege `bms:servers:list` IAM permission when possible.

Risk: Credentials could be exposed if AK/SK values are hardcoded or shared through edited test inputs.

Mitigation: Use environment variables or authenticated CLI profiles, do not hardcode AK/SK credentials, and review `test-vars.json` before running tests.

Risk: Broad trigger wording or edited test scripts could cause unintended queries or execution with untrusted values.

Mitigation: Confirm list-only BMS intent and region before execution, and avoid running the included test script with untrusted environment variables or modified test values.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/erickeyhu-hug/skills/huawei-cloud-bms-list)
- [IAM Policies](references/iam-policies.md)
- [CLI Installation Guide](references/cli-installation-guide.md)
- [Verification Method](references/verification-method.md)
- [Dataflow Diagram](references/dataflow-diagram.md)
- [Acceptance Criteria](references/acceptance-criteria.md)

## Skill Output:

**Output Type(s):** [Shell commands, API Calls, Markdown, Guidance]

**Output Format:** [Markdown guidance with bash commands and JSON query results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only output focused on BMS names, IDs, statuses, counts, and name-only lists.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
