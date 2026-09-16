## Description:

Analyzes privacy-reduced bathroom doorway or silhouette-only bathroom video to track an older adult's toilet occupancy time and produce abnormal-stay alerts when the configured threshold is exceeded.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Caregivers, nursing-home operators, and home-safety developers use this skill to analyze bathroom monitoring video or URLs, detect entry and exit events, calculate continuous occupancy duration, and surface alerts or historical reports. It is an auxiliary monitoring tool and does not provide medical diagnosis or rescue instructions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Highly sensitive bathroom-monitoring footage may be uploaded to a remote service.

Mitigation: Use only with informed consent, enforce HTTPS production endpoints, and reduce privacy exposure before upload by installing cameras at the doorway or applying silhouette-only, blurred, or pixelated capture.

Risk: The skill creates or reuses an internal identity and stores service tokens locally.

Mitigation: Protect local token storage, restrict filesystem access, and review token handling before installing or running the skill.

Risk: Alerts can be mistaken for medical or rescue guidance.

Mitigation: Treat output as auxiliary occupancy monitoring; require human verification for urgent alerts and avoid using the skill as a medical diagnostic system.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-elderly-toilet-time-abnormal-analysis)
- [Publisher profile](https://clawhub.ai/user/18072937735)
- [Skill demo](https://lifeemergence.com/sample.html)
- [API documentation](references/api_doc.md)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, guidance]

**Output Format:** [Markdown or JSON report text with alert fields, report links, and optional saved output files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May call remote analysis and history APIs, upload local video files, poll for results, and return report-export links.]

## Skill Version(s):

1.0.11 (source: server release metadata; artifact frontmatter says 1.0.13)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
