## Description:

Through fixed cameras and optional microphones, this skill analyzes pregnancy-related emotional fluctuation signals such as crying, frowning, anxious behavior, prolonged silent sitting, and impatient conversation tone, then produces structured reports and suggested soothing actions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External users and care-oriented operators can use this skill to analyze authorized audio or video from a pregnant person's home or prenatal waiting-room setting and review structured emotion-monitoring reports, report links, and suggested soothing or escalation actions. It is not a medical diagnosis tool.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill handles sensitive audio/video-derived observations about a pregnant person's emotions and behavior.

Mitigation: Install only with explicit opt-in from the monitored person, inform household or clinic bystanders, and limit inputs to trusted, authorized media sources.

Risk: The skill can access cloud report history and use silent identity/account handling.

Mitigation: Review identity, token, local SQLite, and cloud report retention paths before deployment, and document how users can delete local and cloud records.

Risk: Automatic spouse or emergency-contact escalation can create privacy, consent, or relationship-safety concerns.

Mitigation: Configure spouse and emergency notifications intentionally, verify recipient consent and contact accuracy, and require human review for escalation policies.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/18072937735/skills/smyx-pregnancy-emotion-soothing-analysis)
- [Publisher Profile](https://clawhub.ai/user/18072937735)
- [API Documentation](references/api_doc.md)
- [Skill Demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, guidance]

**Output Format:** [JSON or Markdown reports with detected events, soothing-action recommendations, history tables, and report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May query cloud report history and return sensitive audio/video-derived observations; outputs should be reviewed before operational use.]

## Skill Version(s):

1.0.9 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
