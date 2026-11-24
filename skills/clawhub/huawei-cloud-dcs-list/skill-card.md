## Description:

Lists and filters Huawei Cloud DCS (Redis or Memcached) instances and returns the results as names, tables, JSON, Markdown, or CSV.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wlc-dev](https://clawhub.ai/user/wlc-dev)

### License/Terms of Use:

MIT-0

## Use Case:

Cloud operators and developers use this skill to inventory and inspect Huawei Cloud DCS instances, filter results for operational checks, and export listings for downstream use.

### Deployment Geography for Use:

Global (Huawei Cloud regions; default region cn-north-4)

## Known Risks and Mitigations:

Risk: A launch environment controlled by an attacker could redirect command execution to a different program with the agent's privileges; scanning was partial and does not establish that the artifact is safe.

Mitigation: Before installation or use, review who can influence the launch environment and selected executable, and review the skill's tool permissions. Use trusted launch settings.

## Reference(s):

- [KooCLI Installation & Credential Guide](references/cli-installation-guide.md)
- [IAM Policies (least privilege, read-only)](references/iam-policies.md)
- [Read-only Guard](references/read-only-guard.md)
- [Output Formats](references/output-formats.md)
- [Verification Method](references/verification-method.md)
- [Huawei Cloud KooCLI official quick start](https://support.huaweicloud.com/qs-hcli/hcli_02_003.html)
- [ClawHub skill page](https://clawhub.ai/wlc-dev/skills/huawei-cloud-dcs-list)

## Skill Output:

**Output Type(s):** [Text, JSON, Markdown, CSV]

**Output Format:** [Plain text lists and tables, JSON, Markdown tables, or RFC 4180 CSV]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Filtered and paged instance listings; optional Markdown or CSV file export.]

## Skill Version(s):

1.0.12 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
