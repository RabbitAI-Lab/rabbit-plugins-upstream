## Description:

Analyzes fixed-camera video of an elderly person at rest to estimate respiratory rate and flag tachypnea or dyspnea risk from visual chest or abdominal motion.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External caregivers, families, and elder-care platform operators use this skill to analyze elderly resting video, calculate respiratory rate, and produce visual-only alert reports for possible tachypnea or dyspnea. It is an assistive monitoring workflow and should not be treated as a medical diagnosis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill processes sensitive bedroom video and health-adjacent respiratory reports through configured backend APIs.

Mitigation: Use only with clear consent from the monitored person or caregiver, and treat videos, reports, and generated links as sensitive data.

Risk: The bundled configuration includes development HTTP endpoints in addition to production service URLs.

Mitigation: Verify backend configuration before deployment and use production HTTPS endpoints rather than development 192.168.1.234 HTTP endpoints.

Risk: The workflow may store or reuse local user and token records for silent identity/account handling.

Mitigation: Protect the local data directory, restrict file access, and rotate or clear stored tokens when changing users or deployment environments.

Risk: Respiratory-rate alerts are health-adjacent and may be mistaken for clinical diagnosis.

Mitigation: Present outputs as visual monitoring signals only, require human verification for urgent alerts, and escalate to qualified medical care when appropriate.

## Reference(s):

- [API interface documentation](references/api_doc.md)
- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-elderly-tachypnea-detection-analysis)
- [Skill demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, files]

**Output Format:** [Markdown or JSON respiratory analysis report with optional saved output file.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include respiratory-rate values, risk levels, alert text, report links, and history tables returned by the configured backend.]

## Skill Version(s):

1.0.9 (source: server release metadata; artifact frontmatter says 1.0.11)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
