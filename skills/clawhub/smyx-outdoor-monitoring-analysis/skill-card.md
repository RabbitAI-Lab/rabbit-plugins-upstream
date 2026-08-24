## Description:

Detects people, vehicles, non-motorized vehicles, and pets in outdoor monitoring images or videos, then returns structured monitoring reports for courtyards, orchards, farms, and similar areas.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External users and site operators use this skill to analyze outdoor surveillance images or videos for target detection, intrusion assessment, risk level reporting, and historical monitoring report lookup.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Media files, media URLs, and identity-bearing requests are sent to configured remote services.

Mitigation: Use the skill only with media and URLs approved for those services, and confirm trust in the publisher and LifeEmergence/Open API endpoints before deployment.

Risk: The skill silently creates or reuses a local identity and stores service tokens in a workspace SQLite database.

Mitigation: Deploy in a controlled workspace, review local data storage handling, and avoid sharing workspaces that may contain service tokens.

Risk: Outdoor surveillance analysis can produce incorrect or incomplete detections and risk assessments.

Mitigation: Treat outputs as security-supporting analysis only and require human review for operational or emergency decisions.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/18072937735/skills/smyx-outdoor-monitoring-analysis)
- [Skill Demo](https://lifeemergence.com/sample.html)
- [Outdoor Monitoring API Documentation](references/api_doc.md)
- [Shared Analysis API Documentation](skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown and JSON-style structured text with report links and optional saved output files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can analyze local files or URLs and can query cloud-hosted historical reports.]

## Skill Version(s):

1.0.15 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
