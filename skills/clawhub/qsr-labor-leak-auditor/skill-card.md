## Description:

Real-time labor decision support for restaurant and franchise operators with summary-first mobile-optimized output, including surfaced events, state control, goal tracking, recovery planning, forward planning, event-aware comparisons, hidden-by-default math, standardized output structure, and concise correction handling.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mcphersonai](https://clawhub.ai/user/mcphersonai)

### License/Terms of Use:

Creative Commons Attribution-NonCommercial 4.0 International (CC BY-NC 4.0)

## Use Case:

Restaurant and franchise operators use this skill to track daily and week-to-date labor cost against sales, goals, and operating context before payroll closes. It provides concise in-chat summaries, recovery options, forward target cards, and exportable store-scoped records for operational review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may process confidential store sales, labor totals, average labor cost, and GM base-pay parameters.

Mitigation: Confirm that the host platform and companion memory engine meet the operator's retention, deletion, authentication, export, and access-control requirements before use.

Risk: Operators may accidentally provide personal employee identifiers or individual wage-rate details during labor reviews.

Mitigation: Use roles instead of names where possible, omit unnecessary identifying details, and avoid entering individual wage rates tied to named employees.

Risk: Labor recommendations may be misleading if local operating context is missing or stale.

Mitigation: Review standing rules, event tags, catering, weather, promotions, and manager overrides before acting on staffing changes.

## Reference(s):

- [QSR Labor Leak Auditor on ClawHub](https://clawhub.ai/mcphersonai/skills/qsr-labor-leak-auditor)
- [McPherson AI](https://mcphersonai.com)
- [QSR Labor Leak Auditor README](README.md)

## Skill Output:

**Output Type(s):** [text, markdown, configuration, guidance]

**Output Format:** [Markdown executive summaries and structured text records]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Math is summarized by default; detailed worksheets and scoped exports are returned on request.]

## Skill Version(s):

3.1.3 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
