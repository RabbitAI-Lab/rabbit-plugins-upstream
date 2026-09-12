## Description:

Manage CloudRobo workspaces: create, list, show, update, and delete workspaces; manage workspace members; view workspace overview statistics; and switch the active workspace context for other CloudRobo skills.

This skill is ready for commercial/non-commercial use.

## Publisher:

[huaweiclouddev](https://clawhub.ai/user/huaweiclouddev)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and cloud operations engineers use this skill to administer Huawei Cloud CloudRobo workspace lifecycle, membership, quota overview, and active workspace context before running dataset, training, evaluation, or inference workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The included test script has a code-injection risk when workspace or user identifiers are untrusted.

Mitigation: Run the test script only in a clean environment with trusted WORKSPACE_ID, USER_ID, and ROLE_ID values, or review and harden the script before use.

Risk: Cloud credentials may be exposed if AK/SK values are stored in plaintext config or used with broad permissions.

Mitigation: Use least-privileged or temporary AK/SK credentials and store config files with owner-only permissions.

Risk: Disabling SSL verification can expose signed CloudRobo requests to interception.

Mitigation: Keep SSL verification enabled except for controlled debugging against trusted endpoints.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/huaweiclouddev/skills/huawei-cloud-cloudrobo-workspace)
- [CLI Installation Guide](references/cli-installation-guide.md)
- [IAM Policies](references/iam-policies.md)
- [API Paths](references/api-paths.md)
- [Workspace Config Reference](references/workspace-config-catalog.md)
- [Dataflow Diagram](references/dataflow-diagram.md)
- [Verification Method](references/verification-method.md)
- [Acceptance Criteria](references/acceptance-criteria.md)
- [Huawei Cloud API Explorer](https://console.huaweicloud.com/apiexplorer/)
- [CloudRobo service endpoint pattern](https://cloudrobo.{region}.myhuaweicloud.com)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, code, markdown]

**Output Format:** [Markdown with inline shell commands, JSON examples, and configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include CloudRobo CLI and SDK examples, workspace IDs, member IDs, role IDs, OBS paths, and active workspace configuration guidance.]

## Skill Version(s):

1.0.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
