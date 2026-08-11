## Description:

Identifies babies kicking off blankets or exposing their bodies during sleep and alerts parents to cover them up to prevent catching a cold. | 婴儿蹬被监测技能，识别婴儿夜间睡觉踢开被子、身体裸露，及时提醒家长给宝宝盖被保暖，预防着凉感冒

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

External caregivers and parent-facing agents use this skill to analyze nursery photos, videos, or URLs for baby blanket-kicking or body-exposure events and to retrieve cloud-hosted monitoring reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sensitive nursery media or video URLs are sent to lifeemergence.com cloud services for analysis and history retrieval.

Mitigation: Use only approved media, confirm caregiver consent, and review the service's retention, deletion, and report-history controls before installation.

Risk: The skill can create or reuse local identity records and token state without asking the user for an identity value.

Mitigation: Run the skill in an isolated workspace when evaluating it, inspect local data and token storage, and confirm the default identity behavior matches the deployment's privacy policy.

Risk: Monitoring output is an auxiliary reminder and may be incomplete or incorrect for infant safety decisions.

Mitigation: Treat reports as decision support only, maintain direct caregiver supervision, and verify the nursery camera position, visibility, and crib environment before relying on alerts.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-infant-blanket-kick-monitoring-analysis)
- [API documentation](references/api_doc.md)
- [Skill demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, guidance]

**Output Format:** [Markdown and JSON text with analysis results, recommendations, and report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May save analysis output to a user-specified file; supports basic, standard, and JSON detail modes.]

## Skill Version(s):

1.0.8 (source: server release metadata; artifact frontmatter states 1.0.10)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
