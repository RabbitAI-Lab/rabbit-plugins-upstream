## Description:

Lists Huawei Cloud CodeArts projects, repositories, pipelines, and deployment tasks for a selected region or project.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wlc-dev](https://clawhub.ai/user/wlc-dev)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and cloud administrators use the skill to inspect CodeArts project, repository, pipeline, and deployment-task inventories, optionally scoped by region, project, name, or status.

### Deployment Geography for Use:

Global across Huawei Cloud regions available to the tenant; defaults to cn-north-4.

## Known Risks and Mitigations:

Risk: Runtime executable or extra-argument overrides can bypass the advertised read-only protection.

Mitigation: Clear those overrides before use, install the CLI from a trusted source, and use dedicated read-only Huawei credentials.

Risk: The SDK fallback reads credentials into memory, and full inventory fields are returned to the agent.

Mitigation: Use dedicated read-only credentials and limit access to the agent and inventory data to what the task requires.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/wlc-dev/skills/huawei-cloud-codearts-list)
- [Huawei Cloud KooCLI quick start](https://support.huaweicloud.com/qs-hcli/hcli_02_003.html)
- [KooCLI installation script](https://cn-north-4-hdn-koocli.obs.cn-north-4.myhuaweicloud.com/cli/latest/hcloud_install.sh)
- [Acceptance Criteria](artifact/references/acceptance-criteria.md)
- [IAM Policies](artifact/references/iam-policies.md)
- [Data Flow Diagram](artifact/references/dataflow-diagram.md)
- [Verification Method](artifact/references/verification-method.md)

## Skill Output:

**Output Type(s):** [text, JSON]

**Output Format:** [Resource inventory as a table, raw JSON, or compact name-and-ID list]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports region, project, name, and status filters; output contains returned resource fields.]

## Skill Version(s):

1.0.0 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
