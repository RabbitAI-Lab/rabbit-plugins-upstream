## Description:

Analyzes fixed kitchen camera video or image inputs to detect human presence, stove flame or heat-source status, unattended duration, and stove-left-on alerts for elder-care kitchen safety.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

External caregivers, family members, senior-care operators, and smart-home integrators use this skill to analyze kitchen stove-area media for unattended flame conditions, generate structured reports, and review cloud report history. It supports elder-care kitchen monitoring workflows where alerts require human verification before action.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Private kitchen videos or URLs are processed by a vendor backend.

Mitigation: Use the skill only with consent from the monitored person or authorized caregiver, and avoid submitting media that is outside the intended stove-area monitoring purpose.

Risk: Cloud report history is associated with an automatically resolved user identity and local workspace tokens.

Mitigation: Restrict access to the workspace data directory, protect stored identity and token files, and clear or rotate credentials when the skill is no longer needed.

Risk: Stove-left-on alerts are safety critical and may be wrong or incomplete.

Mitigation: Treat alerts as decision support and require phone, camera, or in-person verification before relying on automated valve actions or emergency response.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-kitchen-stove-left-on-detection-analysis)
- [Skill Demo](https://lifeemergence.com/sample.html)
- [API Interface Documentation](artifact/references/api_doc.md)
- [Supplemental API Documentation](artifact/skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [text, markdown, json, shell commands, guidance]

**Output Format:** [Markdown and JSON text from CLI/API analysis results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May write result text to a local output file when the --output option is used.]

## Skill Version(s):

1.0.6 (source: server release metadata; artifact frontmatter reports 1.0.9)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
