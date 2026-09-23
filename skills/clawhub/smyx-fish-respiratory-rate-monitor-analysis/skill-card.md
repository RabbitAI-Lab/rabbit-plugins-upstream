## Description:

Analyzes fixed-camera aquarium video to estimate fish gill-opening respiratory rate and surface abnormal breathing or hypoxia alerts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Aquarium operators, fish farms, laboratories, and developers use this skill to analyze close-up fish video, calculate respiratory rate in breaths per minute, and produce warnings or reports when visual signals suggest abnormal breathing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends aquarium videos, report history, and identity fields to configured cloud services.

Mitigation: Install only for trusted use cases, review configured endpoints before running, and avoid sensitive workspaces unless cloud processing is acceptable.

Risk: The skill can silently create or reuse identity state and store local tokens.

Mitigation: Run in an isolated workspace or account, review local token storage expectations, and clear local state when identity persistence is not desired.

Risk: Automatic cloud history queries may expose prior reports through the configured service.

Mitigation: Use accounts with appropriate report access and confirm that report history retrieval is acceptable before enabling history-list workflows.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-fish-respiratory-rate-monitor-analysis)
- [Publisher profile](https://clawhub.ai/user/smyx-sunjinhui)
- [API documentation](references/api_doc.md)
- [SMYX analysis API documentation](skills/smyx_analysis/references/api_doc.md)
- [Skill demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown reports and JSON or text CLI output from cloud API calls]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include respiratory-rate metrics, alert levels, recommended actions, history tables, report links, and an optional output file.]

## Skill Version(s):

1.0.9 (source: server release evidence; artifact frontmatter says 1.0.11)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
