## Description:

Analyzes dining images or videos to assess eating speed, eating habits, dietary structure, and unhealthy eating tendencies, then returns structured reports and nutrition-improvement recommendations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agent operators use this skill to submit meal-related images, videos, or public URLs for dietary behavior analysis, structured health-reference reports, history lookup, and nutrition-improvement guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Eating-behavior media and identifiers are sent to the Life Emergence cloud service, and report history is cloud-linked.

Mitigation: Use only in trusted workspaces where users understand this data flow, and avoid sensitive videos unless identity isolation is in place.

Risk: Reusable tokens and default identities may be stored locally, which can mix private report history across users in shared workspaces.

Mitigation: Run the skill in a single-user trusted workspace or isolate identities and token storage before shared deployment.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-diet-analysis)
- [Skill demo](https://lifeemergence.com/sample.html)
- [API interface documentation](references/api_doc.md)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, files, guidance]

**Output Format:** [Markdown text with structured JSON excerpts, report links, and optional saved output files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include cloud report history and report export links; analysis results are health references and not medical or nutritionist diagnosis.]

## Skill Version(s):

1.0.14 (source: server release metadata; artifact frontmatter lists 1.0.17)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
