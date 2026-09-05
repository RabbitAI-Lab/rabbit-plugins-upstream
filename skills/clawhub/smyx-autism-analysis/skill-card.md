## Description:

Analyzes child video or image inputs for autism spectrum disorder behavior indicators and returns structured reports with risk findings, recommendations, and report links.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

External users, caregivers, educators, and professionals can use this skill to submit child behavior media for preliminary ASD-related behavior screening, structured report generation, and historical report lookup. The output is for screening support and should not replace clinical diagnosis or professional medical evaluation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sensitive child-related video, image, or URL inputs may be sent to the publisher's cloud service for analysis.

Mitigation: Use only with informed consent, disclose what media is uploaded and where it is processed, and avoid submitting unnecessary identifying content.

Risk: Reports are cloud-backed and historical report queries may expose retained health-related analysis records.

Mitigation: Tell users where reports are stored, how report links are shared, and how retained reports can be reviewed or deleted.

Risk: The skill may automatically create or reuse an account identity and store local tokens.

Mitigation: Document the identity used for report association, protect local credential storage, and provide a process to remove credentials when access is no longer needed.

Risk: ASD analysis output can be mistaken for a medical diagnosis.

Mitigation: Present results as preliminary screening support and direct users to qualified clinical professionals for diagnosis and care decisions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-autism-analysis)
- [API interface documentation](references/api_doc.md)
- [Analysis API documentation](skills/smyx_analysis/references/api_doc.md)
- [Skill demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [JSON and Markdown report text with report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include ASD-related screening results, risk indicators, recommendations, cloud report URLs, and historical report tables.]

## Skill Version(s):

1.0.13 (source: server release metadata; artifact frontmatter reports 1.0.14)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
