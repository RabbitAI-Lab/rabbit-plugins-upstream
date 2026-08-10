## Description: <br>
Queries the Elastic IP bound to a single Huawei Cloud ECS instance by ECS ID or name and returns the public IP address, EIP ID, status, bandwidth, and binding details. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[erickeyhu-hug](https://clawhub.ai/user/erickeyhu-hug) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, cloud operators, and support engineers use this skill to find the public EIP attached to a specific Huawei Cloud ECS instance for troubleshooting, cost review, inventory, and public-exposure checks. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Overbroad Huawei Cloud credentials may expose more ECS and EIP inventory than the lookup requires. <br>
Mitigation: Use a least-privilege IAM identity with read-only EIP list/get and ECS list/get permissions. <br>
Risk: Huawei Cloud AK/SK credentials could be exposed if pasted into chat or embedded in files. <br>
Mitigation: Configure credentials locally with KooCLI or environment variables and do not paste AK/SK into the agent conversation. <br>
Risk: The SDK fallback can perform an unfiltered regional EIP listing if no ECS ID is provided. <br>
Mitigation: Set HUAWEI_CLOUD_ECS_ID and use the ECS device ID filter before running the SDK fallback test. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/erickeyhu-hug/skills/huawei-cloud-ecs-eip-query) <br>
- [CLI Installation Guide](references/cli-installation-guide.md) <br>
- [EIP and ECS Policies](references/eip-policies.md) <br>
- [Verification Method](references/verification-method.md) <br>
- [Data Flow Diagram](references/dataflow-diagram.md) <br>
- [Acceptance Criteria](references/acceptance-criteria.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell commands, JSON command output, and Python SDK examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Read-only lookup guidance; primary path uses KooCLI and fallback path uses the Huawei Cloud EIP Python SDK.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
