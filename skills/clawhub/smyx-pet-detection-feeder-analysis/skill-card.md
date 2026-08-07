## Description:

Analyzes feeder or IPC camera images and videos to detect cats and dogs, recognize pet identity, support enrollment, and return structured pet-recognition reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to analyze smart-feeder or IPC camera media for pet detection, cat/dog classification, individual pet recognition, pet enrollment, and historical report lookup.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends feeder or IPC camera images/videos, media URLs, pet identity/enrollment data, and report history to cloud services.

Mitigation: Use only with a trusted publisher and service, and confirm users are comfortable sharing this media and pet identity data before deployment.

Risk: The skill may silently manage identities and associate historical reports with locally stored user data.

Mitigation: Review identity handling and report-access behavior before use, and avoid exposing internal identity values in user-facing output.

Risk: The skill may reuse a local API key file, create a local SQLite user database, and store service tokens locally.

Mitigation: Inspect the workspace data directory before and after use, restrict file permissions, and rotate or remove stored credentials when they are no longer needed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-pet-detection-feeder-analysis)
- [Publisher profile](https://clawhub.ai/user/smyx-sunjinhui)
- [Skill demo](https://lifeemergence.com/sample.html)
- [API reference](references/api_doc.md)

## Skill Output:

**Output Type(s):** [text, markdown, json, shell commands]

**Output Format:** [Markdown, JSON, and plain text status or report output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include cloud report links, historical report tables, and optional saved output files.]

## Skill Version(s):

1.0.8 (source: server release metadata; artifact frontmatter says 1.0.12)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
