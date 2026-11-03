## Description:

This skill analyzes video of a child's study area and produces per-minute focus scores, distraction events, and study-session reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Parents and teachers use the skill to review visual indicators of a child's attention during a study session, including focus scores and distraction periods. It can also retrieve prior reports associated with the user.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Child footage may be uploaded to a provider even when export-only mode is selected.

Mitigation: Do not use real child footage until export-only behavior is fixed; confirm guardian authorization, the receiving provider, and retention and deletion terms.

Risk: Private reports may be mixed across users.

Mitigation: Require sender isolation fixes before shared-user deployment and avoid shared-user use until then.

Risk: Authenticated requests and stored tokens could expose sensitive data if destinations or token handling are not controlled.

Mitigation: Restrict authenticated requests to approved HTTPS destinations and protect stored tokens.

## Reference(s):

- [Skill API reference](artifact/references/api_doc.md)
- [Skill release on ClawHub](https://clawhub.ai/smyx-sunjinhui/skills/smyx-child-focus-analysis-analysis)
- [Skill demonstration](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Analysis, JSON, Markdown]

**Output Format:** [Structured analysis reports in JSON and Markdown history tables]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes per-minute focus scores, distraction events and durations, an overall focus grade, and low-focus alerts.]

## Skill Version(s):

1.0.14 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
