## Description:

Identifies sleep stages including falling asleep, light sleep, deep sleep, and REM; monitors body movement, nighttime awakenings, and sleep apnea for sleep monitoring scenarios.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to submit sleep-monitoring video files or URLs to a cloud analysis service, retrieve structured sleep-stage, movement, awakening, and apnea findings, and list prior reports associated with the internal account identity.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sleep videos or URLs may be processed by the publisher's cloud service.

Mitigation: Use only media appropriate for vendor cloud processing and confirm privacy, retention, deletion, and account-control terms before using private in-home or medical footage.

Risk: The skill can silently create or reuse an account identity and store service tokens locally.

Mitigation: Run it in a controlled workspace, avoid sharing the workspace across users, and review or clear locally stored account data and tokens according to deployment policy.

Risk: Sleep analysis output is health-related and may be incomplete or inaccurate.

Mitigation: Treat results as sleep-quality reference information, not a replacement for professional sleep monitoring equipment or medical diagnosis.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-sleep-quality-analysis)
- [API documentation](references/api_doc.md)
- [Skill demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON]

**Output Format:** [Markdown report or JSON analysis result, with optional saved output file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Processes sleep-monitoring videos or URLs and can return historical report lists and report links.]

## Skill Version(s):

1.0.15 (source: server release metadata; artifact frontmatter says 1.0.16)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
