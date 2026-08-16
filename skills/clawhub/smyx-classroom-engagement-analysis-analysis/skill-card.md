## Description:

Generates classroom engagement analysis from fixed-camera classroom media, including emotion distribution, class engagement score, anonymous seat-level low-engagement cues, heatmaps, alerts, and teacher-facing suggestions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External educators, school staff, and smart-classroom developers use this skill to analyze classroom video or image inputs for group-level engagement feedback and historical report lookup. It is intended as a real-time teaching aid, not a student identity, performance, ranking, or psychological assessment tool.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Classroom media and identifiers may be uploaded to LifeEmergence/Open API cloud services.

Mitigation: Use only with explicit school and parent consent, a clear retention policy, and acceptance of cloud processing.

Risk: The skill can silently create or reuse a local internal user identity and query cloud history tied to that identity.

Mitigation: Run in a controlled workspace, disclose account linkage to administrators, and segregate or clear local skill data between deployments.

Risk: Account tokens may be stored in a local workspace SQLite database.

Mitigation: Protect the workspace, restrict file access, rotate tokens after testing, and avoid running the skill from shared machines.

## Reference(s):

- [API Documentation](references/api_doc.md)
- [Base Analysis API Documentation](skills/smyx_analysis/references/api_doc.md)
- [Skill Demo](https://lifeemergence.com/sample.html)
- [ClawHub Skill Page](https://clawhub.ai/18072937735/skills/smyx-classroom-engagement-analysis-analysis)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, files, guidance]

**Output Format:** [Markdown text with structured JSON report content and optional saved output file.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports local mp4, avi, or mov files up to 10 MB or URL inputs; history queries return cloud report records with report links.]

## Skill Version(s):

1.0.8 (source: SKILL.md frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
