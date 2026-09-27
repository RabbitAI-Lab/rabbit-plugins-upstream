## Description:

Analyzes local authentication, web access, PowerShell, and Windows event logs for suspicious activity and produces a timeline with Chinese-language explanations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yottameta](https://clawhub.ai/user/yottameta)

### License/Terms of Use:

MIT-0

## Use Case:

Security analysts, incident responders, and developers use this skill to review logs they are authorized to inspect, triage possible intrusions, and obtain a chronological report with suggested checks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The npm installer may write to multiple agent directories without the safeguards described in the skill documentation.

Mitigation: Review the installer before use and choose an explicit single target with --agent or --dir; avoid global or no-argument installation.

Risk: Running an unreviewed package source through npx may introduce unexpected installation behavior.

Mitigation: Pin or manually review the package source before running npx.

Risk: Analyzing logs without permission may expose sensitive system or user data.

Mitigation: Analyze only logs you are authorized to inspect.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/yottameta/skills/yotta-logwatch)
- [Project homepage listed in ClawHub metadata](https://github.com/YottaMeta/yotta-logwatch)
- [Analysis specification](references/analysis-spec.md)
- [Authentication log rules](references/auth-log-rules.md)
- [Web log rules](references/web-log-rules.md)
- [PowerShell log rules](references/powershell-log-rules.md)
- [Windows event rules](references/windows-event-rules.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON]

**Output Format:** [Plain-text, Markdown, or JSON timeline and findings report]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes severity, supporting log lines, Chinese-language explanations, and review suggestions.]

## Skill Version(s):

0.3.0 (source: ClawHub release and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
