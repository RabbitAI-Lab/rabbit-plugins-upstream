## Description:

Detects cats, dogs, and birds in images or video for home pet monitoring and provides analysis reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Home pet owners and monitoring operators use this skill to check images or video for cats, dogs, and birds, review detection results, and retrieve past reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Images, video, or media URLs are sent to an external analysis service.

Mitigation: Use only media you are authorized to share and review the service's data handling before uploading.

Risk: The skill silently creates or reuses an identity and stores service tokens in a local SQLite database.

Mitigation: Limit access to the workspace and its stored credentials; install only if you accept account-scoped processing.

Risk: Broad history requests can retrieve cloud reports tied to that identity.

Mitigation: Confirm the intended account and request before retrieving or sharing report history.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/18072937735/skills/smyx-pet-detection-analysis)
- [API documentation](references/api_doc.md)
- [Skill demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON]

**Output Format:** [Text reports with structured JSON, Markdown history tables, and report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results and history are retrieved from a cloud service.]

## Skill Version(s):

1.0.15 (source: ClawHub release metadata; bundled frontmatter says 1.0.18)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
