## Description:

短剧创作台的选型评估与私有化搭建指南。

This skill is ready for commercial/non-commercial use.

## Publisher:

[2253128](https://clawhub.ai/user/2253128)

### License/Terms of Use:

MIT

## Use Case:

Developers, technical leads, and operations teams use this skill to decide whether to self-host an AI short-drama production studio, compare licensing and architecture tradeoffs, prepare deployment dependencies, configure model and storage services, and estimate production costs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The documentation presents the skill as offline while also promoting API-key and service channels through WeChat and external sites.

Mitigation: Independently vet any linked service or contact before sharing personal, payment, organization, or production credential information.

Risk: Deployment examples include sudo, system package, database, and service-management commands that can change production hosts.

Mitigation: Review commands before execution and run them only on intended hosts with an approved deployment plan.

Risk: The cost-estimation script uses placeholder pricing and omits some real-world costs such as retries and rework.

Mitigation: Replace placeholder unit prices with current provider quotes and treat results as estimates, not final budgets.

## Reference(s):

- [Selection Scorecard](references/selection-scorecard.md)
- [Deploy and Configure](references/deploy-and-configure.md)
- [Operations and Compliance](references/ops-and-compliance.md)
- [Cost Estimate Script](scripts/cost_estimate.py)
- [Upstream Reference Project](https://gitee.com/forproject/zhenling-drama)

## Skill Output:

**Output Type(s):** [guidance, markdown, shell commands, configuration, code]

**Output Format:** [Markdown guidance with inline shell commands, configuration examples, and a Python cost-estimation script]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The cost-estimation script prints local calculations to the terminal and uses placeholder prices that must be replaced before budgeting.]

## Skill Version(s):

1.0.1 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
