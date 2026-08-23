## Description: <br>
Queries Huawei Cloud billing and fee details only when Terraform needs a billing or pricing inquiry, covering balances, bills, coupons, stored-value cards, orders, refunds, costs, free resources, resource usage, enterprise accounts, and on-demand or period pricing. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[erickeyhu-hug](https://clawhub.ai/user/erickeyhu-hug) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and cloud engineers use this skill when Terraform work requires read-only Huawei Cloud billing, pricing, fee, coupon, order, refund, account, or usage information. It helps collect queried values for bill summaries, price checks, environment inventory, and automation parameter selection without performing create, update, or delete operations. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The security scan says the skill is read-only but labeled billing-only while packaged behavior can query broader Huawei Cloud account, IAM, and resource metadata. <br>
Mitigation: Install only when that broader read-only query scope is intended, and use tightly scoped read-only Huawei Cloud credentials. <br>
Risk: The security scan notes that setup installs Python dependencies, creates a local virtual environment, validates IAM access, and disables SSL verification in the SDK configuration. <br>
Mitigation: Review the package before installation, use non-production or least-privilege credentials where possible, and account for the disabled SSL verification behavior before running queries. <br>
Risk: Billing, account, and resource query output may contain sensitive commercial or account information. <br>
Mitigation: Limit query scope by region, project, resource, and date range, and do not reveal Huawei Cloud credential environment variable values in responses. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/erickeyhu-hug/skills/huawei-cloud-business-tf-support) <br>
- [BSS Python Script Usage Guide](references/bss/guide.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell command examples and JSON or tabular query results from scripts] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs should be based on actual Huawei Cloud API responses and should avoid exposing credential environment variable values.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
