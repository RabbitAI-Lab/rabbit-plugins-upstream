## Description:

Lists Huawei Cloud public or private DNS zones and record sets with filtering, pagination, and table, JSON, or names-only output.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wlc-dev](https://clawhub.ai/user/wlc-dev)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and cloud operators use it to inspect tenant DNS zones and record sets for inventory, operations checks, and lookup of zone IDs or domain names before dependent work.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The bundled setup guide includes an installer command whose source could not be verified.

Mitigation: Install KooCLI using Huawei's documented download and checksum process before running the skill.

Risk: DNS results may contain private domain names and contact details.

Mitigation: Use a DNS read-only account, configure credentials outside chat, and handle returned inventory as sensitive.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/wlc-dev/skills/huawei-cloud-dns-list)
- [Huawei Cloud KooCLI installation guide](https://support.huaweicloud.com/qs-hcli/hcli_02_003.html)
- [Least-privilege DNS IAM policy](references/iam-policies.md)
- [Verification method and API parameters](references/verification-method.md)

## Skill Output:

**Output Type(s):** [Text, JSON]

**Output Format:** [Tabular text, JSON array, or newline-separated domain names]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes returned DNS fields and automatically paginates list results.]

## Skill Version(s):

1.0.1 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
