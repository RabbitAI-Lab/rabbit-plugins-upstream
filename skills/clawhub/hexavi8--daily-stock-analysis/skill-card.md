## Description:

Deterministic daily stock analysis skill for global equities. Use when users need daily analysis, next-trading-day close prediction, prior forecast review, rolling accuracy, and reliable markdown report output.

This skill is ready for commercial/non-commercial use.

## Publisher:

[hexavi8](https://clawhub.ai/user/hexavi8)

### License/Terms of Use:


## Use Case:

External users and analysts use this skill to create daily equity analysis reports with next-trading-day close forecasts, prior forecast review, rolling accuracy metrics, and self-improvement actions. It supports global equities while requiring users to verify market data from authoritative disclosure, market data, and news sources.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: File-handling scripts may be tricked into writing or moving reports outside the intended workspace.

Mitigation: Install only after review, use trusted ticker and date inputs, avoid migration on untrusted paths, and prefer a fixed version that validates filename components and rejects symlinked report directories.

Risk: Market data or financial conclusions may be stale, conflicting, or misleading if sourced from a single provider.

Mitigation: Cross-check critical values with at least two independent authoritative or high-quality sources and include source timestamps in each report.

Risk: Generated stock forecasts may be mistaken for investment advice or a return guarantee.

Mitigation: Preserve the required informational-use disclaimer and treat recommendations and forecasts as research inputs requiring independent review.

## Reference(s):

- [Daily Stock Analysis Skill Page](https://clawhub.ai/hexavi8/skills/daily-stock-analysis)
- [Workflow](references/workflow.md)
- [Report Template](references/report_template.md)
- [Metrics Definition](references/metrics.md)
- [Authoritative Information Sources](references/sources.md)
- [Security and Privacy Rules](references/security.md)
- [Minimal Compatibility Mode](references/minimal_mode.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown report with YAML frontmatter and supporting shell commands for report planning and accuracy calculation]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces local daily-stock-analysis reports under the user-provided working directory, including recommendation, next-session close forecast, prior review metrics, rolling accuracy fields, improvement actions, source list, and investment-risk disclaimer.]

## Skill Version(s):

1.0.2 (source: ClawHub server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
