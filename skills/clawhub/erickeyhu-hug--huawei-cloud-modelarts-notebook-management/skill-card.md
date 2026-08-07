## Description: <br>
Manage Huawei Cloud ModelArts Notebook instances through full lifecycle operations via the hcloud CLI, covering instance, lease, tag, image, flavor, cluster, feature, and dynamic storage operations while requiring confirmation for write actions. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[erickeyhu-hug](https://clawhub.ai/user/erickeyhu-hug) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and cloud operators use this skill to inspect and manage Huawei Cloud ModelArts Notebook resources through hcloud CLI commands. It supports day-to-day queries, lifecycle changes, image and storage operations, lease renewal, and tag management with confirmation required before write operations. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The installation guide includes a remote shell execution command for hcloud CLI installation. <br>
Mitigation: Do not run the curl-to-bash command as written; install hcloud from an official package or downloaded installer that can be inspected and verified. <br>
Risk: Full lifecycle management can create billable resources, delete resources, change instance state, attach or detach storage, renew leases, or change images. <br>
Mitigation: Use read-only IAM unless write access is required, and require explicit user confirmation before create, update, delete, start, stop, attach, detach, renew, register, sync, or image operations. <br>
Risk: Some ModelArts notebook storage and CLI behaviors are documented as inconsistent or easy to misapply. <br>
Mitigation: Follow the known-issues guidance for storage ownership, pool_id, dew_secret_name, mount_path, cli-jsonInput, lease duration calculation, and response parsing before running affected operations. <br>


## Reference(s): <br>
- [CLI Command Examples](references/cli-command-examples.md) <br>
- [IAM Policies](references/iam-policies.md) <br>
- [Verification Method](references/verification-method.md) <br>
- [Known Issues and Practical Solutions](references/known-issues.md) <br>
- [API Paths](references/api-paths.md) <br>
- [CLI Installation Guide](references/cli-installation-guide.md) <br>
- [Data Flow Diagram](references/dataflow-diagram.md) <br>
- [Acceptance Criteria](references/acceptance-criteria.md) <br>
- [Huawei Cloud hcloud CLI Documentation](https://support.huaweicloud.com/qs-hcli/hcli_02_003.html) <br>
- [Huawei Cloud ModelArts API Explorer](https://console.huaweicloud.com/apiexplorer/#/openapi/ModelArts) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Configuration instructions, Code, Guidance] <br>
**Output Format:** [Markdown with inline bash, JSON, and Python code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs are intended as user-reviewed operational commands and guidance; write operations require explicit user confirmation before execution.] <br>

## Skill Version(s): <br>
1.0.0 (source: release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
