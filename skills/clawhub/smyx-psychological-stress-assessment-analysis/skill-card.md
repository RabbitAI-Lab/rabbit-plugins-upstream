## Description:

Combines facial blood flow and emotional characteristics to analyze stress index, anxiety tendency, and depression tendency, suitable for mental health monitoring scenarios.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to assess psychological stress signals from face images or videos and retrieve structured stress, anxiety tendency, and depression tendency reports. The results are presented as wellness-oriented assessment information and are not a substitute for professional mental-health care or clinical diagnosis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Face images or videos and mental-health assessment outputs may be uploaded to third-party services.

Mitigation: Use only with explicit user consent, review the provider's privacy and retention terms, and avoid sensitive or regulated mental-health workflows unless contractual controls are in place.

Risk: Reports may be associated with persistent local or cloud identities and tokens.

Mitigation: Confirm identity handling, token storage, deletion, and access controls before deployment, and limit access to authorized users.

Risk: Stress, anxiety, and depression tendency outputs may be mistaken for clinical diagnosis.

Mitigation: Present results as wellness-oriented assessment support and direct users to qualified professionals for persistent abnormalities or clinical decisions.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-psychological-stress-assessment-analysis)
- [Skill Demo](https://lifeemergence.com/sample.html)
- [API Documentation](references/api_doc.md)
- [Analysis API Documentation](skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, API calls, guidance]

**Output Format:** [Markdown or JSON structured assessment report with report links when available]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include stress index, anxiety tendency, depression tendency, suggestions, history tables, and cloud report links.]

## Skill Version(s):

1.0.10 (source: server release metadata; artifact frontmatter lists 1.0.14)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
