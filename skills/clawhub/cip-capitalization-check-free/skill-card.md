## Description:

A free deterministic check for a construction in progress ledger that recomputes cost pooling, cumulative cost roll forward, carrying balance, capitalized interest, and transfer amounts, with findings citing source lines.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

External finance, accounting, and audit-preparation users can run local consistency checks over pasted or file-based construction-in-progress ledger data. The skill helps identify arithmetic and table-consistency issues in cost aggregation, capitalized interest, carrying balance, and transfer-to-fixed-asset amounts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Users may treat arithmetic ledger checks as accounting or audit opinions.

Mitigation: Review results with qualified finance or audit staff; the skill discloses that it does not provide accounting or audit opinions.

Risk: The free version omits several scope checks such as transfer timing, post-transfer cost collection, interrupted-work capitalization, and contract-rate mismatch checks.

Mitigation: Use the output as a table-consistency screen only, and separately review the disclosed out-of-scope items before relying on the ledger.

Risk: CIP ledger data may be sensitive financial information.

Mitigation: Run only in an environment approved for the ledger data; server security evidence describes the checker as local, deterministic, non-networked, and non-persistent.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/cip-capitalization-check-free)

## Skill Output:

**Output Type(s):** [Text, JSON, Shell commands, Guidance]

**Output Format:** [Markdown guidance and optional JSON results from the local Node.js checker]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Findings cite source lines; insufficient input returns missing-field guidance instead of conclusions.]

## Skill Version(s):

1.0.51 (source: server release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
