## Description:

Provides 1688 shop health checks across traffic, inquiries, transactions, products, customers, advertising, and risk, producing summary conclusions, an HTML data report, and prioritized follow-up actions for one or more bound shops.

This skill is ready for commercial/non-commercial use.

## Publisher:

[1688aiinfra](https://clawhub.ai/user/1688aiinfra)

### License/Terms of Use:

MIT-0

## Use Case:

External 1688 merchants and shop operators use this skill to diagnose shop performance, compare bound shops, identify operational risks, and choose prioritized optimization actions after the report.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can access 1688 shop and business data.

Mitigation: Install and run it only in environments where that data access is intended and authorized.

Risk: The skill can store a 1688 AK in OpenClaw configuration.

Mitigation: Confirm credential storage is acceptable before configuration and rotate or remove the AK when access is no longer needed.

Risk: The skill may install packages automatically.

Mitigation: Use an environment where automatic package installation is acceptable, or disable/review package installation before execution.

Risk: The skill can propose follow-up action cards and scheduled daily diagnostics.

Mitigation: Review action cards before confirming and enable scheduling only when recurring diagnostics are intended.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/1688aiinfra/skills/1688-shop-health-check)
- [Publisher profile](https://clawhub.ai/user/1688aiinfra)
- [Analysis methodology](artifact/references/analysis-methodology.md)
- [CLI commands](artifact/references/cli-commands.md)
- [Interaction specs](artifact/references/interaction-specs.md)
- [Wiki routing rules](artifact/references/wiki-routing-rules.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance, Files]

**Output Format:** [Chinese Markdown summary plus an HTML report file and interactive action-card options]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include JSON command results, generated report files, and follow-up scheduling or optimization guidance.]

## Skill Version(s):

1.4.0 (source: ClawHub release metadata; artifact frontmatter reports 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
