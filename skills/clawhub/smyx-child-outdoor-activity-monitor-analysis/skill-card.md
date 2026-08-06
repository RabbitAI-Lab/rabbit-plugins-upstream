## Description:

Monitors fixed door or balcony camera footage to detect child exit and return events, compute daily outdoor-activity duration, and produce alerts when activity is below the configured recommendation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to analyze authorized child door or balcony camera videos, generate structured outdoor-activity duration reports, and query prior reports from the configured cloud service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Child and home camera footage is processed by the configured cloud service.

Mitigation: Use only with guardian consent, submit only authorized footage, and protect any generated report links or exported reports.

Risk: The skill creates or reuses a local identity and can store access tokens in the workspace data directory.

Mitigation: Restrict access to the workspace data directory, avoid sharing it, and rotate or clear stored credentials when the workspace changes hands.

Risk: Network video URL inputs can cause the cloud service to fetch externally hosted footage.

Mitigation: Provide only trusted, authorized video URLs and avoid arbitrary third-party links.

## Reference(s):

- [Child Outdoor Activity Duration Monitoring API Documentation](artifact/references/api_doc.md)
- [Skill demo](https://lifeemergence.com/sample.html)
- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-child-outdoor-activity-monitor-analysis)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, guidance]

**Output Format:** [Markdown and JSON-style structured analysis reports with optional report links and saved text output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May query historical reports and may write an output file when requested.]

## Skill Version(s):

1.0.7 (source: server release metadata; artifact frontmatter states 1.0.9)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
