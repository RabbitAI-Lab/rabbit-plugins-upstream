## Description:

A free deterministic checker for Chinese-style trial balance sheets that recomputes closing balances, checks profit-and-loss closeout, validates debit and credit totals, checks parent and child account subtotals, and flags duplicate, blank, or invalid cells with source line numbers.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

Accounting staff, finance managers, and auditors use this skill before monthly close or audit preparation to check arithmetic consistency in a pasted or JSON-wrapped account balance table. It returns line-cited findings and clearly lists checks that the free edition does not run.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill includes paid-upgrade prompts and an optional flow that asks an agent to install an unpinned external payment package.

Mitigation: Verify the payment provider, package, version, and platform rules before running any payment-install command; require the user to personally confirm wallet authorization or payment.

Risk: The skill writes a local marker file for upsell tracking.

Mitigation: Run the skill in a controlled workspace or sandbox and review local file writes before deployment in shared environments.

Risk: The free edition performs deterministic trial-balance checks but omits paid checks for imbalance attribution and pre-close adjustment lists.

Mitigation: Present withheld checks clearly and treat outputs as arithmetic consistency findings that still require qualified accounting review.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/trial-balance-check-free)
- [Skill definition](artifact/SKILL.md)
- [Sample input template](artifact/templates/sample.json)

## Skill Output:

**Output Type(s):** [Text, JSON, Guidance]

**Output Format:** [Plain text or JSON containing line-cited accounting check results, missing-input messages, executed checks, withheld checks, and scope notes.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Runs locally over one supplied trial balance table; the free edition omits paid upgrade checks for imbalance attribution and pre-close adjustment lists.]

## Skill Version(s):

1.0.2 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
