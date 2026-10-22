## Description:

Analyzes plant images and videos through a cloud service to identify growth stages and return structured reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Growers and agricultural advisers use plant images or videos to assess growth stages and review analysis reports for crop-management decisions. Users can also request earlier cloud reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Images, videos, or media URLs are sent to lifeemergence.com services for analysis.

Mitigation: Share only media approved for external processing and review the service's data-handling terms before use.

Risk: The skill silently creates or reuses an internal identity and stores authentication tokens in a local workspace database.

Mitigation: Install only if this account linkage and local token storage are acceptable; restrict workspace access and remove stored credentials when no longer needed.

Risk: Historical report requests retrieve data from the linked cloud account.

Mitigation: Confirm the linked account is appropriate before requesting or sharing previous reports.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/smyx-sunjinhui/skills/smyx-plant-growth-stage-recognition-analysis)
- [Skill demonstration](https://lifeemergence.com/sample.html)
- [API documentation](skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Structured analysis report or report list, with optional saved text file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include growth-stage findings, recommendations, and report links.]

## Skill Version(s):

1.0.16 (source: ClawHub release; artifact frontmatter lists 1.0.19)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
