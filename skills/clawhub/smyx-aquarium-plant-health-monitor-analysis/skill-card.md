## Description:

Analyzes aquarium plant images and videos for visible health issues and provides care suggestions and cloud report history.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Aquarium keepers, aquascapers, and aquarium shops use the skill to assess aquatic plant symptoms from images or video, receive care suggestions, and review cloud-stored reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Aquarium images, videos, and report-history queries are sent to lifeemergence.com services.

Mitigation: Review the service and obtain consent before sending media or querying cloud history.

Risk: The skill automatically creates or reuses an identity and stores service tokens in a local SQLite database.

Mitigation: Limit local access to the workspace and its stored tokens; use only if this identity and token handling is acceptable.

Risk: A hidden caller-supplied identity parameter can affect access to cloud report history.

Mitigation: Do not allow untrusted callers or automation to supply identity parameters; prefer a release with authentication and report-ownership checks.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/smyx-sunjinhui/skills/smyx-aquarium-plant-health-monitor-analysis)
- [Aquarium plant monitoring API reference](references/api_doc.md)
- [Skill introduction](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Text or Markdown health reports, care suggestions, and historical report tables]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include cloud report links; results can be saved to a local file.]

## Skill Version(s):

1.0.13 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
