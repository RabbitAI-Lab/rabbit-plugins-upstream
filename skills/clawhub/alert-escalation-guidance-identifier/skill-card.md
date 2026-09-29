## Description:

Provides severity-based service assignment guidance for incoming alerts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Incident responders and service operators use this skill to draft severity-to-response-lead and service-queue assignment guidance for alerts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The bundled routing may omit named service owners, unknown-severity triage, and operating-hours rules promised by the documentation, yielding misleading escalation guidance.

Mitigation: Review the generated assignment against the service's owner, triage queue, and on-call policy before using it for incident operations; rely on the bundled operation only for levels, lead_levels, and default_queue mappings.

## Reference(s):

- [Service Assignment Guide on ClawHub](https://clawhub.ai/wxt-ai/skills/alert-escalation-guidance-identifier)

## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [String]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Returns a severity assignment rule; does not send alerts or persist an assignment.]

## Skill Version(s):

1.1.0 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
