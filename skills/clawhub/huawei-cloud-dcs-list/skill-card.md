## Description:

Lists Huawei Cloud DCS Redis and Memcached instances in a tenant region and formats the results as names, tables, JSON, Markdown, or CSV.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wlc-dev](https://clawhub.ai/user/wlc-dev)

### License/Terms of Use:

MIT-0

## Use Case:

Cloud operators and developers use this skill to inspect regional DCS inventory, filter and sort instances, and obtain instance identifiers for follow-up work.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: ClawScan reports an unsafe remote install method, and its review is incomplete, so the results do not establish that the skill is safe.

Mitigation: Avoid installation until the publisher provides a verifiable, version-pinned installer and the remaining security checks have been reviewed.

Risk: The security review reports that tag filtering can return instances outside the requested tag scope.

Mitigation: Confirm the filter behavior and required tool scope with the publisher, and verify returned instances against the intended scope before relying on the inventory.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/wlc-dev/skills/huawei-cloud-dcs-list)
- [Huawei Cloud KooCLI installation guide](https://support.huaweicloud.com/qs-hcli/hcli_02_003.html)
- [Least-privilege IAM policy](artifact/references/iam-policies.md)
- [Verification method](artifact/references/verification-method.md)

## Skill Output:

**Output Type(s):** [Text, JSON, Markdown, CSV]

**Output Format:** [Instance names, tables, JSON arrays, GitHub-flavored Markdown tables, or RFC 4180 CSV]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Selectable region, filters, ordering, and page size; Markdown or CSV results can optionally be saved to files.]

## Skill Version(s):

1.0.9 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
