## Description:

Identifies common pet behaviors, including scratching, chewing, destructive activity, and separation anxiety, from pet videos and provides a behavior analysis report.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Pet owners and their agents use local videos or video URLs to review pet behavior, receive a structured analysis report, and access past cloud reports. Results are informational; consult a professional pet trainer for behavior correction advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Pet footage or video URLs are sent to third-party cloud services for analysis.

Mitigation: Review cloud processing and retention terms before submitting sensitive household footage.

Risk: The skill automatically creates or reuses an internal user identity and stores user and token records locally for cloud report history.

Mitigation: Review account linking and local credential storage before use, and limit access to the stored records.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/18072937735/skills/smyx-pet-behavior-detection-analysis)
- [API interface documentation](artifact/references/api_doc.md)
- [Skill demonstration](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON]

**Output Format:** [Structured behavior report or JSON analysis; Markdown table for historical reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include behavior summaries, recommendations, and report links.]

## Skill Version(s):

1.0.15 (source: server-resolved ClawHub release; bundled frontmatter says 1.0.22)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
