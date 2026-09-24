## Description:

Analyzes fixed-camera walking video to estimate gait metrics such as step length, gait speed, trunk sway, and cadence, then returns gait stability signals and fall-risk classifications.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

External users, caregivers, care organizations, and health-platform developers use this skill to analyze elderly walking videos or URLs and receive structured gait metrics, fall-risk levels, report links, and history lookups. Outputs are screening aids and do not replace professional medical or rehabilitation evaluation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Elderly gait videos, video URLs, and health report links may contain sensitive health or personal data and are sent to configured cloud services.

Mitigation: Use only with informed consent and acceptable retention, access-control, encryption, and report-sharing practices; avoid protected or highly sensitive footage unless those controls are in place.

Risk: The skill can silently create or reuse a persistent local/cloud identity for history and report retrieval.

Mitigation: Review identity behavior before deployment and ensure users or administrators understand and approve how reports are associated and retrieved.

Risk: Fall-risk outputs are screening signals and may be incorrect or incomplete for clinical decisions.

Mitigation: Treat results as advisory gait observations and route concerning findings to qualified medical or rehabilitation professionals.

## Reference(s):

- [API interface documentation](references/api_doc.md)
- [Shared analysis API documentation](skills/smyx_analysis/references/api_doc.md)
- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-elderly-gait-instability-detection-analysis)
- [Skill demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown and JSON-style structured analysis text with command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include gait metrics, fall-risk level, risk factors, alert text, report links, and history tables.]

## Skill Version(s):

1.0.10 (source: server release metadata; artifact frontmatter reports 1.0.15)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
