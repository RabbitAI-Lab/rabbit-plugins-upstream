## Description:

Grades tomato and strawberry ripeness from images or video and provides harvest guidance and report links.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Growers and horticultural teams use fruit images or video to assess tomato and strawberry ripeness, plan harvest timing, and review prior reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Fruit images or URLs are sent to a cloud service for analysis.

Mitigation: Review the service's data practices and send only images and URLs you are authorized to share.

Risk: Report history is associated with an internally managed identity, and local token storage or the hidden identity parameter may affect which reports are accessed or created.

Mitigation: Limit CLI access to trusted callers and review identity handling before using historical reports.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/smyx-sunjinhui/skills/smyx-fruit-ripeness-grading-analysis)
- [Skill API documentation](artifact/references/api_doc.md)
- [Skill demonstration](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Analysis, Guidance, Text]

**Output Format:** [Markdown or JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Ripeness grades, harvest guidance, report links, and optional saved results; historical reports may be shown as a Markdown table.]

## Skill Version(s):

1.0.11 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
