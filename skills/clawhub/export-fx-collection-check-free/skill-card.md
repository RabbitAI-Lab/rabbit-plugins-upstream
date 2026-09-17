## Description:

Checks export declaration and FX collection write-off tables by recalculating rows, reconciling totals, and flagging duplicate, blank, or negative entries with source-backed findings.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

Finance and treasury staff use this skill during month-end reconciliation, settlement review, or export documentation checks to identify arithmetic mismatches, missing fields, duplicate declaration numbers, and negative amounts in export declaration and FX collection tables.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The release security summary flags an unsafe external paid-install workflow promoted by the skill.

Mitigation: Use the free local checker only; do not paste the purchase prompt into an agent or run the unpinned @latest installer unless the external package and SkillPay workflow have been independently verified.

Risk: The free checker omits several full-version checks and does not determine tax, export, or foreign-exchange compliance.

Mitigation: Treat results as arithmetic and completeness checks only; verify omitted checks and compliance questions through authoritative records and qualified review.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/export-fx-collection-check-free)

## Skill Output:

**Output Type(s):** [Text, JSON, Shell commands, Guidance]

**Output Format:** [Plain text or JSON findings from a local Node.js checker, with Markdown usage guidance in the skill documentation]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Runs on user-provided table text; the local checker describes no network use, registration, API key, or payment requirement.]

## Skill Version(s):

1.0.3 (source: evidence release and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
