## Description:

Detects hazardous child behaviors in images or videos, including climbing, playing with fire, touching power sources, and dangerous actions near windows, and returns alerts with structured analysis reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and child-safety operators use this skill to analyze local or URL-based child monitoring media for hazardous behaviors and retrieve structured reports or historical report lists.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Real child footage may be uploaded to a cloud analysis service and report history may be retrieved.

Mitigation: Require explicit consent and privacy terms for uploads and report history, and limit history retrieval to scoped user-controlled access.

Risk: The skill silently creates and reuses service identities and stores tokens locally.

Mitigation: Review identity behavior before installation and require secure credential storage or a clear credential-clearing flow.

Risk: The release ships with plaintext development API endpoints.

Mitigation: Require HTTPS production endpoints before use with real child footage.

## Reference(s):

- [API documentation](references/api_doc.md)
- [Skill demo](https://lifeemergence.com/sample.html)
- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-child-dangerous-behavior-recognition-analysis)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Files]

**Output Format:** [Markdown or JSON structured report, with optional saved output file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include detected behavior categories, counts, alert status, threshold details, recommendations, and report links.]

## Skill Version(s):

1.0.14 (source: server release metadata; artifact frontmatter and release changelog mention 1.0.16)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
