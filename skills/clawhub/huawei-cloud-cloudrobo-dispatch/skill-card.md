## Description:

Manage CloudRobo embodied-agent task dispatch through robo-dispatcher: create robot tasks with execution models and constraints, list and inspect session tasks, cancel tasks, wait for completion, and retrieve task results.

This skill is ready for commercial/non-commercial use.

## Publisher:

[huaweiclouddev](https://clawhub.ai/user/huaweiclouddev)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and robotics operators use this skill to dispatch, monitor, cancel, and retrieve results for CloudRobo embodied-agent tasks within a workspace-backed session. It is suited for orchestrating robots and inference services through CloudRobo CLI or SDK workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Dispatch commands and the bundled test script can create live robot movement tasks when valid robot and execution model IDs are supplied.

Mitigation: Use a dedicated test workspace, a known safe robot or simulator, dry-run or read-only checks when possible, explicit operator confirmation for mutating actions, and bounded execution constraints.

Risk: Huawei Cloud AK/SK credentials can grant access to CloudRobo resources if exposed in shared profiles, scripts, or logs.

Mitigation: Use least-privileged credentials, keep secrets in environment or local configuration only, avoid logging credential values, and rotate keys after testing or suspected exposure.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/huaweiclouddev/skills/huawei-cloud-cloudrobo-dispatch)
- [CLI Installation Guide](references/cli-installation-guide.md)
- [Authentication & Access Control](references/iam-policies.md)
- [Verification Method](references/verification-method.md)
- [Acceptance Criteria](references/acceptance-criteria.md)
- [Validation Rules](references/validation-rules.md)
- [Dataflow Diagrams](references/dataflow-diagram.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Code, Configuration, Guidance]

**Output Format:** [Markdown with inline bash, Python, and JSON snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include CloudRobo CLI or SDK command plans that create, query, wait for, cancel, or retrieve real robot task results.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
