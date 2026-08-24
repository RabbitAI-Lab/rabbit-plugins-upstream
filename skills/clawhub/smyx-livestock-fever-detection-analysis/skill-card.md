## Description:

Detects abnormal body temperature rise or drop in livestock and poultry from thermal or visible-light imagery, and outputs fever/hypothermia early warnings based on visual thermal features.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Farm operators, animal-health staff, and agents use this skill to screen livestock and poultry imagery or video for visual signs of abnormal body temperature. It supports early warning workflows by returning structured fever or hypothermia findings, individual locations, estimated temperature ranges, and report links.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Farm imagery, video, and URLs are sent to remote LifeEmergence services for analysis.

Mitigation: Use only inputs approved for external processing and confirm retention, deletion, and access controls before deployment.

Risk: The skill can create or reuse an internal account identity and store tokens locally without a user-facing setup step.

Mitigation: Run the skill in an isolated workspace, review local token and identity storage, and prefer a version that asks before account setup.

Risk: History lookup can retrieve cloud reports associated with the current identity.

Mitigation: Limit use of history commands to authorized operators and verify the active identity before querying cloud report history.

Risk: Temperature abnormality results are screening signals, not veterinary diagnoses.

Mitigation: Require veterinary or laboratory confirmation before disease diagnosis, treatment, quarantine, or culling decisions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-livestock-fever-detection-analysis)
- [API documentation](references/api_doc.md)
- [Skill demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [text, markdown, json, shell commands, configuration]

**Output Format:** [Markdown text with JSON-formatted structured analysis, history listings, and report links.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs are generated through remote LifeEmergence services; local uploads and URL inputs are supported, with documented file-size and media-format limits.]

## Skill Version(s):

1.0.9 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
