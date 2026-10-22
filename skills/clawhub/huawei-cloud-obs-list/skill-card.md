## Description:

Lists a Huawei Cloud account's OBS buckets through KooCLI, with an SDK fallback and table, JSON, or names-only output.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wlc-dev](https://clawhub.ai/user/wlc-dev)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and cloud operators use this skill to inventory Huawei Cloud OBS buckets and retrieve bucket names for routine operations or downstream automation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Command overrides or an unverified KooCLI installation could make execution differ from expectations.

Mitigation: Install KooCLI through Huawei's official instructions and keep OBS_LIST_HCLOUD_BIN and OBS_LIST_HCLOUD_ARGS unset.

Risk: The SDK fallback's endpoint or count behavior may not match the requested settings, making inventory results misleading.

Mitigation: Review and correct the fallback's endpoint and count controls before relying on its results.

Risk: Over-privileged or exposed credentials could put the cloud account at risk.

Mitigation: Use dedicated credentials limited to bucket listing, configure them outside chat, and never share keys in chat.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/wlc-dev/skills/huawei-cloud-obs-list)
- [Huawei Cloud KooCLI quick start](https://support.huaweicloud.com/qs-hcli/hcli_02_003.html)
- [CLI installation and credentials](references/cli-installation-guide.md)
- [Read-only IAM policy](references/iam-policies.md)
- [Verification method](references/verification-method.md)

## Skill Output:

**Output Type(s):** [Text, JSON]

**Output Format:** [Aligned bucket table, JSON array, or names-only text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Bucket name, creation date, region, and storage class when available; supports region and page-size controls.]

## Skill Version(s):

1.0.0 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
