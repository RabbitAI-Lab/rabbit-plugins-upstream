## Description:

This skill analyzes classroom or desk-camera video of a child to estimate visual fatigue indicators such as PERCLOS, head nodding, eye-region changes, and a 0-100 fatigue score.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

External educators, parents, and classroom support workflows can use this skill to submit child learning-area media for structured fatigue and drowsiness assessment. It returns visual-only fatigue signals, rest guidance, and report links without presenting the result as a medical or sleep-disorder diagnosis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill handles highly sensitive child facial video and uploads media to cloud services.

Mitigation: Use only with clear guardian consent, approved retention and deletion terms, and a deployment that protects media in transit and at rest.

Risk: The security evidence reports an unsafe, under-scoped cloud workflow and plaintext development endpoints in the packaged defaults.

Mitigation: Require a production HTTPS-only configuration and review all endpoint settings before real child media is processed.

Risk: The skill silently creates or reuses an internal identity and stores tokens locally.

Mitigation: Limit execution to trusted workspaces, protect local credential storage, and verify identity handling before enabling history lookups.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-child-drowsiness-fatigue-detection-analysis)
- [Skill Demo](https://lifeemergence.com/sample.html)
- [API Documentation](references/api_doc.md)
- [Shared Analysis API Documentation](skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, configuration, guidance]

**Output Format:** [Markdown text with structured JSON-style fatigue analysis, history-list output, and report links.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May save the returned report text to a caller-specified output file.]

## Skill Version(s):

1.0.9 (source: server release metadata; SKILL.md frontmatter says 1.0.14)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
