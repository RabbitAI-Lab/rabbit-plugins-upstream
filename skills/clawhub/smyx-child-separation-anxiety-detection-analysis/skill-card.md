## Description:

Analyzes home-entrance or kindergarten drop-off videos or images to identify crying expressions, clinging or resistance behaviors, and separation-anxiety level, then returns behavior metrics, reminders, and caregiver-facing suggestions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External users such as parents, teachers, and child-care operators use this skill to analyze drop-off media for visual behavior indicators and receive structured reports, reminders, and non-diagnostic calming suggestions. Developers and system integrators may connect it to smart-camera or kindergarten-management workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill handles child and family video or report data through a remote service.

Mitigation: Use only with explicit consent, submit only necessary media, and confirm retention, deletion, and access-control terms before deployment.

Risk: Security evidence reports active plaintext network endpoints.

Mitigation: Require HTTPS-only production endpoints and block insecure endpoint configuration before operational use.

Risk: Security evidence reports local service-token storage.

Mitigation: Protect stored tokens with appropriate local permissions or secret-management controls and rotate tokens if exposure is suspected.

Risk: The skill evaluates behavior related to child separation anxiety and may be mistaken for a clinical assessment.

Mitigation: Present outputs as visual behavior observations and friendly reminders only, and route serious or persistent concerns to qualified child-health professionals.

## Reference(s):

- [API Interface Documentation](artifact/references/api_doc.md)
- [SMYX Analysis API Documentation](artifact/skills/smyx_analysis/references/api_doc.md)
- [Skill Demo](https://lifeemergence.com/sample.html)
- [ClawHub Skill Page](https://clawhub.ai/18072937735/skills/smyx-child-separation-anxiety-detection-analysis)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, configuration, guidance]

**Output Format:** [Markdown tables and structured JSON or text reports with report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May save report output to a file when the output path option is used.]

## Skill Version(s):

1.0.10 (source: server-resolved release metadata; artifact frontmatter says 1.0.12)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
