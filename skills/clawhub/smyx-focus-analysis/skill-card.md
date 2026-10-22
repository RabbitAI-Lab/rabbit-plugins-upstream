## Description:

Analyzes video of gaze and head position to report attention and distraction in classroom, workplace, and driving scenarios.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Teachers, workplace managers, and safety officers can request attention analysis of a video or review past reports. The skill provides attention scores, trends, suggestions, and report links; its assessments should not replace human judgment.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Videos or video URLs containing faces and attention data are sent to the Life Emergence cloud service.

Mitigation: Use only with lawful authority and informed consent; confirm the service's retention and deletion terms before uploading sensitive media.

Risk: The skill creates or reuses a persistent workspace identity and stores service tokens locally without clear user controls.

Mitigation: Review identity and token storage before use, restrict local access, and ask the publisher about account and token management before production deployment.

Risk: Attention scores may be mistaken for definitive assessments in classrooms, workplaces, or driving.

Mitigation: Treat scores as indicative only and require human review before making decisions about individuals or safety.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/18072937735/skills/smyx-focus-analysis)
- [Skill demonstration](https://lifeemergence.com/sample.html)
- [Shared analysis API notes](skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON]

**Output Format:** [Structured analysis report or Markdown history table, with report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results can be saved to a local file; historical reports are fetched from the cloud service.]

## Skill Version(s):

1.0.17 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
