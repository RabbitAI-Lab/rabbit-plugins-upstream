## Description:

AI-powered insurance anti-fraud analysis skill for detecting and preventing insurance fraud across major insurance types, with claim fraud indicators, underwriting risk controls, investigation workflows, and big-data anti-fraud model guidance for the Chinese insurance market.

This skill is ready for commercial/non-commercial use.

## Publisher:

[gechengling](https://clawhub.ai/user/gechengling)

### License/Terms of Use:

MIT-0

## Use Case:

Insurance claims, risk control, underwriting, compliance, and fraud investigation teams use this skill to review fraud indicators, structure risk scoring, plan investigation steps, and draft human-reviewed anti-fraud analysis. It is advisory only and should not be used as the sole basis for claim denial, regulatory reporting, or legal conclusions.

### Deployment Geography for Use:

China

## Known Risks and Mitigations:

Risk: Regulatory statements, scoring thresholds, and workflows may be outdated or incomplete for a live insurance decision.

Mitigation: Verify China-specific regulatory content against current official sources and qualified legal or compliance reviewers before operational use.

Risk: Fraud scores or model outputs could be treated as conclusive evidence and cause incorrect claim denial or escalation.

Mitigation: Use scores only as investigation signals, require independent supporting evidence, and keep human review in the decision process.

Risk: Anti-fraud investigations can involve sensitive personal, medical, financial, and law-enforcement-related data.

Mitigation: Apply data minimization, de-identification, explicit authorization, and documented business necessity before using external or sensitive data.

Risk: Generated reports or referral recommendations could be sent externally before review.

Mitigation: Preview risk scores, investigation reports, and referral recommendations with the user, then require explicit confirmation and legal or compliance review before saving or reporting.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/gechengling/skills/insurance-anti-fraud)
- [Artifact skill definition](artifact/SKILL.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, guidance]

**Output Format:** [Markdown with structured tables, checklists, workflows, and illustrative Python snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Advisory outputs require human review and user confirmation before file creation, external reporting, or operational use.]

## Skill Version(s):

5.0.5 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
