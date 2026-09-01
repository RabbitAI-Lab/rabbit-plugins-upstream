## Description:

Analyzes cat scratch post video or image inputs by calling publisher cloud APIs to estimate scratching frequency, session duration, and relative intensity, then returns structured observations about stress level and claw health without diagnosing disease or prescribing behavior correction.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

External users and pet-care developers use this skill to analyze cat scratch post media for scratching frequency, duration, relative intensity, stress-level observations, claw-health observations, and historical report lookup.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Pet media is sent to the publisher's cloud service for analysis.

Mitigation: Submit only media approved for that service and avoid sensitive household or personal content.

Risk: Activity can be linked to an account identity and cloud history.

Mitigation: Review identity and history behavior before deployment and disclose the cloud-linked workflow to users.

Risk: Authentication or profile data may be stored in a local workspace SQLite database.

Mitigation: Restrict workspace access and remove local credentials or profile data when the skill is no longer needed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-pet-scratch-frequency-intensity-analysis)
- [Skill API documentation](references/api_doc.md)
- [Shared analysis API documentation](skills/smyx_analysis/references/api_doc.md)
- [Skill demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [text, markdown, json, shell commands, configuration]

**Output Format:** [Markdown or JSON structured analysis report with optional report links and history tables]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include scratching counts, session duration, relative intensity, stress and claw-health observations, and cloud report links.]

## Skill Version(s):

1.0.8 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
