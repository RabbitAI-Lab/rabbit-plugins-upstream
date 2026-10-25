## Description:

Analyzes child drop-off videos for crying, clinging, and resistance behaviors and returns an indicative separation-anxiety severity assessment.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Parents and teachers use this skill to review home or kindergarten drop-off footage, identify possible separation distress, and obtain a structured report with suggestions for support. It also retrieves prior reports from the cloud.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Children's and families' identifiable footage and report queries are sent to a cloud service.

Mitigation: Obtain appropriate guardian and school consent before upload; confirm retention, authorization, and report-access controls before using real minors' footage.

Risk: The skill may create an identity automatically and store API tokens locally, exposing reports if workspace data is shared.

Mitigation: Do not pass custom identity values or share the workspace data directory; restrict access to locally stored tokens and cloud reports.

Risk: Playful behavior or incidental tears may be misclassified as separation distress.

Mitigation: Review findings in context and use them only as an aid, not as a substitute for a child mental-health professional's assessment.

## Reference(s):

- [Skill API documentation](artifact/references/api_doc.md)
- [ClawHub skill listing](https://clawhub.ai/18072937735/skills/smyx-child-separation-anxiety-detection-analysis)

## Skill Output:

**Output Type(s):** [Analysis, Guidance, Markdown, JSON]

**Output Format:** [Structured JSON analysis or Markdown report with history links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include severity level, observations, recommendations, and links to cloud-hosted reports.]

## Skill Version(s):

1.0.13 (source: server-resolved release metadata; bundled frontmatter states 1.0.17)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
