## Description:

Temu 美国站电商退货与退款 API，经 LinkFox 网关转发 Partner US Returns & Refunds / 售后退货退款相关 bg/temu 接口，帮助处理退货申请、退款、售后单查询与退货面单流程。

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External Temu sellers and developers use this skill to query and operate US returns, refunds, after-sales records, return addresses, carriers, signatures, and return-label upload flows through LinkFox-provided scripts and API references.

### Deployment Geography for Use:

United States

## Known Risks and Mitigations:

Risk: The security scan reports broad proxying, account login or payment setup paths, and local storage or printing of sensitive tokens and response data.

Mitigation: Install only if the LinkFox gateway is trusted, review commands before running them, and treat onboarding phone-code and billing actions as account or payment operations.

Risk: Production access tokens and customer, order, refund, or after-sales data may appear in command arguments, terminal output, or saved response files.

Mitigation: Avoid passing production tokens in logged command arguments, keep token stores protected or relocated, use masked token listing in shared environments, and delete saved response files when they are no longer needed.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/linkfox-ai/skills/linkfox-temu-returns-refunds-us)
- [API Reference](references/api.md)
- [Access Token Guide](references/access-token.md)
- [Partner US Returns and Refunds Catalog](references/partner-us-catalog.md)
- [Endpoint Documentation Index](references/apis/README.md)
- [Onboarding and Billing Guidance](references/onboarding.md)
- [Temu Partner US Returns and Refunds Documentation](https://partner-us.temu.com/documentation?menu_code=d3d2812d87034d35adb016972349fcb0)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, JSON files, Guidance]

**Output Format:** [Markdown guidance with shell commands, JSON request examples, and saved JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Scripts may write full LinkFox or Temu responses under the caller's working directory and may print summaries or full JSON depending on response size and flags.]

## Skill Version(s):

1.0.6 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
