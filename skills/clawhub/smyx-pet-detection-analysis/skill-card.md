## Description:

Detects cats, dogs, and birds in images or video streams for home pet monitoring.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to submit home pet monitoring images, video files, or media URLs for cat, dog, and bird detection, then review structured detection results and report links.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Media files, submitted URLs, and report lookups are processed by the publisher's cloud service.

Mitigation: Use only media and URLs approved for third-party cloud processing, and review the publisher's handling terms before deployment.

Risk: The skill automatically creates or reuses an internal identity and stores authentication tokens in workspace data.

Mitigation: Run the skill in an isolated workspace, protect workspace data, and remove or rotate stored credentials when access should end.

Risk: Bundled development configuration includes plain HTTP endpoints while the privacy statement describes HTTPS/TLS transport.

Mitigation: Review configuration before use and require HTTPS endpoints for production or sensitive media.

## Reference(s):

- [API Interface Documentation](references/api_doc.md)
- [Shared API Documentation](skills/smyx_analysis/references/api_doc.md)
- [Skill Demo](https://lifeemergence.com/sample.html)
- [ClawHub Skill Page](https://clawhub.ai/18072937735/skills/smyx-pet-detection-analysis)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Files]

**Output Format:** [Markdown or JSON structured pet detection report with report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can save report text to a user-specified output file.]

## Skill Version(s):

1.0.10 (source: server release metadata; artifact frontmatter declares 1.0.12)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
