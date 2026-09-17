## Description:

A free local checker for construction retention-money ledgers that recomputes withheld amounts, warranty expiry dates, and refundable amounts, then flags total, duplicate, blank, and date issues with source ledger line citations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

Project accountants, cost staff, and infrastructure finance teams use this skill during settlement and warranty refund reviews to check construction retention-money ledgers before deciding whether funds should be retained or returned.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The release embeds paid upgrade instructions that ask users to run an unpinned external installer and install another skill.

Mitigation: Use the free checker only for local deterministic ledger arithmetic; run the payment installer or paid-skill installation only after independently verifying the provider, source, and remote code execution/payment flow.

Risk: The free version omits checks for contract rate caps, deduction reasonableness, overdue refund scheduling, actionable follow-up lists, and early refund detection.

Mitigation: Review the omitted checks before making retention-money decisions that depend on those areas, and do not treat the free result as covering paid-only checks.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/retention-money-check-free)

## Skill Output:

**Output Type(s):** [Text, JSON, Shell commands, Guidance]

**Output Format:** [Human-readable text or JSON from a local Node.js command]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Runs locally with Node.js standard library; reports insufficient input instead of producing unsupported conclusions.]

## Skill Version(s):

1.0.3 (source: server evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
