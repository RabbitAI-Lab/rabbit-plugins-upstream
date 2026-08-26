## Description:

Combines facial blood flow and emotional characteristics to analyze stress index, anxiety tendency, and depression tendency for mental health monitoring scenarios.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Employees, external users, and developers can use this skill to submit face images or videos for cloud-backed psychological stress assessment, including stress index, anxiety tendency, depression tendency, suggestions, report links, and historical report lookup.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uploads face images or videos for cloud-backed mental-health and biometric-style analysis.

Mitigation: Use only with explicit user consent and clear disclosure of the remote service, data upload, retention, and report access behavior.

Risk: The skill silently creates or reuses a persistent identity and may store tokens in the workspace data directory.

Mitigation: Review identity and token handling before installation, restrict workspace access, and rotate or remove stored credentials when no longer needed.

Risk: Assessment output could be mistaken for clinical diagnosis.

Mitigation: Present results as reference-only mental health screening information and direct users with persistent concerns to qualified professionals.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-psychological-stress-assessment-analysis)
- [Skill Demo](https://lifeemergence.com/sample.html)
- [API Interface Documentation](references/api_doc.md)
- [Shared Analysis API Documentation](skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [text, markdown, json, shell commands, guidance]

**Output Format:** [Markdown or JSON assessment output with report links and optional saved result files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports basic, standard, and JSON detail levels; historical reports are returned as Markdown tables.]

## Skill Version(s):

1.0.11 (source: server release metadata; artifact frontmatter lists 1.0.14)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
