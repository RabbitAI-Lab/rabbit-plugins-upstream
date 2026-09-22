## Description:

Manage Huawei Cloud APIG dedicated API Gateway instances and resources through the hcloud CLI, including instance lifecycle, API groups and APIs, publish and offline workflows, throttling policies, EIP binding, and read-only public access diagnostics.

This skill is ready for commercial/non-commercial use.

## Publisher:

[huaweicloudskill](https://clawhub.ai/user/huaweicloudskill)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and cloud operators use this skill to inspect, diagnose, create, update, publish, and delete Huawei Cloud APIG dedicated gateway resources through KooCLI. It is intended for APIG administration workflows that require explicit region selection, least-privilege credentials, command preview for mutations, and read-back verification.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The package includes telemetry code that can use Huawei Cloud credentials and send execution inputs, outputs, errors, and stack traces to a remote endpoint.

Mitigation: Review the package before installation and remove or disable the bundled skill_quality_sdk.py telemetry path unless that reporting behavior is intentional.

Risk: APIG create, update, publish, EIP binding, and delete workflows can mutate or remove cloud resources.

Mitigation: Use read-only IAM permissions by default, elevate only when mutation is required, preview every mutating command, require explicit user confirmation, and perform read-back verification.

Risk: Huawei AK/SK credentials can be exposed through hardcoded examples, shell history, or overly broad credentials.

Mitigation: Use least-privilege Huawei credentials from environment variables or a local KooCLI profile, avoid command-line AK/SK values, and do not persist secrets in skill documents or scripts.

Risk: Public access can be misdiagnosed if an internal API group sl_domain is treated as an internet endpoint.

Mitigation: Use the APIG instance eip_address for public access decisions, treat sl_domain as internal-only, and verify EIP binding through the AddIngressEipV2 response, retry result, or console evidence.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/huaweicloudskill/skills/huawei-cloud-apig-instance-management)
- [Huawei Cloud APIG documentation](https://support.huaweicloud.com/apig/)
- [KooCLI quickstart](https://support.huaweicloud.com/qs-hcli/hcli_02_003.html)
- [KooCLI installation and authentication guide](references/cli-installation-guide.md)
- [IAM policies for APIG skill](references/iam-policies.md)
- [Verification method](references/verification-method.md)
- [Data flow diagrams](references/dataflow-diagram.md)
- [Acceptance criteria](references/acceptance-criteria.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline hcloud CLI commands and JSON-oriented verification steps]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only actions return command output analysis; mutating actions require command preview, user confirmation, execution, and read-back verification.]

## Skill Version(s):

1.0.1 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
