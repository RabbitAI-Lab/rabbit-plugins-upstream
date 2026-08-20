## Description:

Loop Polish automates full-stack quality checks, browser verification, scoring, conservative auto-fixes, regression loops, and release reports for development or staging projects.

This skill is ready for commercial/non-commercial use.

## Publisher:

[lqclf](https://clawhub.ai/user/lqclf)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineering teams use Loop Polish as a pre-release QA and acceptance loop for full-stack applications in development or staging environments. It starts services, verifies APIs, browser flows, and database state, scores quality, applies controlled fixes, reruns regressions, and produces a report.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Full mode can change source code, mutate application data, and read database credentials automatically.

Mitigation: Run it only in disposable development or staging environments with test data; start with preflight mode or set db_verify=false when database access is not needed.

Risk: Automated fixes may introduce incorrect behavior or broad changes, especially with moderate or aggressive strategies.

Mitigation: Begin with the conservative strategy, review the generated branch and diff before merging, and require human approval for schema, authentication, or large deletion changes.

Risk: Diagnostics can include sensitive runtime details if not handled carefully.

Mitigation: Redact authorization headers, cookies, passwords, tokens, secrets, and database connection strings from reports, logs, and saved state.

Risk: Service startup and cleanup can affect local processes on common development ports.

Mitigation: Only terminate processes confirmed to belong to the target project, and ask before touching unrelated processes.

## Reference(s):

- [Loop Polish ClawHub release](https://clawhub.ai/lqclf/skills/loop-polish-skills)
- [README.md](artifact/README.md)
- [SKILL.md](artifact/SKILL.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown reports with inline command, configuration, and code-diff details]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Full mode may create a working branch, state file, quality report, and code changes; diagnostics should redact credentials, tokens, cookies, and passwords.]

## Skill Version(s):

1.1.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
