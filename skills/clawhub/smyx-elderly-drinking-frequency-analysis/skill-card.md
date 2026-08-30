## Description:

Analyzes fixed-camera video of an older adult's cup area to count cup-pickup events as an indirect drinking-frequency signal and emit dehydration-risk reminders when configured thresholds or intervals indicate concern.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External caregivers, family members, and elder-care operators use this skill to analyze home or care-facility video of a cup area, generate daily pickup-frequency reports, and decide when to remind an older adult to drink. It provides behavior statistics and directional risk alerts, not a medical diagnosis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sensitive home or care-facility video may be sent to remote services.

Mitigation: Use only with informed consent from the elderly person or guardian, and verify endpoint ownership, retention policy, access controls, and transport protections before deployment.

Risk: Hidden local identity reuse can link multiple reports, especially in shared workspaces.

Mitigation: Run the skill in an isolated workspace or account and verify account isolation and token storage before using history or report-list features.

Risk: Cup-pickup events are an indirect proxy for drinking and can be wrong when cups are shared, moved by others, or not filled with water.

Mitigation: Treat alerts as caregiver prompts, combine them with direct observation or personal baselines, and avoid using the output as a medical diagnosis.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/18072937735/skills/smyx-elderly-drinking-frequency-analysis)
- [Skill Demo](https://lifeemergence.com/sample.html)
- [API Documentation](artifact/references/api_doc.md)
- [Shared API Error Reference](artifact/skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown text with structured JSON-like analysis content and report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May save the analysis response to a caller-specified output file.]

## Skill Version(s):

1.0.9 (source: server release metadata; artifact frontmatter reports 1.0.11)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
