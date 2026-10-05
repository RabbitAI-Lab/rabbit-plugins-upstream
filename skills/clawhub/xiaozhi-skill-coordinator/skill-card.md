## Description:

Routes Chinese K–12 learning requests to the appropriate study skill and, with user consent, summarizes authorized learning data in a monthly report.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

Chinese K–12 students, with adult supervision for primary grades, use this skill to find the right study support and request a consolidated monthly learning report. Parents and educators can review authorized summaries where sharing permissions allow.

### Deployment Geography for Use:

Mainland China; adapt curriculum, consent practices, and crisis-support contacts before use elsewhere.

## Known Risks and Mitigations:

Risk: Cross-skill summaries and sharing can expose a student's learning or emotional information beyond the intended audience.

Mitigation: Review cross-skill, profile, teacher writeback, parent sharing, and reminder permissions before use; summarize only authorized, task-relevant data.

Risk: Curriculum assumptions, consent practices, and crisis-support contacts may not fit deployments outside mainland China.

Mitigation: Localize the curriculum, consent rules, and crisis-support contacts before deploying elsewhere.

Risk: A monthly report may imply historical coverage when prior learning records are unavailable.

Mitigation: Limit the report to information provided in the current session and clearly state its coverage; do not invent historical figures.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/qizhitang/skills/xiaozhi-skill-coordinator)
- [Publisher profile](https://clawhub.ai/user/qizhitang)
- [One-week learning coordination example](references/one-week-linkage-record.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, JSON]

**Output Format:** [Chinese-language text or Markdown reports; structured handoff data when authorized]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Monthly reports require a user request or consent; the skill does not teach lessons or send reminders itself.]

## Skill Version(s):

2.10.0 (source: skill frontmatter and server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
