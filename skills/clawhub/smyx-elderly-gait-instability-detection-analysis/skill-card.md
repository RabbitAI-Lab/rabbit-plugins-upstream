## Description:

Analyzes straight-line walking videos of older adults to estimate gait metrics such as step length, gait speed, cadence, and trunk sway, then returns a fall-risk level and structured report.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

External caregivers, care facilities, rehabilitation teams, and developers use this skill to submit walking videos or video URLs for gait metric extraction, fall-risk screening, and historical report lookup. Outputs are screening aids and do not replace professional medical evaluation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Walking videos or video URLs may be sent to lifeemergence cloud services for analysis.

Mitigation: Use only with informed consent from the recorded person or authorized caregiver, and confirm privacy, retention, deletion, and access controls before using real health-related footage.

Risk: Reports may be associated with a persistent internal identity, and local tokens may be stored in the workspace data directory.

Mitigation: Review account-linking and token-handling behavior before deployment, use isolated workspaces for evaluation, and clear local data when it is no longer needed.

Risk: Gait metrics and fall-risk levels could be mistaken for a medical diagnosis.

Mitigation: Present outputs as auxiliary screening information only and direct users to professional rehabilitation or neurological evaluation for clinical decisions.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-elderly-gait-instability-detection-analysis)
- [API Interface Documentation](references/api_doc.md)
- [Skill Demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [text, markdown, json, shell commands, guidance]

**Output Format:** [Markdown or JSON gait-analysis report with metrics, risk level, risk factors, recommendations, and report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can query historical cloud reports and can write an output file when requested.]

## Skill Version(s):

1.0.5 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
