## Description:

Analyzes plant images or video to identify growth stages and return structured reports for agricultural decision support.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Agricultural producers and agronomy teams can submit plant images or video to review identified growth stages and structured analysis that supports field decisions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Reports may be mixed across users in shared account contexts.

Mitigation: Have the publisher fix and verify per-user report isolation before using shared workspaces or sensitive media.

Risk: Credential handling needs review.

Mitigation: Have the publisher correct and document credential handling before deployment.

Risk: The export-only option can still upload media to LifeEmergence’s cloud service, and the bundled code cannot verify deletion claims.

Mitigation: Avoid sensitive media until export-only behavior and media retention are verified with the publisher.

## Reference(s):

- [API documentation](skills/smyx_analysis/references/api_doc.md)
- [Skill demonstration](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Analysis, JSON, Markdown, Report links]

**Output Format:** [Structured JSON analysis with report text and links; report listings can be presented as Markdown tables.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Analysis detail can be basic, standard, or JSON; results may include recommendations and report export links.]

## Skill Version(s):

1.0.17 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
