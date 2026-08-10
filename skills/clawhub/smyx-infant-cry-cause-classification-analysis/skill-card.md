## Description:

Classifies possible causes of infant crying from baby-monitor audio or audio-video input and returns the most likely cause, confidence, and supportive care hints.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to analyze infant cry audio or videos, distinguish likely causes such as hunger, sleepiness, discomfort, need for attention, fear, colic, or unknown, and retrieve prior analysis reports. Results are parenting-support references and are not a substitute for pediatric diagnosis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends baby audio, video, or URLs to remote services for analysis.

Mitigation: Use only with guardian consent and clear expectations for cloud processing, retention, and deletion.

Risk: The skill may silently create or reuse an identity and store account tokens locally.

Mitigation: Review local identity and token handling before deployment and limit use to environments where that persistence is acceptable.

Risk: The skill can retrieve historical reports associated with the local or internal identity.

Mitigation: Confirm that history access, user separation, and report visibility meet privacy requirements before use.

Risk: Cry-cause classification may be wrong or incomplete and could be mistaken for medical advice.

Mitigation: Present outputs as supportive references only and direct caregivers to seek pediatric care for persistent or abnormal crying or other concerning symptoms.

## Reference(s):

- [API Documentation](references/api_doc.md)
- [SMYX Analysis API Documentation](skills/smyx_analysis/references/api_doc.md)
- [Skill Demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [text, markdown, json, shell commands, guidance]

**Output Format:** [Markdown or JSON analysis results with cause labels, confidence, secondary causes, feature summaries, suggestions, and report links.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can produce a single analysis result or a Markdown table of historical cloud reports.]

## Skill Version(s):

1.0.7 (source: server release metadata; artifact frontmatter reports 1.0.9)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
