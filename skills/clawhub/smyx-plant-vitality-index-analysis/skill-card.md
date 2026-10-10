## Description:

Analyzes plant images or videos through a remote service to report a 0–100 vitality score, recent trends, and links to analysis reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Gardeners and plant-monitoring teams use the skill to assess plant vitality from images or videos, compare trends, and access prior reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Plant media or URLs are sent to an external analysis service.

Mitigation: Use only media you are authorized to share, and review the destination service before submitting sensitive content.

Risk: The skill can silently create or reuse an identity and store tokens in a local workspace database.

Mitigation: Install only if you trust the publisher and accept persistent account linkage; protect workspace data and restrict access to stored credentials.

Risk: Cloud report history may be accessible with limited user control.

Mitigation: Review who can access the linked account and its reports before enabling history queries.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/smyx-sunjinhui/skills/smyx-plant-vitality-index-analysis)
- [API documentation](references/api_doc.md)
- [Skill demonstration](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON]

**Output Format:** [Structured analysis report or Markdown report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Vitality score on a 0–100 scale; trends and report history when available.]

## Skill Version(s):

1.0.13 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
