## Description:

Analyzes Gmail purchase, booking, subscription, refund, and order emails to estimate spending habits, compare them with cards in a Fleece wallet, and suggest card-use or profile updates.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenyuan99](https://clawhub.ai/user/chenyuan99)

### License/Terms of Use:

MIT-0

## Use Case:

External users with connected Gmail and a Fleece wallet use this skill to estimate spending from purchase-related emails and understand how their saved cards fit observed categories. It supports aggregate spend summaries, missed-rewards estimates, and confirmation-gated Fleece profile updates.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill reads purchase-related Gmail messages and Fleece wallet metadata, which can expose sensitive spending patterns.

Mitigation: Install only when this access is acceptable, keep Gmail handling read-only, extract only essential transaction fields, and report aggregates instead of full message content.

Risk: Recommended Fleece profile updates could change a user's spending profile if accepted without review.

Mitigation: Require explicit user confirmation before running profile update commands, and review each proposed amount before applying it.

Risk: Gmail receipts may undercount or misrepresent actual spending because cash purchases, missing emails, shared accounts, deleted mail, refunds, and cancellations can affect coverage.

Mitigation: State the analysis window and coverage, separate evidence from inference, subtract confirmed refunds, exclude canceled orders, and label low-coverage results as low confidence.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenyuan99/skills/fleece-gmail-spend)
- [Publisher profile](https://clawhub.ai/user/chenyuan99)

## Skill Output:

**Output Type(s):** [markdown, shell commands, guidance]

**Output Format:** [Markdown with tables and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports aggregate spending evidence, category estimates, wallet-fit conclusions, and confirmation-required Fleece profile update commands.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
