## Description:

Analyzes nighttime eldercare footage for bed exits, prolonged wandering, and extended immobility, and provides reports for caregivers.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Caregivers and eldercare operators use this skill to review nighttime video for possible bed exits, wandering, or prolonged immobility and to retrieve historical monitoring reports. Alerts and analyses support, but do not replace, in-person checks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sensitive eldercare images, videos, and historical reports are processed by configured cloud services.

Mitigation: Confirm consent from monitored people and avoid uploading sensitive footage unless necessary.

Risk: Untrusted video URLs may expose sensitive content or lead to unintended remote downloads.

Mitigation: Use only trusted video URLs and review them before analysis.

Risk: Local workspace data may contain identity and token data.

Mitigation: Restrict access to the local workspace data directory and handle it as sensitive data.

Risk: Automated behavior detection may miss or misclassify urgent events.

Mitigation: Have caregivers verify alerts in person; do not treat results as a substitute for human checks.

## Reference(s):

- [Eldercare analysis API documentation](references/api_doc.md)
- [ClawHub skill listing](https://clawhub.ai/18072937735/skills/smyx-elderly-bed-exit-wandering-monitoring-analysis)
- [Skill introduction](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Analysis, Guidance, Reports]

**Output Format:** [Structured text or Markdown; JSON when requested]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include risk alerts, recommendations, historical-report tables, and report links.]

## Skill Version(s):

1.0.20 (source: server-resolved ClawHub release; artifact frontmatter lists 1.0.13)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
