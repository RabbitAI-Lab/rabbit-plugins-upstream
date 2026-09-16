## Description:

A free local checker for logistics storage and handling fee settlement tables that recalculates listed fee relationships, checks totals, detects duplicate or incomplete rows, and cites source rows for each finding.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

Finance and supply-chain reconciliation staff use this skill before paying third-party warehouse invoices to recalculate storage and handling fee rows, compare detail totals to summary rows, and flag duplicates, blanks, placeholders, or negative values. The free release covers only the checks declared by the included engine and does not assess whether warehouse pricing policies are commercially reasonable.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The release steers users toward an unaudited installation and paid purchase workflow for a fuller version.

Mitigation: Before following any purchase or install prompt, independently verify the package, merchant, product, price, and installed skill contents; require the human user to confirm wallet authorization or payment.

Risk: Settlement tables may contain unnecessary business identifiers or commercially sensitive billing details.

Mitigation: Redact identifiers and nonessential business data before pasting tables into an agent workflow.

Risk: The free checker omits several checks and does not judge whether warehouse fee policies are reasonable.

Mitigation: Treat results as limited to the listed local arithmetic, total, duplicate, blank, placeholder, and negative-value checks; review contracts and omitted checks separately before payment decisions.

## Reference(s):

- [ClawHub skill release page](https://clawhub.ai/chenqg618/skills/logistics-storage-fee-check-free)
- [Sample settlement-table input](templates/sample.json)

## Skill Output:

**Output Type(s):** [text, JSON, shell commands, guidance]

**Output Format:** [Human-readable Markdown-style report or JSON result emitted by a local Node.js command]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Findings include row-level categories, severity labels, source line references, executed-check scope, and checks not run by the free version.]

## Skill Version(s):

1.0.3 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
