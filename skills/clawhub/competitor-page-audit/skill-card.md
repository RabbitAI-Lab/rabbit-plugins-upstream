## Description:

Reviews a main ASIN and authorized competitor product pages for field completeness, expression consistency, and review evidence, producing a comparison issue checklist; it is not for real-time price, sales, inventory, advertising, order, or return-rate judgments.

This skill is ready for commercial/non-commercial use.

## Publisher:

[funewa](https://clawhub.ai/user/funewa)

### License/Terms of Use:

MIT-0

## Use Case:

External Amazon sellers and operators use this skill to compare a primary ASIN with an authorized competitor ASIN, check page-field completeness and consistency against review evidence, and receive a page-audit issue list before making operational decisions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill presents as a competitor page audit but exposes broader ARI Amazon review and operations authority.

Mitigation: Install it only for users who intend to grant that broader ARI authority, and review the available account capabilities before use.

Risk: Paid or auto-confirmed analysis can spend credits without a fresh prompt in some account states.

Mitigation: Check auto-confirm settings before use, prefer quote-only requests for paid work, and avoid broad no-confirm spending thresholds.

Risk: The skill can save an API key locally, export files, enable ongoing collection or monitoring, bind competitors, and update workflow state.

Mitigation: Require explicit user intent for persistent account changes, exports, monitoring, competitor binding, and workflow-state updates.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/funewa/skills/competitor-page-audit)
- [README](artifact/README.md)
- [Dedicated operations workflow](artifact/references/operation-workflow.md)
- [ARI CLI and API reference](artifact/references/reference.md)
- [ARI products](https://ari.funewa.com/zh/products)
- [ARI reports](https://ari.funewa.com/zh/reports)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown reports and concise natural-language summaries, with optional CLI commands and report or export links.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an ARI API key; conclusions depend on ARI account permissions, available product fields, review samples, and paid-operation confirmation state.]

## Skill Version(s):

1.4.7 (source: SKILL.md frontmatter, _meta.json, CHANGELOG, release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
