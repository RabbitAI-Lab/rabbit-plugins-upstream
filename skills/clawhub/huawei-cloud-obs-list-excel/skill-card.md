## Description:

Lists Huawei Cloud OBS buckets and exports the results as a local Excel workbook, terminal table, or JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wlc-dev](https://clawhub.ai/user/wlc-dev)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and cloud administrators can inventory Huawei Cloud OBS buckets and create a local spreadsheet report for review or recordkeeping.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The installation steps weaken download security.

Mitigation: Use a dedicated virtual environment, verify certificates, and install reviewed dependency versions; obtain KooCLI through Huawei's verified distribution instructions.

Risk: Cloud credentials and account-wide bucket metadata require careful handling.

Mitigation: Grant only bucket-list permissions and configure credentials locally; never paste secrets into chat.

Risk: Endpoint overrides or result limits may not be honored by the SDK fallback.

Mitigation: Do not rely on those options when the SDK fallback is used until the behavior is corrected and verified.

## Reference(s):

- [Huawei Cloud KooCLI Quick Start](https://support.huaweicloud.com/qs-hcli/hcli_02_003.html)
- [CLI Installation Guide](references/cli-installation-guide.md)
- [Least-Privilege IAM Policies](references/iam-policies.md)
- [Data Flow Diagram](references/dataflow-diagram.md)

## Skill Output:

**Output Type(s):** [Files, Text, JSON]

**Output Format:** [Excel (.xlsx), terminal table, or JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Bucket inventory only; the Excel workbook is created locally.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
