## Description:

Checks Chinese insurance commission and handling fee settlement tables for six arithmetic and consistency issues, with row-cited findings and clear insufficient-input responses.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

External finance and cashier teams at insurance intermediaries, agencies, and bancassurance channels use this skill after receiving monthly or quarterly settlement sheets to check commission, handling fee, clawback, tax-withholding, net-receipt, duplicate-settlement, and missing-field consistency before reconciliation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Users may treat arithmetic consistency findings as legal, tax, audit, or regulatory advice.

Mitigation: Present the skill as a settlement-table consistency aid and require finance, compliance, or audit review before using results for filings, recovery, payment, or regulatory decisions.

Risk: The free release omits several higher-level analyses, including cross-institution summaries, sorted remediation lists, and difference attribution.

Mitigation: Make the executed and omitted checks visible in review, and do not infer that out-of-scope categories are error-free.

Risk: Server security evidence reports inaccurate disclosure strings about telemetry behavior.

Mitigation: Review the release disclosure and security summary before deployment, and make any data-sharing or anonymous-usage-statistics behavior clear to users.

## Reference(s):

- [ClawHub skill page: insurance-commission-check-free](https://clawhub.ai/chenqg618/skills/insurance-commission-check-free)
- [ClawHub publisher profile: chenqg618](https://clawhub.ai/user/chenqg618)

## Skill Output:

**Output Type(s):** [text, JSON, guidance]

**Output Format:** [Chinese human-readable text or JSON result objects with findings, summary, scope, sums, and exit-code semantics.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Findings cite source row numbers; insufficient input returns missing requirements instead of conclusions.]

## Skill Version(s):

1.0.1 (source: server release and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
