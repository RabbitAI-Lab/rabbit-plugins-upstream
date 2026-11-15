## Description:

覆盖健康审核、医学评估、核保结论解读、回访跟进、双录质检全流程。帮助核保人员提升健康风险评估准确性和工作效率。

This skill is ready for commercial/non-commercial use.

## Publisher:

[gechengling](https://clawhub.ai/user/gechengling)

### License/Terms of Use:

MIT-0

## Use Case:

Insurance underwriting staff use this skill as a workflow reference to review health disclosures, structure medical assessments, explain draft underwriting outcomes, prepare follow-up guidance, and check sales-recording compliance. Outputs are advisory drafts for qualified human review and execution.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review is benign with medium confidence, but its Skillspector analysis was partial because two linked references were missing.

Mitigation: Treat the review as incomplete; check available supporting guidance and confirm the skill's underwriting scope before relying on it.

Risk: The workflow may involve sensitive health and identity data and may produce draft underwriting recommendations.

Mitigation: Minimize and redact personal data before input, and require an authorized qualified reviewer to verify recommendations before use; keep customer contact and institutional actions with authorized personnel.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/gechengling/skills/underwriting-expert-digital-employee)

## Skill Output:

**Output Type(s):** [Analysis, Guidance, Markdown]

**Output Format:** [Structured Markdown reports, checklists, explanations, and draft communication text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Advisory drafts require qualified human review; the skill does not contact customers or execute institutional workflows.]

## Skill Version(s):

2.0.9 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
