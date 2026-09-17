## Description:

This skill checks owner-supplied material ledgers by recomputing issued quantities, issued amounts, and settlement deductions, then flags total mismatches, duplicate rows, missing fields, and negative values with source line references.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

Project cost staff and subcontract settlement staff use this skill during monthly measurement and final settlement to check owner-supplied material ledgers for arithmetic and ledger consistency issues.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: External purchase and package-install guidance conflicts with the skill's offline and no-payment framing.

Mitigation: Use the free local checker only for its local checks; avoid external npx, purchase, or install steps unless the user independently trusts the source and explicitly chooses the separate full product.

Risk: The free checker omits settlement checks such as over-issue analysis and pre-settlement action planning.

Mitigation: Review the checks_not_run list before relying on results, and do not treat a clean free-check result as a complete settlement review.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/chenqg618/skills/owner-supplied-material-check-free)

## Skill Output:

**Output Type(s):** [text, json, shell commands, guidance]

**Output Format:** [Plain text or JSON report from a local Node.js command]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Findings cite source ledger lines; insufficient input returns missing-field guidance rather than conclusions.]

## Skill Version(s):

1.0.1 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
