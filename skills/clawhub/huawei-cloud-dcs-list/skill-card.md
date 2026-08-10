## Description: <br>
Query Huawei Cloud DCS instance names and list managed Redis or Memcached instances across a region for read-only inventory, filtering, and daily inspection. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[erickeyhu-hug](https://clawhub.ai/user/erickeyhu-hug) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and cloud operations engineers use this skill to list Huawei Cloud DCS instances, find instances by name, status, or ID, and produce quick inventory summaries without making write changes. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Huawei Cloud AK/SK credentials may be exposed if pasted into shared terminals, logs, or persistent shell history. <br>
Mitigation: Use least-privilege read-only DCS credentials, avoid shared terminals for secrets, prefer temporary environment variables, and unset them after use. <br>
Risk: Installing the Huawei Cloud CLI with elevated permissions can introduce supply-chain risk if the download source is not verified. <br>
Mitigation: Verify the Huawei CLI download source before running sudo installation steps. <br>
Risk: Overbroad IAM permissions are unnecessary for this read-only inventory workflow. <br>
Mitigation: Use DCS ReadOnlyAccess or a finer-grained policy limited to dcs:instance:get and dcs:instance:list. <br>
Risk: Exact name matching may return empty results in some deployments even when an instance exists. <br>
Mitigation: Use the fuzzy name filter for lookup, then verify the returned instance_id with ShowInstance for precise details. <br>


## Reference(s): <br>
- [CLI Installation Guide](artifact/references/cli-installation-guide.md) <br>
- [IAM Policies](artifact/references/iam-policies.md) <br>
- [Verification Method](artifact/references/verification-method.md) <br>
- [Data Flow Diagram](artifact/references/dataflow-diagram.md) <br>
- [Acceptance Criteria](artifact/references/acceptance-criteria.md) <br>
- [Huawei Cloud KooCLI Linux Download](https://hwcloudcli.obs.cn-north-4.myhuaweicloud.com/cli/latest/hcloud_cli_linux_amd64.tar.gz) <br>
- [Huawei Cloud KooCLI macOS Download](https://hwcloudcli.obs.cn-north-4.myhuaweicloud.com/cli/latest/hcloud_cli_mac_amd64.tar.gz) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with Huawei Cloud CLI commands, JSON IAM policy examples, and Python SDK fallback code] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Read-only DCS queries; command examples require user-supplied region, credentials, and optional instance identifiers.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
