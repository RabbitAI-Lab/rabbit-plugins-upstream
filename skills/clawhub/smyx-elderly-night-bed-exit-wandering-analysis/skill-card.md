## Description:

Using fixed cameras with infrared night vision in nursing-home or home bedrooms, the skill monitors elderly bed-exit status and nighttime activity trajectory, then outputs behavioral statistics and abnormal alerts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External care teams, nursing-home operators, home-care providers, and developers use this skill to analyze nighttime bedroom or hallway video for bed-exit duration, wandering behavior, threshold-based alerts, and historical report lookup. The output is for care-monitoring reference and is not a medical diagnosis or a substitute for human verification.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Bedroom and hallway monitoring videos can contain highly sensitive personal information and are sent to Life Emergence cloud services for analysis.

Mitigation: Use only with informed consent from the monitored person or authorized family or care representatives, and confirm the cloud service's retention, access-control, and data-handling terms before submitting media or URLs.

Risk: The skill may silently reuse or create an internal identity and query cloud report history tied to that identity.

Mitigation: Run it in a dedicated workspace, restrict access to local configuration and token files, and verify that account provisioning and historical report access match the deployment's privacy expectations.

Risk: Alert outputs are care-monitoring references and may be incomplete or incorrect for urgent events such as suspected falls or wandering away.

Mitigation: Require human review of alerts and keep emergency response procedures outside the automated skill output.

## Reference(s):

- [Elderly Night Bed-Exit and Wandering API Documentation](references/api_doc.md)
- [SMYX Analysis API Error Codes](skills/smyx_analysis/references/api_doc.md)
- [Skill Demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, guidance]

**Output Format:** [Markdown and JSON-style structured analysis reports with alert text, report links, and optional Markdown tables for historical reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include bed-exit events, total exit duration, wandering status and duration, alert level, alert message, recommendations, and cloud report links.]

## Skill Version(s):

1.0.9 (source: server release metadata; artifact frontmatter lists 1.0.8)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
