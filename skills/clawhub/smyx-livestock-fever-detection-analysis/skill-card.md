## Description:

Detects abnormal body temperature rise or drop in livestock and poultry from thermal or visible-light imagery, and outputs fever/hypothermia early warnings based on visual thermal features.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

External users and farm operations teams use this skill to screen livestock and poultry thermal or visible-light images and videos for abnormal body-temperature patterns. It provides structured fever or hypothermia early-warning reports, abnormal individual lists, estimated temperature ranges, and report links for herd health screening, not veterinary diagnosis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Supplied images, videos, or URLs are sent to external Life Emergence APIs for analysis.

Mitigation: Use the skill only with media that is approved for external processing and disclose that external API processing is part of the workflow.

Risk: The skill can silently create or reuse an account identity and query cloud report history.

Mitigation: Review account-linking behavior before installation and restrict use to workspaces where this identity association is acceptable.

Risk: Account tokens may be stored in a workspace SQLite database.

Mitigation: Apply local credential handling controls, limit workspace access, and remove persisted credentials when the skill is no longer needed.

Risk: Body-temperature analysis is an early-warning screening aid and may be mistaken for veterinary diagnosis.

Mitigation: Present outputs as screening results only and require professional veterinary or laboratory confirmation before disease diagnosis or treatment decisions.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-livestock-fever-detection-analysis)
- [API Interface Documentation](references/api_doc.md)
- [Skill Demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown and JSON-oriented structured analysis text, with optional file output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes abnormality level, estimated temperature range, individual locations, abnormal individual lists, historical report tables, and report links when returned by the service.]

## Skill Version(s):

1.0.7 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
