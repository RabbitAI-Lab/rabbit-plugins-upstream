## Description: <br>
Helps agents answer Huawei Cloud BSS billing questions about balances, spend, attribution, reconciliation, coupons, stored-value cards, and enterprise or partner billing using read-only hcloud queries. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[erickeyhu-hug](https://clawhub.ai/user/erickeyhu-hug) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, developers, and FinOps teams use this skill to investigate Huawei Cloud BSS billing questions with read-only evidence: balances, monthly spend, charge attribution, reconciliation, resource packages, coupons, stored-value cards, and enterprise or partner billing scope. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill relies on an existing hcloud profile with access to Huawei Cloud billing data. <br>
Mitigation: Use a read-only BSS IAM profile and confirm that users are comfortable exposing billing data to the agent before running queries. <br>
Risk: The install guide includes non-interactive installer commands and local cleanup commands that can affect hcloud installation or profile state. <br>
Mitigation: Review installation, update, language-setting, uninstall, and cleanup commands manually; avoid non-interactive installation and rm -rf ~/.hcloud unless profile impact is understood and backups exist. <br>
Risk: Billing conclusions can be misleading when based on partial pagination, incomplete periods, sampling, or narrow evidence boundaries. <br>
Mitigation: State scope, billing period, and money basis explicitly; avoid whole-account or final conclusions unless the evidence covers that grain. <br>


## Reference(s): <br>
- [Huawei Cloud KooCLI Installation Guide](references/cli-installation-guide.md) <br>
- [IAM Minimum Permissions](references/iam-policies.md) <br>
- [Command Contract Appendix](references/related-commands.md) <br>
- [Huawei Cloud Billing Semantic Catalog](references/semantic/catalog.yml) <br>
- [Billing Ontology](references/semantic/billing-ontology.yml) <br>
- [Huawei Cloud KooCLI Releases](https://support.huaweicloud.com/wtsnew-hcli/index.html) <br>
- [Huawei Cloud IAM Permission Best Practices](https://support.huaweicloud.com/bestpractice-iam/iam_0426.html) <br>
- [Huawei Cloud API Explorer](https://console.huaweicloud.com/apiexplorer/#/openapi/overview) <br>


## Skill Output: <br>
**Output Type(s):** [Analysis, Guidance, Shell commands, Markdown] <br>
**Output Format:** [Brief Markdown guidance with optional hcloud shell commands and concise billing findings] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses read-only Huawei Cloud BSS queries, avoids raw command output and sensitive identifiers, and refuses payment, renewal, refund, delete, and other account-changing requests.] <br>

## Skill Version(s): <br>
1.0.0 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
