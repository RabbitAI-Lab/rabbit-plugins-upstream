## Description:

Runs the R2C (Robot-to-Cloud) robot-side edge client using Zenoh pub/sub with mTLS credential bundles, hardware adapters, translators, and control-loop workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[huaweiclouddev](https://clawhub.ai/user/huaweiclouddev)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and robotics engineers use this skill to start and test a robot-side R2C data-plane client, configure Zenoh/mTLS connectivity, and develop custom hardware adapters for CloudRobo-connected robots.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The verification script can start a live robot client with a real hardware configuration.

Mitigation: Review commands before execution, supervise the robot, and prefer dummy configs or dry_run mode for testing.

Risk: The skill uses credential bundles and optional private-key passwords.

Mitigation: Protect credential bundles and private-key passwords as secrets, prefer TLS endpoints, and avoid exposing passwords in shared shells.

Risk: Installing broad or unpinned package extras can expand the trusted dependency set.

Mitigation: Install only the minimal pinned packages needed for the target robot and review packages before use.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/huaweiclouddev/skills/huawei-cloud-cloudrobo-r2c)
- [CLI Installation Guide](references/cli-installation-guide.md)
- [Authentication & Access Control](references/iam-policies.md)
- [Dataflow Diagram](references/dataflow-diagram.md)
- [Verification Method](references/verification-method.md)
- [Acceptance Criteria](references/acceptance-criteria.md)
- [Client Config Reference](references/client-config-catalog.md)
- [Robot Config Reference](references/robot-config-catalog.md)
- [Custom Adapter Development Guide](references/custom-adapter-guide.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Code, Guidance]

**Output Format:** [Markdown with inline bash commands, YAML and JSON configuration examples, and Python code examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include long-running client commands, dry-run verification steps, credential-bundle handling guidance, and custom adapter implementation examples.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
