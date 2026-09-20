## Description:

Classifies likely causes of infant crying from audio or audio-video inputs and returns confidence, secondary causes, acoustic feature summaries, soothing guidance, and report links.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to analyze infant cry recordings or media URLs, classify likely cry causes, and retrieve structured reports or cloud history for caregiving workflows. Results are directional support and should not be treated as medical diagnosis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Infant audio, video, or media URLs may be sent to a configured remote service.

Mitigation: Use only with guardian consent and confirm service retention, deletion, and access controls before uploading child or household recordings.

Risk: The skill creates or reuses a local identity and may store authentication tokens locally.

Mitigation: Review account isolation and local token storage controls before installation; restrict filesystem access and rotate credentials if exposed.

Risk: Cloud history reports can be retrieved through the service.

Mitigation: Confirm report authorization boundaries and avoid using the skill where history visibility across users or devices is not acceptable.

Risk: Cry-cause classification can be mistaken for clinical advice.

Mitigation: Treat results as directional caregiving support only and seek professional care for persistent, abnormal, or medically concerning crying.

## Reference(s):

- [Infant cry cause classification API documentation](references/api_doc.md)
- [Shared analysis API error documentation](skills/smyx_analysis/references/api_doc.md)
- [Skill demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, guidance]

**Output Format:** [Markdown summaries or JSON from the analysis CLI/API, optionally written to a file.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include confidence scores, secondary causes, acoustic feature summaries, soothing hints, report links, and cloud history tables.]

## Skill Version(s):

1.0.11 (source: server release metadata; artifact frontmatter says 1.0.14)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
