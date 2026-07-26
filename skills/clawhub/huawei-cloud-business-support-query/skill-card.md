## Description: <br>
Queries Huawei Cloud billing and pricing, including balances, bills, coupons, stored-value cards, orders, refunds, costs, free resources, usage, enterprise accounts, and on-demand or period pricing without write operations. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[huaweiclouddev](https://clawhub.ai/user/huaweiclouddev) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, cloud engineers, and FinOps users can use this skill to query Huawei Cloud billing, pricing, balances, orders, coupons, costs, usage, and related account data through packaged read-only scripts. It helps collect current account and resource facts for cost review, pricing estimates, reporting, and operational inventory checks. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill requires Huawei Cloud credentials and may expose sensitive billing identifiers, account balances, costs, orders, coupons, and usage records in command output or logs. <br>
Mitigation: Use temporary least-privilege credentials, avoid broad administrator AK/SK values, and protect generated outputs and logs. <br>
Risk: The skill runs local setup and query scripts before accessing Huawei Cloud services. <br>
Mitigation: Review the packaged scripts before first use and run them only in a controlled environment intended for Huawei Cloud billing and inventory queries. <br>
Risk: The billing-focused description does not fully match the broader resource and identity lookup behavior present in the artifact. <br>
Mitigation: Confirm that the intended deployment permits billing queries plus related inventory and identity lookups before granting credentials. <br>


## Reference(s): <br>
- [BSS Python Script Usage Guide](references/bss/guide.md) <br>
- [ClawHub Skill Page](https://clawhub.ai/huaweiclouddev/skills/huawei-cloud-business-support-query) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell commands and JSON query results] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Read-only Huawei Cloud query results may include sensitive billing identifiers, balances, costs, orders, coupon details, and usage records.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
