## Description:

Run the R2C (Robot-to-Cloud) data-plane client for a robot-side edge process that uses Zenoh pub/sub, an mTLS credential bundle, hardware adapters, translators, and a control loop.

This skill is ready for commercial/non-commercial use.

## Publisher:

[huaweicloudskill](https://clawhub.ai/user/huaweicloudskill)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and robotics engineers use this skill to start and test a CloudRobo R2C robot edge client, stream observations over Zenoh with mTLS credentials, handle cloud actions, record observations, and develop custom hardware adapters.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The R2C client can control real robot hardware.

Mitigation: Start with dummy hardware or dry_run, confirm dry_run still sends observations, clear the robot workspace before live execution, and keep an emergency stop available.

Risk: The client uses credential bundles and may transmit robot telemetry.

Mitigation: Use non-production credentials first, protect the credential bundle and private key password, and review privacy controls before installation.

Risk: Custom adapters can execute trusted local code against hardware.

Mitigation: Install custom adapters only from trusted sources and test them in dry_run before enabling real execution.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/huaweicloudskill/skills/huawei-cloud-cloudrobo-r2c)
- [CLI Installation Guide](references/cli-installation-guide.md)
- [Authentication & Access Control](references/iam-policies.md)
- [Dataflow Diagram](references/dataflow-diagram.md)
- [Verification Method](references/verification-method.md)
- [Acceptance Criteria](references/acceptance-criteria.md)
- [Client Config Reference](references/client-config-catalog.md)
- [Robot Config Reference](references/robot-config-catalog.md)
- [Custom Adapter Development Guide](references/custom-adapter-guide.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline bash, YAML, JSON, and Python snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose long-running edge-client commands and configuration changes; command execution can create logs or observation recording files.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
