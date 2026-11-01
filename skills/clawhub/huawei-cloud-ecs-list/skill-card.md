## Description:

Lists Huawei Cloud ECS instances in a selected region through read-only queries, with filters and table, JSON, or compact name-and-ID output.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wlc-dev](https://clawhub.ai/user/wlc-dev)

### License/Terms of Use:

MIT-0

## Use Case:

Cloud operators and platform engineers use this skill to inspect ECS inventory in a Huawei Cloud region, filter instances by name or status, and retrieve instance IDs for follow-on workflows. It returns inventory data and does not perform instance changes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The installer source is unverified, and environment settings can bypass the stated read-only guarantee.

Mitigation: Use Huawei's official installation instructions and checksum verification. Leave ECS_LIST_HCLOUD_BIN and ECS_LIST_HCLOUD_ARGS unset, use a trusted execution environment, and grant only ecs:servers:list.

Risk: Credentials and inventory output containing IP addresses and other cloud metadata could be exposed.

Mitigation: Keep credentials out of chat, provide SDK credentials through the environment, and protect the inventory output.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wlc-dev/skills/huawei-cloud-ecs-list)
- [Huawei Cloud KooCLI quick start](https://support.huaweicloud.com/qs-hcli/hcli_02_003.html)
- [KooCLI installation and credential setup](artifact/references/cli-installation-guide.md)
- [Least-privilege ECS IAM policy](artifact/references/iam-policies.md)
- [Data flow](artifact/references/dataflow-diagram.md)
- [Verification method and API details](artifact/references/verification-method.md)
- [Acceptance criteria](artifact/references/acceptance-criteria.md)

## Skill Output:

**Output Type(s):** [Text, JSON]

**Output Format:** [Plain-text instance table, compact names-and-IDs list, or JSON array printed to stdout]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Region-scoped ECS inventory with optional name and status filters and automatic paging; stdout only.]

## Skill Version(s):

1.0.5 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
