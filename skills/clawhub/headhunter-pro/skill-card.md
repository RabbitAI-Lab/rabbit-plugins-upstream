## Description:

Headhunter Pro v17.0 is an AI-assisted recruiting workflow toolkit for talent gap analysis, candidate screening, recommendation reports, outreach scripts, interview assessment, offer negotiation, onboarding support, and talent pool activation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[walterjiang-sketch](https://clawhub.ai/user/walterjiang-sketch)

### License/Terms of Use:

MIT-0

## Use Case:

Recruiters, talent acquisition teams, and recruiting operations users use this skill to structure end-to-end headhunting work, including candidate scoring, outreach, interview evaluation, client reporting, onboarding follow-up, and talent pool reactivation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Privacy-sensitive recruiting profiles may include candidate contact details, notes, or inferred personal information.

Mitigation: Use documented lawful basis, collect only necessary candidate data, keep outputs in the intended workspace, and define retention and deletion practices before production use.

Risk: Broad credentials or external sourcing workflows could expose unrelated repositories or personal data.

Mitigation: Do not grant broad GitHub repository tokens; prefer read-only, narrowly scoped access and require user confirmation before using external candidate sources.

Risk: Automated follow-up, monitoring, or messaging could contact candidates without review.

Mitigation: Disable cron-style monitoring and automatic messaging by default, and require explicit human approval before outreach or candidate file writes.

Risk: Workspace memory access could include unrelated candidate or business information.

Mitigation: Limit memory reads to relevant recruiting files and remove access to unrelated memory before installing the skill.

## Reference(s):

- [Headhunter Pro on ClawHub](https://clawhub.ai/walterjiang-sketch/skills/headhunter-pro)
- [9+1 Dimension Scoring Standard](references/nine-dimension.md)
- [Recommendation Report v3](references/recommendation-report-v3.md)
- [Outreach Scripts](references/outreach-scripts.md)
- [Pipeline State Machine](references/pipeline-states.md)
- [CRM Engagement Scoring](references/crm-engagement-scoring.md)
- [Brief Drift Detection](references/brief-drift-detection.md)
- [Executive 6D Assessment](references/executive-6d-deep.md)
- [Onboarding Support](references/onboarding-support.md)
- [Talent Pool Activation](references/talent-pool-activation.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown reports, scoring tables, outreach scripts, checklists, and concise recommendations.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs should identify assumptions, avoid fabricating missing facts, and keep candidate personal information within the user's workspace.]

## Skill Version(s):

17.0.0 (source: SKILL.md frontmatter, skill.yml, server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
