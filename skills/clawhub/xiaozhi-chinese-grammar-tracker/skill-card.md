## Description:

Helps students identify and correct six common Chinese sentence-error types, and with consent, maintain a grammar-error profile for persistent patterns, pre-writing reminders, and monthly progress reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

External learners and education agents use this skill to check Chinese grammar errors, guide students through corrections, and track recurring error patterns when the user has consented. It is aimed at upper-primary and middle-school Chinese language learning.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Long-term grammar-error profiles may retain student learning data when profile tracking is enabled.

Mitigation: Enable profile tracking only after explicit consent, and preserve view, correct, delete, pause, sharing-control, and export options.

Risk: Cross-skill sharing or parent-visible summaries could expose student information beyond the intended audience.

Mitigation: Keep cross-skill sharing, parent sharing, and reminders off unless explicitly enabled, and share only the minimum fields needed for the requested workflow.

Risk: Crisis referral contacts may not be appropriate for every country or region.

Mitigation: Verify local emergency and support contacts for the user's region before relying on any crisis-contact information.

Risk: Generated practice items or grammar corrections can be wrong or over-correct valid sentences.

Mitigation: Use the bundled item self-check rules and the high-frequency false-positive list before presenting generated exercises or corrections.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/qizhitang/skills/xiaozhi-chinese-grammar-tracker)
- [Grammar Error Library](artifact/references/grammar-error-library.md)
- [Chinese Error Dimension Table](artifact/shared/chinese-error-dimension-table.md)
- [Learning DNA Profile Schema](artifact/shared/dna-profile.schema.json)
- [Multi-Agent Handover Protocol Schema](artifact/shared/handover-protocol.schema.json)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, guidance]

**Output Format:** [Markdown guidance with optional JSON profile or handover payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May update long-term grammar-error profiles only when consent is enabled; otherwise limited to current-session guidance.]

## Skill Version(s):

2.1.0 (source: server release metadata and artifact frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
