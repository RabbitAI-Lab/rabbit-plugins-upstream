## Description:

Checks hotel OTA commission and net settlement statements by recalculating commissions, net settlement amounts, totals, duplicate channels, and missing fields, with each finding tied to source line evidence.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

Hotel and homestay operators use this skill to check monthly OTA settlement tables from channels such as Ctrip, Meituan, and Fliggy. It helps verify arithmetic consistency for commission, net settlement, column totals, duplicate channel rows, and required fields before relying on the statement.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The release security summary says the free checker is local, but the skill also includes an optional paid-upgrade prompt involving an unpinned remote installer and purchase flow.

Mitigation: Use the local free checker only when needed, and require independent verification of package version, source, payment flow, and installed skill before allowing an agent to run the installer or initiate purchases.

Risk: The checker intentionally omits paid-tier checks such as commission-rate range, negative net settlement, negative other-fee, and high combined-fee detection.

Mitigation: Treat passing output as confirmation of only the listed free checks, and review omitted checks separately when those risks matter.

Risk: The checker does not validate channel contract terms, tax treatment, promotion settlement differences, or order-level details.

Mitigation: Use source contracts, tax guidance, channel documentation, or order-level reconciliation for decisions outside the stated arithmetic table checks.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/ota-commission-check-free)

## Skill Output:

**Output Type(s):** [Analysis, JSON, Markdown, Shell commands, Guidance]

**Output Format:** [Human-readable console output or JSON result containing findings, summaries, executed checks, withheld checks, and missing-input guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Runs locally with Node.js standard libraries, cites source line numbers, and returns insufficient-input status rather than conclusions when required table fields are missing.]

## Skill Version(s):

1.0.3 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
