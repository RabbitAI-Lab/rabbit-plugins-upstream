## Description:

Manage CloudRobo robot instances by registering robots, querying robot lists and details, updating metadata, deleting offline robots, exporting robot access certificate ZIPs, and retrieving robot-side SDK package information.

This skill is ready for commercial/non-commercial use.

## Publisher:

[huaweicloudskill](https://clawhub.ai/user/huaweicloudskill)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and robot operations teams use this skill to manage the CloudRobo robot lifecycle, including onboarding, operational lookup, metadata updates, certificate export, cleanup, and SDK upgrade discovery.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The bundled verification script can update a robot, export its certificate ZIP, and delete it when ROBOT_ID is set.

Mitigation: Do not run scripts/test-cli-commands.sh with ROBOT_ID set unless those actions are intended; prefer dry-run commands and manual execution with explicit confirmations.

Risk: CloudRobo AK/SK credentials and ~/.cloudrobo/config.yaml grant access to CloudRobo operations.

Mitigation: Use a least-privilege CloudRobo account, protect environment variables and config files, and avoid logging or committing credentials.

Risk: Exported robot certificate ZIPs are credential bundles for robot-side access.

Mitigation: Store exported ZIPs only in protected locations, avoid shared or public paths, and verify the export produced a non-empty ZIP before use.

## Reference(s):

- [CLI Installation Guide](artifact/references/cli-installation-guide.md)
- [IAM Policies](artifact/references/iam-policies.md)
- [Dataflow Diagram](artifact/references/dataflow-diagram.md)
- [Robot Config Reference](artifact/references/robot-config-catalog.md)
- [Validation Rules](artifact/references/validation-rules.md)
- [Verification Method](artifact/references/verification-method.md)
- [Acceptance Criteria](artifact/references/acceptance-criteria.md)
- [ClawHub skill page](https://clawhub.ai/huaweicloudskill/skills/huawei-cloud-cloudrobo-robot)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands, Python snippets, JSON/YAML examples, and operational checklists.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May guide mutating CloudRobo operations and certificate ZIP export; credentials and exported ZIP files require protected handling.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
