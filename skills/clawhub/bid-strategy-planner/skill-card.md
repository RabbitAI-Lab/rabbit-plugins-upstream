## Description: <br>
Bid Strategy Planner helps choose a paid-campaign bidding strategy, derive an initial tCPA or tROAS target from campaign history, map portfolio groupings, and plan learning-phase entry. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[aaron-he-zhu](https://clawhub.ai/user/aaron-he-zhu) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Marketing operators and growth teams use this skill to select a bid strategy for new or restructured paid campaigns and to set a defensible starting target from CPA, ROAS, conversion volume, and funnel-stage evidence. It is intended for planning and handoff, not for directly changing ad-account settings. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Campaign CPA, ROAS, conversion volume, budgets, and related business metrics can expose sensitive business performance data. <br>
Mitigation: Use trusted connector or export flows, avoid pasting credentials, and grant only the access needed to support planning. <br>
Risk: Saved planning notes can preserve outdated or unreviewed bid-strategy assumptions as durable decisions. <br>
Mitigation: Review saved memory notes and keep durable choices in a pending-decision flow until the campaign owner confirms them. <br>
Risk: Bid targets based on incomplete, guessed, or stale metrics can lead to misleading campaign plans. <br>
Mitigation: Label metrics as Measured, User-provided, or Estimated, and request a GA4 or ecommerce export when target math lacks required evidence. <br>


## Reference(s): <br>
- [Bid Strategy Matrix](references/bid-strategy-matrix.md) <br>
- [ClawHub skill page](https://clawhub.ai/aaron-he-zhu/skills/bid-strategy-planner) <br>
- [Project homepage](https://github.com/aaron-he-zhu/aaron-marketing-skills) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance] <br>
**Output Format:** [Markdown planning response with optional saved Markdown memory note] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes bid-strategy recommendation, target math, portfolio grouping map, and learning-phase entry plan.] <br>

## Skill Version(s): <br>
19.0.0 (source: frontmatter, server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
