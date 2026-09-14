## Description:

Manage CloudRobo robot instances by registering, listing, updating, deleting offline robots, exporting access certificates, and retrieving robot-side SDK package information.

This skill is ready for commercial/non-commercial use.

## Publisher:

[huaweiclouddev](https://clawhub.ai/user/huaweiclouddev)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and robotics operations teams use this skill to manage CloudRobo robot lifecycle workflows, including registration, inventory lookup, metadata updates, certificate export for onboarding, SDK package lookup, and cleanup of decommissioned robots.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The included verification script can update a real robot, export its access credentials, and delete it when ROBOT_ID is set.

Mitigation: Use non-production credentials and workspaces, avoid setting ROBOT_ID for routine checks, prefer dry-run or read-only verification, and require explicit confirmation before mutating commands.

Risk: Certificate export writes a sensitive access-config ZIP and the test script includes a hardcoded export password.

Mitigation: Provide a unique password for real exports, store exported ZIP files as secrets, and keep credential bundles out of source control and shared locations.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/huaweiclouddev/skills/huawei-cloud-cloudrobo-robot)
- [CLI Installation Guide](references/cli-installation-guide.md)
- [Authentication & Access Control](references/iam-policies.md)
- [Verification Method](references/verification-method.md)
- [Dataflow Diagram](references/dataflow-diagram.md)
- [Acceptance Criteria](references/acceptance-criteria.md)
- [Robot Config Reference](references/robot-config-catalog.md)
- [Validation Rules](references/validation-rules.md)

## Skill Output:

**Output Type(s):** [Markdown, Shell commands, Code, Configuration, Guidance]

**Output Format:** [Markdown guidance with CLI command examples, Python SDK snippets, configuration notes, and verification steps]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May direct agents to create, update, export credentials for, or delete CloudRobo robot resources after user confirmation.]

## Skill Version(s):

1.0.0 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
