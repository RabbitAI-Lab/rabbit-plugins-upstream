## Description:

Using fixed thermal-imaging camera footage, this skill analyzes multiple people in a shared scene, compares each person's skin-surface temperature with the group average, and reports relative temperature anomalies with a recommendation to recheck using a calibrated thermometer.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers can use this skill to analyze thermal camera images or videos from family, meeting-room, kindergarten, or care-facility gathering spaces for relative body-temperature anomalies. It supports structured screening reports, historical report lookup, and directional alerts, but it is not a medical diagnosis tool.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Thermal health media and report history may be processed through cloud services and include sensitive personal or health-related information.

Mitigation: Use only with explicit participant consent, appropriate privacy review, encrypted storage, and environments approved for sensitive media.

Risk: The security review reports silent identity-state persistence and under-scoped, partly plaintext network paths.

Mitigation: Do not deploy as-is in sensitive environments; require HTTPS-only endpoints, scoped identity handling, and secure credential storage before production use.

Risk: Relative temperature anomalies can be affected by masks, hats, recent exercise, hot drinks, sunlight, air conditioning, heaters, or poor thermal-camera setup.

Mitigation: Treat outputs as screening signals only and confirm any anomaly with a calibrated medical thermometer or qualified clinical process.

## Reference(s):

- [Thermal Fever Screening API Documentation](references/api_doc.md)
- [Skill Demo](https://lifeemergence.com/sample.html)
- [ClawHub Skill Page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-thermal-fever-screening-analysis)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown and JSON-style structured analysis reports with command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include detected-person counts, group temperature statistics, per-person deltas, anomaly labels, recommended actions, and report links.]

## Skill Version(s):

1.0.7 (source: server-resolved release metadata; artifact frontmatter reports 1.0.13)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
