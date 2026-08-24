## Description:

Queries Huawei Cloud billing and fee details only when Terraform needs a billing or pricing inquiry, covering balances, bills, coupons, stored-value cards, orders, refunds, costs, free resources, resource usage, enterprise accounts, and on-demand or period pricing for supported services.

This skill is ready for commercial/non-commercial use.

## Publisher:

[huaweiclouddev](https://clawhub.ai/user/huaweiclouddev)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill when Terraform work requires Huawei Cloud billing, bill summary, coupon, balance, refund, order, cost, usage, or pricing details. The skill provides read-only query guidance and script-based checks for supported billing and cloud-resource information.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The billing-only description does not fully match the broader cloud inventory scripts and automatic setup behavior identified by security evidence.

Mitigation: Review the skill before installing and use it only when the broader resource inventory behavior is acceptable for the environment.

Risk: The skill expects Huawei Cloud credentials and can make outbound Huawei Cloud API calls.

Mitigation: Use tightly scoped credentials, preferably temporary and read-only for billing where possible, and avoid exposing credential values in outputs.

Risk: The setup flow may install local dependencies before queries are run.

Mitigation: Run environment setup in a controlled workspace and review dependency installation behavior before deployment.

## Reference(s):

- [BSS Python Script Usage Guide](artifact/references/bss/guide.md)
- [ClawHub Skill Page](https://clawhub.ai/huaweiclouddev/skills/huawei-cloud-business-tf-support)
- [Publisher Profile](https://clawhub.ai/user/huaweiclouddev)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with JSON query results and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs should avoid exposing Huawei Cloud credential values and should be scoped to supported read-only queries.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
