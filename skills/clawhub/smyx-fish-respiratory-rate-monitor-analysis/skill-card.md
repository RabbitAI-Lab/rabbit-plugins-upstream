## Description:

Through fixed cameras on aquariums, the system analyzes fish gill-cover opening / closing motion video, detects periodic gill opening and closing, and calculates respiratory rate in breaths per minute.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

External users, aquarists, aquarium operators, ornamental fish farms, and laboratories use this skill to analyze close-up aquarium camera media, estimate fish respiratory rate, surface abnormal breathing patterns, and produce structured respiratory health reports with suggested non-diagnostic actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Aquarium photos, videos, or URLs are processed by a configured cloud service.

Mitigation: Use the skill only when cloud processing is acceptable, avoid private media or URLs unless authorized, and confirm deployment consent for shared aquarium, public aquarium, or laboratory settings.

Risk: The skill can silently create or reuse a local account identity and store session tokens locally.

Mitigation: Review or clear the workspace data directory before and after use when reused identities or local tokens are not desired.

Risk: Respiratory-rate results may be unreliable when input video is unclear, too short, low frame-rate, occluded, or missing fish-species and water-temperature context.

Mitigation: Require clear close-up side-view media, adequate sampling duration, species and water-temperature context, and treat low signal-stability results as a reason to retake the video rather than issue an alert.

Risk: The skill produces abnormal-breathing warnings and suggested actions that could be mistaken for veterinary diagnosis or automated device control.

Mitigation: Use outputs as visual monitoring guidance only, avoid medication names or doses, require user confirmation for aquarium equipment changes, and consult a qualified aquatic animal professional for severe or repeated alerts.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-fish-respiratory-rate-monitor-analysis)
- [Skill Demo](https://lifeemergence.com/sample.html)
- [API Documentation](references/api_doc.md)
- [Analysis API Documentation](skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown and JSON-oriented structured reports with command examples and report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports can include respiratory BPM, signal stability, alert level, recommended actions, disclaimer text, and cloud report links.]

## Skill Version(s):

1.0.6 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
