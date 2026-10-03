## Description:

Analyzes images and videos for strangers near minors and returns safety alerts and structured reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Guardians and staff at homes, schools, and childcare centers use the skill to review images or videos for possible stranger proximity to minors and consult alerts and historical reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Images or videos of minors may be uploaded to an external service for analysis and retained in cloud history.

Mitigation: Use only with authority and consent for monitoring; assess the service's handling and retention of sensitive media before uploading.

Risk: The skill may silently create and reuse a persistent identity and store tokens locally.

Mitigation: Install only if you trust the publisher and accept identity persistence; restrict access to the host and its stored credentials.

## Reference(s):

- [Analysis API documentation](references/api_doc.md)
- [Skill demonstration](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Analysis, Text, Markdown]

**Output Format:** [Structured analysis report or Markdown table of historical reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include risk alerts, recommendations, and report links; results can be saved to a file.]

## Skill Version(s):

1.0.15 (source: server-resolved ClawHub release; bundled frontmatter says 1.0.20)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
