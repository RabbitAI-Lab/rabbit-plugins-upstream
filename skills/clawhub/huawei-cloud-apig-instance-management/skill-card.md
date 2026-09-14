## Description:

Manage Huawei Cloud APIG dedicated instances, API groups, APIs, publishing, throttling policies, public ingress EIP binding, and public-access diagnostics through the hcloud CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[huaweiclouddev](https://clawhub.ai/user/huaweiclouddev)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and cloud operators use this skill to inspect, create, update, publish, throttle, and delete Huawei Cloud APIG resources with hcloud CLI commands. It is also used to diagnose public access issues by checking instance EIP state, API group domains, and the instance-to-publish chain.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The bundled telemetry SDK can send IAM-authenticated execution data off-box.

Mitigation: Review or remove scripts/skill_quality_sdk.py before installation, disable telemetry by default, and avoid exposing AK/SK credentials where SKILL_QUALITY_ENDPOINT or SKILL_QUALITY_INSECURE can be changed unexpectedly.

Risk: Setup guidance uses mutable KooCLI installation and update artifacts.

Mitigation: Pin and verify KooCLI installation artifacts before use.

Risk: The skill can create, update, publish, bind public ingress, and delete APIG resources.

Mitigation: Use read-only credentials unless mutation is required, narrow Huawei IAM permissions to the intended APIG actions and resources, preview every mutating command, and require explicit confirmation for delete operations.

## Reference(s):

- [KooCLI Installation & Authentication Guide](references/cli-installation-guide.md)
- [IAM Policies for APIG Skill](references/iam-policies.md)
- [Verification Method](references/verification-method.md)
- [Data Flow Diagrams](references/dataflow-diagram.md)
- [Acceptance Criteria](references/acceptance-criteria.md)
- [Huawei Cloud APIG Documentation](https://support.huaweicloud.com/apig/)
- [Huawei Cloud KooCLI Quickstart](https://support.huaweicloud.com/qs-hcli/hcli_02_003.html)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline bash commands and JSON-oriented verification guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only actions return command output or diagnostic summaries; mutating actions require preview, confirmation, execution, and read-back verification.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
