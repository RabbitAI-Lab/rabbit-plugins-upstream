## Description:

Syncs a Pinduoduo merchant's live catalog, recent trades, and product changes to local SQLite or enterprise ClickHouse, with multi-shop support.

This skill is ready for commercial/non-commercial use.

## Publisher:

[claw-school](https://clawhub.ai/user/claw-school)

### License/Terms of Use:

MIT-0

## Use Case:

Pinduoduo merchants and their agents use this skill to refresh one or more shops' product catalogs, 30-day trade history, and change events for local or enterprise analysis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill accesses logged-in Pinduoduo browser sessions and persistent profile state.

Mitigation: Use a dedicated Chrome or Edge profile and approve browser-profile creation before running.

Risk: Shop and transaction data persist locally or can be sent to a configured ClickHouse endpoint.

Mitigation: Restrict access to the shop data directory and use only trusted PDD_CH_URL destinations.

Risk: Drift diagnostics are sent to Claw School by default when interface changes are suspected.

Mitigation: Set PDD_BUG_REPORT=0 if outbound diagnostics are not approved, and do not use an untrusted PDD_BUG_REPORT_URL.

Risk: Automatic Python installation can change the host environment.

Mitigation: Require explicit approval before installing Python or creating browser profiles.

## Reference(s):

- [PDD Shop Sync on ClawHub](https://clawhub.ai/claw-school/skills/pdd-sync-shop)
- [Claw School](https://claw-school.com)

## Skill Output:

**Output Type(s):** [JSON, Files]

**Output Format:** [Single-line JSON run status and persisted shop snapshots]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Snapshots include catalog, trade, and change data; collection failures include suggested next actions.]

## Skill Version(s):

1.5.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
