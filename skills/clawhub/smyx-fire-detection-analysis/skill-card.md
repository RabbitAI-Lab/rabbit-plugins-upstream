## Description:

Detects flames and smoke in video or image inputs for fire early warning in locations such as industrial parks, forests, and warehouses.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to analyze surveillance images, videos, or URLs for flame and smoke indicators, then receive structured findings, risk level information, recommendations, and report links.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Surveillance images, videos, URLs, identity values, and report-history queries may be sent to configured cloud or private API endpoints.

Mitigation: Deploy only where those data flows are approved, and require publisher clarification of endpoint ownership, retention/deletion behavior, and external data handling before broad use.

Risk: The skill silently creates or reuses an internal user identity and stores authentication data.

Mitigation: Run in an isolated environment with reviewed credential and token storage, and restrict access to generated identity and report data.

Risk: Fire detection output is a warning aid and may be incorrect or incomplete.

Mitigation: Require operator review and established emergency response procedures for any fire alert or safety decision.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/18072937735/skills/smyx-fire-detection-analysis)
- [Skill Demo](https://lifeemergence.com/sample.html)
- [API Documentation](references/api_doc.md)
- [Analysis API Documentation](skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Shell commands, Guidance]

**Output Format:** [Markdown and JSON analysis results with optional report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Consumes local image/video paths or public URLs; historical report queries return Markdown tables from API results.]

## Skill Version(s):

1.0.18 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
