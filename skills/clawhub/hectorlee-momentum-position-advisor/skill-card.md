## Description:

This skill analyzes price-volume momentum for A-share holdings and produces hold, watch, reduce, sell, and position-sizing guidance using technical patterns and scoring.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xiyanjun](https://clawhub.ai/user/xiyanjun)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to diagnose stock positions, scan market momentum patterns, and summarize whether a position should be held, watched, reduced, or sold. Its outputs are informational technical-analysis guidance and should not be treated as automated trading decisions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill reads portfolio files and writes prior decision state locally, which can expose or persist sensitive holdings data.

Mitigation: Run it only in a trusted workspace, review the portfolio file path before use, and remove local decision-state files when they are no longer needed.

Risk: The skill imports code from another installed skill without a pinned version.

Mitigation: Review the installed volume-price screener dependency before use and keep the dependency under change control for repeatable results.

Risk: The skill can produce strong reduce, sell, and position-size guidance for real holdings.

Mitigation: Treat outputs as informational technical analysis, validate them against independent sources, and require human review before any financial action.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/xiyanjun/skills/hectorlee-momentum-position-advisor)
- [Pattern rules](references/pattern_rules.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Console text and Markdown-style summaries with inline shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include stock codes, scores, pattern labels, warnings, hold/reduce/sell/watch decisions, and optional position-size guidance.]

## Skill Version(s):

0.1.3 (source: server release metadata; artifact frontmatter: 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
