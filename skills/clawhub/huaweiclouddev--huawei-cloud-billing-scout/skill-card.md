## Description: <br>
Huawei Cloud Billing Scout helps agents answer read-only Huawei Cloud BSS balance, spend, charge attribution, reconciliation, coupon, stored-value card, enterprise, and partner billing questions through hcloud. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[huaweiclouddev](https://clawhub.ai/user/huaweiclouddev) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, FinOps teams, and Huawei Cloud account operators use this skill to investigate billing balances, monthly spend, charge attribution, reconciliation gaps, resource packages, coupons, stored-value cards, and enterprise or partner account billing with read-only BSS evidence. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill handles sensitive Huawei Cloud billing data through the user's current hcloud profile. <br>
Mitigation: Use a read-only BSS IAM profile, keep account and business identifiers desensitized, and avoid exposing credentials, profile names, or regions in responses. <br>
Risk: The support documentation includes remote installer commands and uninstall steps that can remove local hcloud configuration. <br>
Mitigation: Manually verify KooCLI installers before execution, avoid non-interactive remote script execution unless the source is trusted and verified, and back up profiles before removing ~/.hcloud. <br>
Risk: The workflow requires a persistent hcloud CLI language configuration change for BSS operations. <br>
Mitigation: Confirm the current profile and configuration before running billing queries, and make the configuration change only when it is needed for the read-only evidence-gathering phase. <br>


## Reference(s): <br>
- [Huawei Cloud Billing Scout Skill Page](https://clawhub.ai/huaweiclouddev/skills/huawei-cloud-billing-scout) <br>
- [Huawei Cloud KooCLI Installation Guide](references/cli-installation-guide.md) <br>
- [IAM Minimum Permissions](references/iam-policies.md) <br>
- [Command Contract Appendix](references/related-commands.md) <br>
- [HuaweiCloudBillingSemanticCatalog](references/semantic/catalog.yml) <br>
- [BillingOntology](references/semantic/billing-ontology.yml) <br>
- [Huawei Cloud KooCLI Latest Version](https://support.huaweicloud.com/wtsnew-hcli/index.html) <br>
- [Huawei Cloud IAM Permission Best Practices](https://support.huaweicloud.com/bestpractice-iam/iam_0426.html) <br>
- [Huawei Cloud API Explorer](https://console.huaweicloud.com/apiexplorer/#/openapi/overview) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown briefing with concise conclusions, fact points, and inline hcloud command guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Read-only BSS evidence only; sensitive identifiers, credentials, profile, and region are not included in final responses.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
