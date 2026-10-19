## Description:

Analyzes images and videos for smoking behavior in public spaces and returns detection reports and historical results.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Facilities and safety teams use the skill to review images and videos for possible smoking incidents, retrieve cloud-hosted detection reports, and inform smoking-control decisions. Results should be reviewed before taking action.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Images, videos, or supplied media URLs are sent to an external service and may contain sensitive surveillance footage.

Mitigation: Use only approved footage and confirm the provider's data handling and access controls before analysis.

Risk: The skill creates or reuses an account identity and retains tokens and report associations in the workspace data directory.

Mitigation: Review account access and protect the workspace data directory from unauthorized access.

Risk: Historical report retrieval can expose previously analyzed records.

Mitigation: Limit report access to authorized users and review retrieved results before sharing them.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/smyx-sunjinhui/skills/smyx-smoking-detection-analysis)
- [Skill demonstration](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON]

**Output Format:** [Structured detection reports in text or JSON; historical results as a Markdown table]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include findings, recommendations, and links to cloud-hosted reports; results can be saved to a file.]

## Skill Version(s):

1.0.16 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
