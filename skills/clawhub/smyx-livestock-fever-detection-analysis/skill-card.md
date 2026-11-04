## Description:

Detects abnormal body temperature rise or drop in livestock and poultry from thermal or visible-light imagery, and outputs fever/hypothermia early warnings based on visual thermal features.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Livestock producers and animal-health staff use thermal or visible-light images and short videos to screen herds for possible fever or hypothermia, review flagged animals, and access analysis reports. Results are for screening and do not provide disease diagnoses or treatment advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Account handling may mix users’ reports.

Mitigation: Wait for sender isolation to be fixed and verify that credentials and report access are restricted to the intended user before use.

Risk: Selected media may be sent to LifeEmergence cloud services, and the security summary notes uploads can occur in the advertised non-analysis mode.

Mitigation: Disclose the cloud transfer and obtain appropriate authorization before selecting media; wait for the documented --export-env-only issue to be fixed and review safe logging and credential destinations.

Risk: Cloud retention and server-side access controls are unverified.

Mitigation: Confirm retention and access controls with the service provider before sending sensitive images or videos.

## Reference(s):

- [API reference](references/api_doc.md)
- [Skill demonstration](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Analysis, JSON, Markdown]

**Output Format:** [Structured screening reports with flagged-animal details, estimated temperature ranges, alert levels, and report links; history lists are presented as Markdown tables.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Screening reference only; not a disease diagnosis or treatment recommendation.]

## Skill Version(s):

1.0.16 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
