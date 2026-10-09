## Description:

Analyzes plant images or videos for signs of wilting and provides early warnings, recommendations, and report links.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Growers and agricultural advisers use plant images or videos to check for early wilting, review monitoring reports, and inform irrigation or disease-control decisions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill silently creates or reuses a cloud-service identity and stores service tokens locally.

Mitigation: Review account and token handling before use, restrict access to stored tokens, and clarify opt-out and deletion options with the publisher.

Risk: Plant media or media URLs are sent to an external cloud service.

Mitigation: Avoid sensitive media until the publisher documents retention and deletion practices; obtain appropriate consent before uploading.

Risk: Wilting assessments may be mistaken for a definitive plant diagnosis.

Mitigation: Treat results as early warnings and confirm decisions against field conditions and expert advice.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/smyx-sunjinhui/skills/smyx-plant-wilting-monitoring-analysis)
- [API documentation](skills/smyx_analysis/references/api_doc.md)
- [Skill demonstration](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON]

**Output Format:** [Structured monitoring report or JSON, with recommendations and report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can return links to historical cloud reports.]

## Skill Version(s):

1.0.15 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
