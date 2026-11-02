## Description:

Analyzes aquarium camera images or video for fish surface-gasping and abnormal breathing patterns, then provides a visual risk warning and suggested next steps.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Aquarium keepers and aquatic facility operators use the skill to review images or video for surface gasping and abnormal breathing, receive visual risk alerts and suggested actions, and retrieve historical reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Video upload and export controls may not reliably limit which aquarium footage reaches LifeEmergence.

Mitigation: Wait for the export-only control to be fixed; approve which footage may be sent and confirm retention practices before use.

Risk: Credential handling and account setup do not yet provide reliable user controls.

Mitigation: Wait for credential handling to be fixed and require explicit account setup before use.

Risk: Emergency alerts lack reliable controls for recipients and repeated notifications.

Mitigation: Specify and approve the alert recipient list and repeat-alert controls before enabling alerts.

Risk: Visual behavior warnings can be mistaken for a confirmed ammonia or disease diagnosis.

Mitigation: Treat results as visual risk warnings only; confirm water conditions with testing and seek qualified aquatic health advice.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/18072937735/skills/smyx-fish-gasping-ammonia-warning-analysis)
- [API reference](references/api_doc.md)
- [Skill demonstration](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Analysis report, Risk warning, Recommendations, Markdown history table]

**Output Format:** [Structured JSON reports and Markdown tables]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports may include observed behavior, alert level, suggested actions, and a report link; results are visual warnings, not a diagnosis.]

## Skill Version(s):

1.0.17 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
