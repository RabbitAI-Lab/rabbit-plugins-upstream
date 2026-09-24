## Description:

Analyzes videos for mental-health and psychological-behavior indicators and returns structured reports with risk notes, improvement suggestions, and report links.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and care program operators use this skill to submit a person's video file or public video URL to a cloud-backed analysis service, then review structured mental-health findings, suggestions, historical reports, and report links.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Videos of people and derived mental-health reports are sent to the publisher's cloud service.

Mitigation: Use only with explicit subject consent, documented retention and deletion terms, and an accepted data-processing posture for personal or health-related media.

Risk: Security evidence flags under-disclosed cloud handling and plaintext-transport concerns.

Mitigation: Require production HTTPS endpoints and review all configured service URLs before deployment.

Risk: The skill may handle identity values and service tokens while retrieving reports and submitting analysis jobs.

Mitigation: Use safer token storage, avoid exposing internal identity values in user-facing output, and rotate credentials if logs or local files are exposed.

Risk: Mental-health analysis output can be mistaken for clinical diagnosis.

Mitigation: Present results as reference information only and direct users with clear distress or clinical needs to qualified mental-health professionals.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-psychology-analysis)
- [Publisher profile](https://clawhub.ai/user/smyx-sunjinhui)
- [API interface documentation](references/api_doc.md)
- [SMYX analysis API documentation](skills/smyx_analysis/references/api_doc.md)
- [Skill demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Files, Guidance]

**Output Format:** [Markdown or JSON analysis reports with report links; optional saved output file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports local mp4, avi, and mov files up to 10 MB or public video URLs; detail modes include basic, standard, and json.]

## Skill Version(s):

1.0.19 (source: server release metadata; artifact frontmatter says 1.0.15)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
