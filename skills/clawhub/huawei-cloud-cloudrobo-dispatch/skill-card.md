## Description:

Manage CloudRobo embodied-agent task dispatch by creating, listing, monitoring, cancelling, and retrieving results for robot tasks within a workspace session.

This skill is ready for commercial/non-commercial use.

## Publisher:

[huaweicloudskill](https://clawhub.ai/user/huaweicloudskill)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to turn natural-language robot work requests into CloudRobo dispatcher tasks, then monitor, wait for, cancel, or inspect task results. It is intended for workspace-scoped robot task orchestration where robot IDs, execution model IDs, and stop conditions are resolved before execution.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The verification script can submit a real robot movement task after only a brief warning.

Mitigation: Run dry-run commands first, use a simulator or isolated test robot, and require an explicit affirmative confirmation before any create-task or cancel-task operation.

Risk: CloudRobo credentials allow task creation, cancellation, and result access within a workspace.

Mitigation: Use least-privilege CloudRobo credentials, avoid hardcoding AK/SK values, and verify the active workspace and session before dispatching tasks.

Risk: Unbounded or incorrect robot tasks can run longer than intended or target the wrong model or robot.

Mitigation: Resolve robot_id and exec_model_id dynamically, require bounded exec_constraints, and confirm the task configuration with the user before submission.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/huaweicloudskill/skills/huawei-cloud-cloudrobo-dispatch)
- [CLI Installation Guide](references/cli-installation-guide.md)
- [IAM Policies](references/iam-policies.md)
- [Verification Method](references/verification-method.md)
- [Dataflow Diagram](references/dataflow-diagram.md)
- [Acceptance Criteria](references/acceptance-criteria.md)
- [Validation Rules](references/validation-rules.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands, Python examples, and JSON configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose CloudRobo CLI and SDK operations that create, wait on, cancel, or read robot dispatch tasks; mutating operations require user confirmation and bounded stop conditions.]

## Skill Version(s):

1.0.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
