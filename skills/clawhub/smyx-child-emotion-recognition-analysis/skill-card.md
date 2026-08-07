## Description:

Analyzes child monitoring images, video, and optional audio to classify visible emotional state, intensity, duration, negative-emotion alerts, and soothing guidance for parent, caregiver, or classroom review.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External users, caregivers, educators, and developers use this skill to analyze child-focused video or audio/video inputs for emotion categories such as happy, calm, sad, angry, fear, cry, and surprise, and to retrieve structured historical reports. Outputs should support awareness and communication, not clinical diagnosis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Child video, optional audio, report queries, identity metadata, and generated report links may be sent to configured cloud services.

Mitigation: Install and use only with guardian or institutional consent, confirm authorization for the media being analyzed, and review where reports and tokens are stored before deployment.

Risk: The skill silently creates or reuses identity metadata for analysis and historical report lookup.

Mitigation: Review the configured identity and token handling before installation, and restrict use to environments where account association and report retention are acceptable.

Risk: Emotion classifications and soothing suggestions can be mistaken for clinical or psychological advice.

Mitigation: Present outputs as communication support only; do not use them as diagnosis, and seek professional help for persistent or concerning negative emotions.

## Reference(s):

- [Child Emotion Recognition API Documentation](references/api_doc.md)
- [Shared Analysis API Documentation](skills/smyx_analysis/references/api_doc.md)
- [Skill Demo](https://lifeemergence.com/sample.html)
- [ClawHub Skill Page](https://clawhub.ai/18072937735/skills/smyx-child-emotion-recognition-analysis)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, configuration, guidance]

**Output Format:** [Markdown or JSON structured analysis report with emotion fields, alerts, soothing hints, and report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May save the generated report to a user-specified output file.]

## Skill Version(s):

1.0.19 (source: server release metadata; artifact frontmatter reports 1.0.7)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
