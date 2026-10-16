## Description:

Analyzes UAV farm imagery through an external service and returns structured analysis results and report links for assessing crop health.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Farm operators, agricultural cooperatives, and drone-imagery analysts can submit field imagery or media URLs to obtain crop-health analysis reports and consult previous reports. Results should be checked against field observations before making management decisions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Agricultural imagery or media URLs may be sent to an external service.

Mitigation: Confirm the service and publisher are trusted and obtain authorization before submitting field data or URLs.

Risk: The skill may create or reuse a local identity, log in remotely, and store session tokens in a workspace SQLite database.

Mitigation: Review the identity and data-retention behavior before installation, and restrict access to the workspace and stored tokens.

Risk: The implementation appears less specific to farm health-index imagery than advertised, so results may not substantiate claimed vegetation-index maps.

Mitigation: Validate outputs against independent imagery analysis and field observations before acting on crop-health findings.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/18072937735/skills/smyx-uav-farm-health-index-map-analysis)
- [Skill API reference](references/api_doc.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Report links]

**Output Format:** [Structured analysis text or JSON, with links to reports; optional saved text file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results depend on an external analysis service; historical reports can be listed.]

## Skill Version(s):

1.0.14 (source: server-resolved ClawHub release; packaged frontmatter says 1.0.18)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
