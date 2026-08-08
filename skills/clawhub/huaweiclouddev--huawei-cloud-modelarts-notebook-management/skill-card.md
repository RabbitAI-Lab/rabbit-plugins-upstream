## Description: <br>
Manage Huawei Cloud ModelArts Notebook instances through hcloud CLI lifecycle, lease, tag, image, flavor, cluster, feature, and storage operations, with user confirmation required before write operations. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[huaweiclouddev](https://clawhub.ai/user/huaweiclouddev) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and cloud operators use this skill to inspect and manage Huawei Cloud ModelArts Notebook resources, including notebook lifecycle actions, images, leases, tags, flavors, clusters, and storage. It is suited for operational guidance where the agent proposes hcloud commands and asks for confirmation before mutating cloud resources. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can guide high-impact cloud lifecycle actions such as creating, deleting, starting, stopping, attaching, and detaching resources. <br>
Mitigation: Require explicit user confirmation for write operations and confirm the exact region, project, resource ID, and expected effect before execution. <br>
Risk: Full management permissions grant broad authority over ModelArts notebook resources and related images, tags, leases, and storage. <br>
Mitigation: Use the read-only IAM policy unless lifecycle management is required, and grant only the additional SWR, OBS, or SFS permissions needed for the chosen workflow. <br>
Risk: Huawei Cloud AK/SK credentials could be exposed through prompts, scripts, command history, or logs. <br>
Mitigation: Keep credentials in protected CLI configuration, environment management, or cloud secret storage, and avoid embedding secrets in generated commands or files. <br>
Risk: The installation guide includes a pipe-to-bash command for hcloud CLI installation. <br>
Mitigation: Prefer downloading from the official Huawei Cloud documentation and reviewing installation steps before running them. <br>
Risk: Documented hcloud CLI and ModelArts API quirks can produce failed or misleading storage and notebook operations. <br>
Mitigation: Consult the known issues reference, use the documented jsonInput workaround when needed, and verify resource state after CLI calls. <br>


## Reference(s): <br>
- [Huawei Cloud hcloud CLI Documentation](https://support.huaweicloud.com/qs-hcli/hcli_02_003.html) <br>
- [Huawei Cloud ModelArts API Explorer](https://console.huaweicloud.com/apiexplorer/#/openapi/ModelArts) <br>
- [CLI Command Examples](artifact/references/cli-command-examples.md) <br>
- [IAM Policies](artifact/references/iam-policies.md) <br>
- [Verification Method](artifact/references/verification-method.md) <br>
- [Known Issues and Practical Solutions](artifact/references/known-issues.md) <br>
- [API Paths](artifact/references/api-paths.md) <br>


## Skill Output: <br>
**Output Type(s):** [shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline bash and JSON examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Commands use caller-supplied regions and resource identifiers; write operations require user confirmation.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
