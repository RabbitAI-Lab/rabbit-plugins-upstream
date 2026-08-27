## Description:

Analyzes night video from a fixed home camera for a person living alone to report lights-off timing, early-morning motion, baseline deviations, and rhythm anomaly reminders.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External caregivers, family members, community care teams, and developers use this skill to analyze night video for sleep-rhythm deviations in a person living alone and retrieve structured cloud reports for follow-up. It provides visual rhythm metrics and reminders, not medical diagnosis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sensitive night-monitoring video, video URLs, identity metadata, and report queries are sent to configured cloud services.

Mitigation: Use only with explicit monitored-person or guardian consent, avoid covert monitoring, minimize footage, and confirm deletion and retention practices before deployment.

Risk: The skill automatically binds requests to persistent identities and stores authentication data while handling highly private footage.

Mitigation: Review identity handling, local credential storage, and cloud report access controls before installing or operating the skill.

Risk: Rhythm anomaly outputs can be mistaken for medical conclusions.

Mitigation: Treat outputs as visual rhythm metrics and follow-up prompts; escalate persistent concerns to qualified caregivers or clinicians.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-living-alone-rhythm-anomaly-analysis)
- [API 接口文档](references/api_doc.md)
- [Supplemental API 接口文档](skills/smyx_analysis/references/api_doc.md)
- [Skill demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration]

**Output Format:** [Markdown and JSON-formatted text reports with optional saved output files and report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can output analysis reports or historical report lists; analysis depends on cloud API responses.]

## Skill Version(s):

1.0.9 (source: server release metadata; artifact frontmatter says 1.0.12)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
