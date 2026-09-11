## Description:

Orchestrates A-share trading SOP workflows by routing natural-language requests to pre-market, intraday, post-market, single-stock research, or first-limit overnight decision chains and summarizing the resulting operational guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[fize](https://clawhub.ai/user/fize)

### License/Terms of Use:

MIT-0

## Use Case:

External users and trading-research agents use this skill to coordinate structured A-share market analysis workflows and produce decision summaries for daily planning, stock research, and overnight first-board strategies.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can produce actionable trading analysis that may be incorrect or misleading.

Mitigation: Treat recommendations as informational, require user review before acting, and stop the workflow when required market data or dependent skill output is unavailable.

Risk: The optional dashboard was flagged for unsafe unauthenticated report APIs and vulnerable HTML rendering.

Mitigation: Run the dashboard only on localhost, avoid loading untrusted or imported report files, and review or harden the web surface before broader exposure.

## Reference(s):

- [Trading SOP ClawHub release](https://clawhub.ai/fize/skills/trading-sop)
- [SOP-A Daily Research Workflow](references/sop-a-daily.md)
- [SOP-B Single-Stock Research Workflow](references/sop-b-stock.md)
- [SOP-C First-Board Overnight Workflow](references/sop-c-firstboard.md)
- [SOP Summary Template](templates/sop_summary.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown reports and concise text summaries, with optional shell commands for the local report dashboard]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May write report Markdown under the workspace report/ directory and can expose a localhost dashboard when explicitly started by the user.]

## Skill Version(s):

1.0.0 (source: SKILL.md frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
