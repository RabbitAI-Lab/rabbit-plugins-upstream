## Description:

Checks IP annuity and renewal ledgers for calculable date, fee, duplicate-application-number, blank-field, cycle, and date-order issues, with findings tied to source line numbers.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

Legal, intellectual-property operations, and finance reviewers use this skill to check copied patent, trademark, and copyright annuity or renewal ledgers before payment and deadline review. It recalculates ledger relationships and flags missing or inconsistent rows, but does not replace official deadline monitoring, fee schedules, payment confirmation, or legal advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Users could treat ledger checks as official fee, deadline, payment, or legal determinations.

Mitigation: Verify business-critical results against original records, official deadline systems, current fee schedules, payment confirmations, and qualified legal review.

Risk: The free version intentionally omits several checks, including overdue action lists, 90/180-day schedules, status-versus-payment consistency, duplicate charging, and agent-fee outlier review.

Mitigation: Review the withheld-check list before relying on the output and perform those checks separately when they are relevant.

Risk: The skill runs local Node.js code on IP ledger data.

Mitigation: Install only from the expected ClawHub release, review the clean scan summary and file hashes, and run it in an environment appropriate for sensitive ledger data.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/ip-annuity-check-free)
- [Skill instructions](artifact/SKILL.md)
- [Local runner](artifact/scripts/run.mjs)
- [Sample input](artifact/templates/sample.json)

## Skill Output:

**Output Type(s):** [text, JSON, guidance]

**Output Format:** [Human-readable terminal text or structured JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Findings cite source line numbers; insufficient input returns missing fields rather than a pass/fail conclusion.]

## Skill Version(s):

1.0.18 (source: server-resolved release and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
