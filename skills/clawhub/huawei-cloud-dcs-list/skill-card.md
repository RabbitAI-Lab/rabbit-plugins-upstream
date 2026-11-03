## Description:

Lists and filters Huawei Cloud DCS (Redis or Memcached) instances in a selected region, returning names, a table, or JSON through KooCLI or Huawei's SDK.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wlc-dev](https://clawhub.ai/user/wlc-dev)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and cloud operators use this skill to inspect Huawei Cloud DCS inventories, filter instances during routine operations, and retrieve instance IDs for follow-on tasks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Exact-name searches can ignore tag restrictions and return instances outside the intended scope.

Mitigation: Request a fix that preserves tag restrictions during exact-name searches, and verify the returned scope before relying on filtered results.

Risk: Inventory queries use cloud account credentials and expose instance details to the requesting agent.

Mitigation: Use credentials limited to listing DCS instances, and never paste access keys or secret keys into chat.

Risk: Installing the CLI involves running software from an external source.

Mitigation: Verify the installer against Huawei's current official documentation before running it.

## Reference(s):

- [Huawei Cloud KooCLI Quick Start](https://support.huaweicloud.com/qs-hcli/hcli_02_003.html)
- [CLI Installation Guide](references/cli-installation-guide.md)
- [Least-Privilege IAM Policy](references/iam-policies.md)
- [API Verification Method](references/verification-method.md)
- [ClawHub Release](https://clawhub.ai/wlc-dev/skills/huawei-cloud-dcs-list)

## Skill Output:

**Output Type(s):** [Text, JSON]

**Output Format:** [Plain-text instance-name list or table, or JSON array]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Names are shown by default; table and raw JSON formats are available.]

## Skill Version(s):

1.0.2 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
