## Description:

Analyzes aquarium video to estimate fish gill-cover breathing rate and provide respiratory monitoring results and alerts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Aquarists, aquarium staff, and fish keepers can use this skill to review aquarium video for gill-cover breathing rate patterns, receive respiratory alerts, and view monitoring reports. Results are visual monitoring signals and are not a veterinary diagnosis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Remote video uploads and unclear destinations may expose aquarium footage or associated identity data.

Mitigation: Before installing, ask the maintainer to identify what video and identity data are sent and where they go; avoid installation until those details are explained.

Risk: Account creation and token storage behavior is unclear.

Mitigation: Ask the maintainer to explain account creation and token storage before installation.

Risk: The security scan was partial because one local reference could not be resolved.

Mitigation: Treat the unresolved reference as a coverage gap; the other scanner's no-findings result does not establish that the skill is safe.

## Reference(s):

- [Skill API reference](artifact/references/api_doc.md)
- [Skill demonstration](https://lifeemergence.com/sample.html)
- [ClawHub release](https://clawhub.ai/smyx-sunjinhui/skills/smyx-fish-respiratory-rate-monitor-analysis)

## Skill Output:

**Output Type(s):** [Analysis, JSON, Markdown, Guidance, Reports]

**Output Format:** [Structured analysis reports and Markdown history listings with report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports respiratory rate and alert information from aquarium imagery or video; recommendations do not control aquarium equipment.]

## Skill Version(s):

1.0.13 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
