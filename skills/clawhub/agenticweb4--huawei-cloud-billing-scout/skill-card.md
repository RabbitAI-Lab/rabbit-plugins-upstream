## Description:

Provides read-only Huawei Cloud BSS billing analysis for balances, spending, charge attribution, reconciliation, coupons, stored-value cards, and enterprise or partner billing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[agenticweb4](https://clawhub.ai/user/agenticweb4)

### License/Terms of Use:

MIT-0

## Use Case:

Cloud billing analysts, finance operations teams, and Huawei Cloud administrators use it to review balances, spending, charge attribution, reconciliation differences, coupons, and authorized enterprise or partner billing from the intended account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Access credentials could be exposed during setup or use.

Mitigation: Use a dedicated IAM identity with only the required billing read permissions, and keep access keys out of chat.

Risk: Billing queries could target an unintended account or scope.

Mitigation: Verify the intended account and explicitly authorize any enterprise or partner scope.

Risk: Billing results remain sensitive even when identifiers are masked.

Mitigation: Treat billing results as sensitive data.

Risk: An unverified CLI installation could compromise the user's environment.

Mitigation: Install KooCLI from Huawei's official documentation and verify its published checksum.

## Reference(s):

- [KooCLI installation guide](references/cli-installation.md)
- [Huawei Cloud IAM best practices](https://support.huaweicloud.com/bestpractice-iam/iam_0426.html)
- [Huawei Cloud API Explorer](https://console.huaweicloud.com/apiexplorer/#/openapi/overview)
- [Huawei Cloud KooCLI quick installation](https://support.huaweicloud.com/qs-hcli/hcli_02_003.html)
- [Huawei Cloud billing account balance API](https://support.huaweicloud.com/api-oce/mac_00001.html)
- [Skill homepage](https://github.com/concept-git/cloud-concept-skills/tree/main/skills/en/huawei-cloud-billing-scout)

## Skill Output:

**Output Type(s):** [Analysis, Text, Markdown, Guidance]

**Output Format:** [Concise Markdown billing brief with verified facts, evidence gaps, and a read-only next step.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires explicit Huawei Cloud or BSS billing context and the billing scope, period, and money basis needed for the query; omits credentials and full business identifiers.]

## Skill Version(s):

2.3.11 (source: frontmatter, server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
