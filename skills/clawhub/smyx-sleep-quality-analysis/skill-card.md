## Description:

Identifies sleep stages including falling asleep, light sleep, deep sleep, and REM; monitors body movement, nighttime awakenings, and sleep apnea, suitable for sleep monitoring scenarios.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to analyze sleep-monitoring video or image inputs, identify sleep stages, body movement, awakenings, and possible sleep apnea, and generate structured sleep-quality reports. It can also retrieve historical sleep-analysis report lists from the publisher's cloud service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sleep-monitoring media and prior report metadata may be sent to the publisher's cloud service.

Mitigation: Use only with appropriate consent and review suitability before sending health-adjacent media or metadata, especially in shared, regulated, or multi-user environments.

Risk: The skill may silently create or reuse a local/cloud-linked identity and persist authentication tokens locally.

Mitigation: Review local identity and token database handling before deployment, and disable or isolate the behavior when identity persistence is not acceptable.

Risk: Historical report listing can automatically retrieve prior reports from the cloud service with weak user control.

Mitigation: Review or disable automatic history-listing behavior where users should explicitly approve retrieval of prior health-adjacent reports.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-sleep-quality-analysis)
- [Skill demo](https://lifeemergence.com/sample.html)
- [API documentation](references/api_doc.md)
- [Analysis API documentation](skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, JSON, Files]

**Output Format:** [Markdown and JSON-formatted text, with optional saved output files and report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports are sleep-quality references only and are not a substitute for professional diagnosis.]

## Skill Version(s):

1.0.12 (source: server release evidence; artifact frontmatter reports 1.0.11)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
