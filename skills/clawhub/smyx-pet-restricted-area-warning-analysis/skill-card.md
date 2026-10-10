## Description:

Analyzes home pet-monitoring videos for restricted-area entry, table climbing, and trash rummaging, returning alerts and structured reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Pet owners and home-monitoring users can analyze video files or URLs for pet activity in restricted areas and review alerts and historical reports. Review flagged events against the original footage before taking action.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Home-monitoring videos or URLs are sent to the publisher's cloud service.

Mitigation: Obtain consent before submitting media; review the publisher's data retention practices and avoid uploading sensitive footage when unsuitable.

Risk: The skill silently creates or reuses an identity, stores tokens locally, and can access cloud report history.

Mitigation: Review identity and history access before use, restrict access to local credentials, and check how to revoke access and remove stored reports.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/smyx-sunjinhui/skills/smyx-pet-restricted-area-warning-analysis)
- [Skill demonstration](https://lifeemergence.com/sample.html)
- [Bundled API reference](references/api_doc.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON]

**Output Format:** [Structured analysis results, readable reports, or Markdown history tables]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include alerts, report links, and an optional saved result file.]

## Skill Version(s):

1.0.16 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
