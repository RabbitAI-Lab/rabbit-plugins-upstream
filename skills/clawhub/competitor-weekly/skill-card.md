## Description:

Generates an evidence-based weekly comparison report for a main Amazon ASIN and authorized competitor products after quote confirmation, using ARI product detail, snapshot, and review data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[funewa](https://clawhub.ai/user/funewa)

### License/Terms of Use:

MIT-0

## Use Case:

External Amazon sellers and operators use this skill to prepare weekly competitor evidence reports for a main ASIN and authorized competitor products after reviewing quote and account requirements. It is intended for review, product-detail, product-snapshot, and competitor comparison workflows, not real-time pricing, sales, inventory, ads, orders, or return-rate reporting.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill receives access to an ARI account and Amazon review or product data.

Mitigation: Install only when that account and data access is acceptable, keep ARI API keys out of reports and examples, and revoke or rotate keys if access is no longer intended.

Risk: Bundled workflows include paid actions and auto-confirm behavior beyond a simple weekly report.

Mitigation: Review quote and confirmation behavior before use, consider turning auto-confirm off, and verify credit impact before confirmed operations.

Risk: Monitoring, scheduling, export, and workbench actions can have ongoing or account-level effects.

Mitigation: Create recurring watches, schedules, exports, or workbench updates only after explicit user intent and review their status in the ARI account.

Risk: The release presents a narrow weekly competitor report while exposing broader CLI capabilities.

Mitigation: Constrain routine use to the intended weekly competitor workflow unless the user deliberately requests another supported ARI capability.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/funewa/skills/competitor-weekly)
- [ARI CLI and API Reference](references/reference.md)
- [Amazon Competitor Weekly Workflow](references/operation-workflow.md)
- [ARI service](https://ari.funewa.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, files, guidance]

**Output Format:** [Markdown reports with CLI command guidance, report URLs, and optional CSV, Markdown, or HTML exports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an ARI API key and may use account-level quote, confirmation, monitoring, export, and report retrieval workflows.]

## Skill Version(s):

1.4.5 (source: server release evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
