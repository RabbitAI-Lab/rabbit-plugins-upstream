## Description:

Contract Consistency Check (Free) runs local, evidence-based checks for party-name, date, amount, placeholder, cross-reference, and defined-term consistency in contract text.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

External users, employees, and developers use this skill to identify mechanically checkable inconsistencies in contract drafts before final review. It reports evidence-backed findings for the free scope and does not replace legal review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The checker does not provide legal advice or evaluate whether contract terms are fair, enforceable, or commercially favorable.

Mitigation: Use the findings as evidence-backed pre-review signals and have qualified reviewers handle legal and business judgment.

Risk: A clean result only covers the free version's six consistency checks and not the withheld contract-review areas.

Mitigation: Review the reported executed checks and withheld checks before relying on the result, especially for final signing decisions.

Risk: The skill runs a local Node-based checker on potentially sensitive contract text.

Mitigation: Run it only in a trusted local environment and follow the security guidance that no hidden network transfer, persistence, or credential handling was found in the inspected artifacts.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/contract-consistency-check-free)
- [ClawHub publisher profile](https://clawhub.ai/user/chenqg618)

## Skill Output:

**Output Type(s):** [Text, JSON, Guidance]

**Output Format:** [Human-readable text or JSON findings with severity, category, line, message, advice, evidence, summary verdict, executed checks, and withheld checks.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Runs locally on provided contract text; returns insufficient-input status instead of a clean verdict when the material lacks checkable contract elements.]

## Skill Version(s):

1.0.51 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
