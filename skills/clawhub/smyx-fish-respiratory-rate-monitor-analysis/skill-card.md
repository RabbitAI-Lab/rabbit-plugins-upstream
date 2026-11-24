## Description:

Analyzes aquarium video of visible fish gill-cover motion to estimate breathing rate and flag readings that may warrant checking water quality, temperature, or fish health.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Aquarists, fish keepers, aquarium operators, and ornamental fish farms can provide close-up aquarium video to estimate gill movement and breathing rate, review potential abnormalities, and retrieve monitoring reports. Results are visual estimates and prompts for further checks, not veterinary diagnoses.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review flags account and credential handling, broad data and notification behavior, and possible analysis despite an export-only request; its scan was partial, so the available evidence is incomplete.

Mitigation: Before installation, verify the publisher, credential and file handling, and remote-service behavior, and confirm that export-only mode prevents analysis.

## Reference(s):

- [API and input guidance](references/api_doc.md)
- [Skill demonstration](https://lifeemergence.com/sample.html)
- [ClawHub release page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-fish-respiratory-rate-monitor-analysis)

## Skill Output:

**Output Type(s):** [text, markdown]

**Output Format:** [Structured monitoring report with estimated respiratory rate, status or warning, suggested checks, and report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include fish-specific baseline comparisons and historical report links; estimates are not diagnoses.]

## Skill Version(s):

1.0.15 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
