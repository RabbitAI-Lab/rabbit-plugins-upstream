## Description:

Analyzes fixed-camera bedroom video of an elderly person at rest to estimate respiratory rate and flag possible tachypnea or dyspnea based on configured thresholds.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Caregivers, family members, and elder-care operators use this skill to analyze resting chest or abdominal video from home, nursing home, or rehabilitation settings and review structured respiratory-rate risk reports. It is an assistive monitoring tool and should not be treated as a medical diagnosis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill handles sensitive bedroom video and health-report data through remote processing.

Mitigation: Require explicit consent before uploads or report-history queries, disclose remote processing and retention, and protect or delete local copies after use.

Risk: The security evidence identifies an unsafe default HTTP development configuration.

Mitigation: Use production HTTPS endpoints for real data and block development HTTP endpoints from production workflows.

Risk: The security evidence notes broad cloud, identity, and token workflows.

Mitigation: Store tokens securely, avoid exposing internal identity values, and define a deletion process for local token and report data.

## Reference(s):

- [API interface documentation](references/api_doc.md)
- [Skill demo](https://lifeemergence.com/sample.html)
- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-elderly-tachypnea-detection-analysis)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Guidance]

**Output Format:** [Markdown or JSON structured respiratory-rate report, with report links for history results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include respiratory rate, respiratory pattern, signal quality, risk level, alert text, follow-up guidance, and report URLs.]

## Skill Version(s):

1.0.11 (source: server release metadata; artifact frontmatter states 1.0.13)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
