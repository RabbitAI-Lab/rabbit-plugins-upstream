## Description:

Detects delivery packages in a target surveillance area for inventory checks and unattended alerts at community stations, residential entrances, and office lobbies.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Facility staff and operators use the skill to inspect surveillance images or videos, count and locate parcels, and review overdue-package alerts or hosted analysis reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Reports may be mixed between users while sender isolation remains unresolved.

Mitigation: Avoid shared-user deployment until sender isolation is fixed.

Risk: Footage may be processed despite the no-analysis option, and remote retention and access behavior are unverified.

Mitigation: Avoid sensitive footage until the no-analysis option is fixed, and confirm the service’s retention and access policies before use.

Risk: The configured API URL may not control where uploads are sent.

Mitigation: Do not rely on --api-url to redirect uploads.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/18072937735/skills/smyx-package-detection-analysis)
- [API documentation](references/api_doc.md)
- [Skill demonstration](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Analysis, JSON, Markdown, Guidance]

**Output Format:** [Structured analysis results and reports; historical report lists can be presented as Markdown tables, with report links when available.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Accepts image or video inputs; supports local files and URLs.]

## Skill Version(s):

1.0.18 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
