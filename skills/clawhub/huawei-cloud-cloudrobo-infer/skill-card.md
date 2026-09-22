## Description:

Manage CloudRobo inference services for model deployment, service lifecycle operations, log inspection, and wait-deploy polling.

This skill is ready for commercial/non-commercial use.

## Publisher:

[huaweicloudskill](https://clawhub.ai/user/huaweicloudskill)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and cloud operators use this skill to guide agents through deploying CloudRobo models as inference services, managing service state, inspecting logs, and assembling safe CLI or SDK commands.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The included test script can start, stop, update, and delete a real CloudRobo service when SERVICE_ID is set.

Mitigation: Run validation in a non-production workspace, leave SERVICE_ID unset for read-only checks, and require explicit human confirmation before service-changing commands.

Risk: CloudRobo operations use real Huawei Cloud credentials and can consume compute resources.

Mitigation: Use least-privilege AK/SK credentials, prefer dry-run flows for create operations, and confirm workspace, pool, model, and stop-schedule settings before deployment.

Risk: Incorrect model-source classification can add invalid deployment parameters or omit required auto-discovered parameters.

Mitigation: Resolve model source first, follow the documented parameter policy, and present the assembled command for review before execution.

## Reference(s):

- [CLI Installation Guide](references/cli-installation-guide.md)
- [Authentication & Access Control](references/iam-policies.md)
- [Service Config Reference](references/service-config-catalog.md)
- [Dataflow Diagram](references/dataflow-diagram.md)
- [Validation Rules](references/validation-rules.md)
- [Verification Method](references/verification-method.md)
- [Acceptance Criteria](references/acceptance-criteria.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration]

**Output Format:** [Markdown with inline shell commands and JSON configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include dry-run commands, workspace/model/service identifiers selected by the user, and masked credential guidance.]

## Skill Version(s):

1.0.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
