## Description:

The Trade Reviewer's procedure for journaling desk activity and reviewing trades from the exchange record - process graded separately from outcome, execution costs measured, one repeatable finding per review, plus the weekly desk review.

This skill is ready for commercial/non-commercial use.

## Publisher:

[galleonlabs](https://clawhub.ai/user/galleonlabs)

### License/Terms of Use:

MIT-0

## Use Case:

Trading desk operators and agents use this skill after order sends, trade closes, weekly routines, and incident reviews to maintain exchange-backed journals and post-trade reviews. It separates process grading from outcome review and records costs, protection, lifecycle, and one repeatable finding per review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill expects access to trading records and workspace files used for journals and reviews.

Mitigation: Install only where that access is intended, scope file and record access to the trading desk workspace, and review generated journal or review changes before relying on them operationally.

Risk: Vague prompts could trigger operational review or status-update behavior unintentionally.

Mitigation: Use explicit trade IDs, incident IDs, weekly review requests, or clear review prompts when invoking the skill.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/galleonlabs/skills/hypergrok-desk-post-trade-review)

## Skill Output:

**Output Type(s):** [Text, Markdown, Files, Guidance]

**Output Format:** [Markdown journal entries, trade review blocks, weekly reviews, incident reports, and concise status messages]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Append-only journal behavior; reviews rely on exchange records before chat context]

## Skill Version(s):

1.0.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
