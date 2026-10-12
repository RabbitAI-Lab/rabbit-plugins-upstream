## Description:

Checks Pinduoduo shop inventory for stockouts, low stock, overstock, and slow-moving items, with replenishment advice based on customizable merchant thresholds.

This skill is ready for commercial/non-commercial use.

## Publisher:

[claw-school](https://clawhub.ai/user/claw-school)

### License/Terms of Use:

MIT-0

## Use Case:

Pinduoduo merchants and their agents use this skill to prioritize restocking and clearance actions using synced inventory and recent sales data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Shop inventory and sales data may be stored locally or handled by a configured ClickHouse endpoint.

Mitigation: Review storage locations and use a trusted, preferably HTTPS, ClickHouse endpoint when configuring PDD_CH_URL.

Risk: Custom database or policy paths could point to sensitive or shared system locations.

Mitigation: Keep PDD_DB_PATH and PDD_RESTOCK_POLICY within an appropriate private data directory.

Risk: Stale inventory snapshots may lead to outdated replenishment advice.

Mitigation: Check the output's as_of timestamp and sync shop data before acting on results older than 24 hours.

## Reference(s):

- [PDD Restock Check on ClawHub](https://clawhub.ai/claw-school/skills/pdd-check-restock)
- [Claw School](https://claw-school.com)

## Skill Output:

**Output Type(s):** [Text, JSON, Guidance]

**Output Format:** [Plain-text action list or structured JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes the data timestamp, decision methodology, restock quantities, and optional first-use guidance.]

## Skill Version(s):

1.1.0 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
