## Description: <br>
Sentry.io error monitoring via sentry-cli. Use when working with Sentry releases, source maps, dSYMs, events, or issue management. Covers authentication, release workflows, deploy tracking, and debug file uploads. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[iahmadzain](https://clawhub.ai/user/iahmadzain) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and release engineers use this skill as a Sentry CLI command reference for authentication, release management, deploy tracking, source map uploads, debug file uploads, issue workflows, monitors, and CI/CD integration. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Sentry authentication tokens and project identifiers may be exposed if copied into source files, logs, or shared build artifacts. <br>
Mitigation: Use scoped Sentry tokens stored in a secret manager or protected environment, and keep .sentryclirc out of source control. <br>
Risk: Source maps, debug files, logs, and build artifacts can contain sensitive application or user information before upload. <br>
Mitigation: Review and redact logs and build artifacts before uploading them to Sentry. <br>
Risk: Example Sentry CLI commands can change release, deploy, issue, monitor, or account state when run against a live organization. <br>
Mitigation: Treat the skill as a command reference and review commands, organization, project, environment, and token scope before execution. <br>


## Reference(s): <br>
- [Sentry CLI installer](https://sentry.io/get-cli/) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with bash, INI, and YAML code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Provides command examples and configuration snippets for Sentry CLI workflows.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
