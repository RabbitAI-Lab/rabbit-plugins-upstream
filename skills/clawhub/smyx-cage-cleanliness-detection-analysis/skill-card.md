## Description:

This skill analyzes pet cage images or videos to estimate feces and urine coverage, score cleanliness, trigger threshold-based cleaning alerts, and return structured reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

External operators of pet boarding centers, pet shops, animal hospitals, and breeding facilities use this skill to analyze cage floor media, identify waste coverage, receive cleaning alerts, and retrieve historical cleanliness reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Cage images, videos, and report queries are sent to a cloud service for analysis.

Mitigation: Use only media approved for cloud processing and confirm storage location, retention, deletion, and access controls before deployment.

Risk: The skill can silently create or reuse an identity and store account tokens locally.

Mitigation: Review local token storage, restrict access to the local database, and define a token deletion or rotation process before use.

Risk: Historical report lookup may expose prior reports tied to the automatically managed identity.

Mitigation: Require explicit approval for history lookup workflows and verify that returned reports are authorized for the current user or organization.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-cage-cleanliness-detection-analysis)
- [API interface documentation](references/api_doc.md)
- [Skill demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Files, Guidance]

**Output Format:** [Structured report text, Markdown tables for history results, JSON detail output, and optional saved output files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include cleanliness scores, waste coverage estimates, threshold alerts, recommendations, and report links.]

## Skill Version(s):

1.0.7 (source: server release evidence; artifact frontmatter reports 1.0.9)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
