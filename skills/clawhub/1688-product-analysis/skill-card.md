## Description:

1688-product-analysis helps 1688 sellers diagnose product performance by combining seller and product data for multi-shop abnormal product discovery, scoring-based product selection, keyword search, competitive comparison, and single-product diagnosis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[1688aiinfra](https://clawhub.ai/user/1688aiinfra)

### License/Terms of Use:

MIT-0

## Use Case:

1688 sellers and commerce operations teams use this skill to find products that need attention, inspect traffic, sales, add-to-cart, conversion, advertising, and competitor signals, and generate actionable product diagnosis reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill connects to a 1688 seller account and queries authenticated seller and product data.

Mitigation: Install and run it only for accounts where this access is intended, and verify ALI_1688_AK/OpenClaw configuration before use.

Risk: Generated reports and local caches can contain seller-specific product and performance information.

Mitigation: Store generated reports and cache files in trusted workspaces and avoid sharing them outside the intended operations team.

Risk: Follow-up optimization and scheduled diagnosis workflows could affect seller operations if invoked unintentionally.

Mitigation: Require explicit user confirmation before optimization or scheduling actions, as described by the security guidance and artifact behavior.

Risk: Command-level usage telemetry is sent to the 1688 gateway.

Mitigation: Use the skill only where this telemetry is acceptable under the seller account's operational and privacy policies.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/1688aiinfra/skills/1688-product-analysis)
- [Analysis dimensions](references/analysis-dimensions.md)
- [Report template](references/report-template-simple.md)
- [Interaction specifications](references/interaction-specs.md)
- [Scoring rules](references/scoring-rules.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance, Configuration]

**Output Format:** [Markdown reports with structured product-selection interactions and JSON command results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Python 3 and a configured ALI_1688_AK/OpenClaw environment for authenticated 1688 seller data access.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
