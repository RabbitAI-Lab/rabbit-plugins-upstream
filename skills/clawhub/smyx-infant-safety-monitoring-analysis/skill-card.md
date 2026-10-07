## Description:

Analyzes infant activity videos for possible safety hazards and returns risk reports, warnings, and care suggestions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Caregivers can submit infant activity videos for advisory hazard analysis and retrieve cloud-stored safety reports. Results do not replace direct supervision.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sensitive infant media and report history are sent to the LifeEmergence cloud service.

Mitigation: Use only with appropriate caregiver consent and avoid submitting media or history you are not comfortable sharing with the service.

Risk: Account linkage may happen silently, with a token stored locally.

Mitigation: Review local token storage and account access before use, especially on shared devices.

Risk: An advisory analysis can miss hazards or arrive too late to prevent harm.

Mitigation: Do not use this skill as a real-time safety monitor or substitute for direct infant supervision.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/smyx-sunjinhui/skills/smyx-infant-safety-monitoring-analysis)
- [Infant safety analysis API documentation](references/api_doc.md)
- [Skill demonstration](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Text, JSON, Markdown]

**Output Format:** [JSON or text reports; Markdown tables for report history]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports may include hazard warnings, care suggestions, and links to cloud-stored reports.]

## Skill Version(s):

1.0.16 (source: server-resolved ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
