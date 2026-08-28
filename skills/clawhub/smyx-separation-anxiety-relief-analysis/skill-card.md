## Description:

Detects pet separation-anxiety behaviors in uploaded or URL-based home-camera media and returns structured monitoring results, severity context, comfort recommendations, and report links.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

External pet owners, boarding-center staff, and support agents use this skill to analyze pet-alone video or image media for separation-anxiety behavior, severity, and comfort recommendations. Results are for behavior observation and should not be treated as a medical diagnosis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Pet and home-camera media may be uploaded to the configured cloud analysis service.

Mitigation: Use only media that the user is comfortable sending to that service, and review the configured service endpoint before running analysis.

Risk: The skill may create or reuse a workspace identity and store tokens or report history locally.

Mitigation: Review local data files such as data/smyx-api-key.txt and the shared SQLite database before installation or reuse, especially on shared systems.

Risk: Behavior analysis results could be mistaken for medical diagnosis.

Mitigation: Present results as behavior-observation guidance and direct severe or persistent anxiety concerns to a veterinarian or professional behavior specialist.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-separation-anxiety-relief-analysis)
- [API documentation](references/api_doc.md)
- [Shared analysis API documentation](skills/smyx_analysis/references/api_doc.md)
- [Skill demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, files, guidance]

**Output Format:** [Markdown or JSON analysis report with optional saved output file and report link]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can return structured behavior observations, severity context, comfort recommendations, historical report tables, and cloud report export links.]

## Skill Version(s):

1.0.9 (source: server release metadata; artifact frontmatter reports 1.0.11)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
