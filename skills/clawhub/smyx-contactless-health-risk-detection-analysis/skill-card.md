## Description:

Analyzes frontal face images or videos to produce early health risk screening reports and alerts for chronic and acute conditions such as heart attack, stroke, hypertension, and hyperlipidemia.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and operators in home, community, or elder-care workflows use this skill to run non-contact health risk screening from a frontal face image or short video and retrieve structured reports or report history.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sensitive face images or videos and health-screening results may be sent to configured Life Emergence cloud services.

Mitigation: Use only authorized inputs with informed consent, avoid unnecessary uploads, and review the service's retention and sharing practices before deployment.

Risk: Screening outputs can be mistaken for medical diagnosis.

Mitigation: Present results as early risk screening only and direct users to professional medical care for diagnosis, treatment, or urgent high-risk findings.

Risk: The skill may create or reuse local identity material and persist backend tokens in a local SQLite database.

Mitigation: Restrict workspace and database file access, clear local credentials when no longer needed, and rotate or revoke tokens after shared or temporary use.

Risk: History queries can expose cloud report metadata linked to the active workspace identity.

Mitigation: Confirm the active identity context before listing reports and avoid displaying internal identifiers or report links to unauthorized users.

## Reference(s):

- [API Interface Documentation](references/api_doc.md)
- [Skill Demo](https://lifeemergence.com/sample.html)
- [ClawHub Skill Page](https://clawhub.ai/18072937735/skills/smyx-contactless-health-risk-detection-analysis)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, JSON, Files, Shell commands, Guidance]

**Output Format:** [Markdown or JSON health screening report with optional saved output file and report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports local image/video paths, public media URLs, report-history listing, and basic/standard/json detail modes.]

## Skill Version(s):

1.0.10 (source: server release metadata; artifact frontmatter lists 1.0.12)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
