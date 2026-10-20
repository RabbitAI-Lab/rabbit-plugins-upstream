## Description:

Lists Huawei Cloud ECS instances by region and filters, with table, JSON, names-only, and Markdown inventory outputs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wlc-dev](https://clawhub.ai/user/wlc-dev)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and cloud operators use this skill to inspect Huawei Cloud ECS inventories for a chosen region, optionally filter instances by status or name, and export results for review or downstream use.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Executable command overrides can weaken the advertised safeguards.

Mitigation: Use a trusted hcloud installation with both command overrides unset; request removal of production command overrides.

Risk: Credential disclosures in the skill are inaccurate, which may lead to unsafe credential handling or excessive access.

Mitigation: Use credentials restricted to ecs:servers:list, keep credentials in a trusted profile or environment, and request correction of the credential guidance.

Risk: Markdown inventory export overwrites an existing destination and may expose instance details.

Mitigation: Check the destination before exporting and protect the resulting inventory file.

Risk: An invalid or unintended region may produce misleading inventory results.

Mitigation: Validate the region input before running the query.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/wlc-dev/skills/huawei-cloud-ecs-list)
- [Huawei Cloud KooCLI documentation](https://support.huaweicloud.com/qs-hcli/hcli_02_003.html)

## Skill Output:

**Output Type(s):** [Text, JSON, Markdown]

**Output Format:** [Plain-text instance table, JSON array, names-and-IDs inventory, or Markdown report]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports region, status, and name filters with automatic paging; Markdown export can overwrite an existing destination file.]

## Skill Version(s):

1.0.0 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
