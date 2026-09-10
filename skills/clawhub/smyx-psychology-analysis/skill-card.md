## Description:

Analyzes videos for mental health and psychological behavior signals, identifies common issue tendencies, and produces structured reports with improvement suggestions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Users analyzing uploaded or URL-hosted videos use this skill to generate structured mental health reference reports that estimate stress, anxiety, depression, emotion, behavior, and social-interaction tendencies. The reports are informational and should not be treated as clinical diagnosis or treatment.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may upload mental-health-related videos and query cloud history.

Mitigation: Review data handling, consent, and retention expectations before using the skill with sensitive media.

Risk: The skill silently creates or reuses an internal identity and stores access tokens locally.

Mitigation: Confirm identity handling and local token storage controls before deployment, and avoid exposing internal identifiers in user-facing output.

Risk: The active bundled configuration points sensitive API traffic at plaintext development HTTP endpoints.

Mitigation: Inspect configuration before installation and use approved HTTPS production endpoints for sensitive health-related data.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-psychology-analysis)
- [Skill Demo](https://lifeemergence.com/sample.html)
- [API Documentation](references/api_doc.md)
- [Analysis API Documentation](skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, guidance]

**Output Format:** [Structured Markdown or JSON mental health analysis reports with report links and history tables.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports basic, standard, and JSON detail levels; analysis types include general, emotion, anxiety, depression, stress, and other.]

## Skill Version(s):

1.0.19 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
