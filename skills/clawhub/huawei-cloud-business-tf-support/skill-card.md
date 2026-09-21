## Description:

Queries Huawei Cloud billing and fee details only when Terraform needs a billing or pricing inquiry, covering balances, bills, coupons, stored-value cards, orders, refunds, costs, resource usage, enterprise accounts, and on-demand or period pricing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[huaweicloudskill](https://clawhub.ai/user/huaweicloudskill)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and infrastructure engineers use this skill when Terraform work requires Huawei Cloud billing, fee, balance, order, refund, coupon, enterprise account, resource usage, or pricing queries. It runs local Python query scripts and returns read-only results based on Huawei Cloud API responses.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The billing-focused description does not fully match the broader cloud resource metadata query scripts.

Mitigation: Grant only least-privilege read-only Huawei Cloud credentials and review each requested query against the documented guide before execution.

Risk: Setup and API traffic disable certificate checks while using cloud credentials.

Mitigation: Run only on trusted networks and avoid sensitive or production use until TLS verification and bootstrap behavior are fixed or removed.

Risk: Query output can expose billing, account, and cloud resource metadata.

Mitigation: Treat outputs as sensitive operational data and avoid sharing logs or cached results outside approved channels.

## Reference(s):

- [BSS Python Script Usage Guide](references/bss/guide.md)
- [ClawHub skill page](https://clawhub.ai/huaweicloudskill/skills/huawei-cloud-business-tf-support)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, JSON, Guidance]

**Output Format:** [Markdown guidance with shell commands and JSON query results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Query output may contain billing, account, and cloud resource metadata and should be treated as sensitive.]

## Skill Version(s):

1.0.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
