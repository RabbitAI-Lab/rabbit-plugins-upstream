## Description:

Advisory skill for insurance claims processing workflows that provides templates, checklists, and decision-support frameworks for medical OCR, liability determination, anti-fraud assessment, and claims reporting.

This skill is ready for commercial/non-commercial use.

## Publisher:

[gechengling](https://clawhub.ai/user/gechengling)

### License/Terms of Use:

MIT-0

## Use Case:

External insurance operations teams, claims reviewers, and developers use this skill to draft claims workflow guidance, OCR review checklists, liability review notes, anti-fraud triage prompts, and claims report templates. All claim decisions, payout amounts, denial language, and fraud labels require qualified human review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Claims guidance may affect sensitive insurance outcomes if used as a final decision.

Mitigation: Use outputs only as drafts and require a qualified insurance professional to review all claim decisions, payout amounts, denial language, and fraud labels before use.

Risk: Claims workflows may involve personal, medical, or identifying data.

Mitigation: Do not paste unnecessary personal or medical data; redact identifiers where possible and follow data minimization practices before OCR or analysis.

Risk: Regulatory references and compliance practices can change over time.

Mitigation: Verify regulatory references against current official sources before relying on them in claims handling or reporting.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/gechengling/skills/insurance-claims-intelligence)
- [Skill source artifact](artifact/SKILL.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Configuration, Guidance]

**Output Format:** [Markdown drafts with checklists, tables, report templates, and illustrative code snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs are advisory drafts and must include a human-review disclaimer before operational use.]

## Skill Version(s):

5.0.5 (source: frontmatter, release metadata, changelog)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
