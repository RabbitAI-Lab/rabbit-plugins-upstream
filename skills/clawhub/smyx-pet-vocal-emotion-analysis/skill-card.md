## Description:

Analyzes cat and dog vocalizations from audio or video files or URLs through a cloud service and returns structured emotion, intent, and report-link output.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to submit pet audio or video for emotion and behavior-intent analysis, including history lookup for prior cloud reports. Results are suitable for pet-owner interaction and review, not veterinary diagnosis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Pet media, media URLs, and report history are sent to the Life Emergence cloud service for analysis and retrieval.

Mitigation: Use only media approved for cloud processing, avoid sensitive recordings, and review the service endpoint and returned reports before relying on results.

Risk: The skill may create or reuse local identity and token records for report history.

Mitigation: Review and manage workspace data files such as smyx-api-key.txt and smyx-common-claw.db when privacy boundaries, rotation, or deletion are required.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-pet-vocal-emotion-analysis)
- [Pet Vocal Emotion Analysis API Documentation](artifact/references/api_doc.md)
- [Skill Demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Files]

**Output Format:** [Structured text with JSON report content, optional Markdown-style history listings, and optional saved output files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include report export links returned by the cloud service.]

## Skill Version(s):

1.0.11 (source: server release metadata; artifact frontmatter says 1.0.14)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
