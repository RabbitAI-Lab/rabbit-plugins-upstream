## Description:

Identifies sleep stages including falling asleep, light sleep, deep sleep, and REM; monitors body movement, nighttime awakenings, and sleep apnea, suitable for sleep monitoring scenarios.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to analyze sleep-monitoring video files or public video URLs, identify sleep stages and movement or apnea indicators, and return structured sleep-quality reports or report-history tables.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sleep videos, remote video URLs, and report history may be processed by lifeemergence.com cloud services.

Mitigation: Install and run only when the user accepts third-party cloud processing of sensitive sleep-monitoring media and account-linked history.

Risk: The skill can create or reuse a local account identity and store tokens or profile data in a workspace SQLite database.

Mitigation: Use a dedicated workspace, restrict access to the workspace data directory, and clear stored identity or token data when it is no longer needed.

Risk: Sleep-stage and apnea outputs are health-related and may be incomplete or inaccurate.

Mitigation: Treat results as informational sleep-quality references, not as a substitute for clinical sleep monitoring or medical diagnosis.

## Reference(s):

- [API 接口文档](references/api_doc.md)
- [API接口文档](skills/smyx_analysis/references/api_doc.md)
- [Skill demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Shell commands, Configuration]

**Output Format:** [Markdown reports, Markdown tables, or JSON text depending on the selected detail level and report-history mode]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can save output to a user-selected file path.]

## Skill Version(s):

1.0.13 (source: SKILL.md frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
