## Description:

Monitors home videos for pets entering restricted areas, climbing onto dining tables, or rummaging through trash, and produces alerts and structured reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

External users and pet owners can submit home monitoring videos to identify restricted-area entry and other specified pet behaviors. The skill returns an analysis report, alerts, and report links, and can list historical reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review flags a mismatch between the pet-monitoring description and reported behavior, along with unresolved questions about account registration, API-secret handling, video uploads, and report access.

Mitigation: Before installing, ask the publisher to clarify the mismatch and verify how credentials, video data, and report access are handled and authorized.

Risk: The security scan was partial, leaving some referenced-path evidence incomplete.

Mitigation: Review the complete release contents and finish the security review before installation.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-pet-restricted-area-warning-analysis)
- [Skill demonstration](https://lifeemergence.com/sample.html)
- [API notes (describe pet health analysis)](references/api_doc.md)

## Skill Output:

**Output Type(s):** [Text, JSON, Markdown, Report links]

**Output Format:** [Structured report text or JSON; historical reports as a Markdown list with links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Detail levels: basic, standard, or JSON; optional file output]

## Skill Version(s):

1.0.21 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
