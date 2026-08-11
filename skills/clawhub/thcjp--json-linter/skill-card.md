## Description:

JSON检查工具 checks workspace JSON files for syntax errors and reports invalid files with error details.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thcjp](https://clawhub.ai/user/thcjp)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and automation users use this skill to scan workspace JSON configuration and data files, identify syntax errors, and receive a structured report for follow-up fixes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review marks the skill suspicious because it requests broader powers than a local JSON syntax checker needs.

Mitigation: Install and run it only in a constrained workspace, and prefer a read-only, local-only implementation for routine linting.

Risk: The artifact declares read, exec, and write tool access, which could allow command execution or file changes during a linting workflow.

Mitigation: Review proposed commands before execution, avoid granting write access unless required, and keep scans limited to intended project files.

Risk: The artifact mentions API-key setup and possible external API use, which can expose sensitive configuration if handled carelessly.

Mitigation: Do not provide secrets unless an external service is explicitly required, keep API keys in environment variables, and avoid scanning or logging secret-bearing files.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thcjp/skills/json-linter)

## Skill Output:

**Output Type(s):** [text, json, guidance]

**Output Format:** [JSON report with file counts, invalid-file details, parse errors, and concise remediation guidance when needed.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports scanned_at, total_files, valid_files, invalid_files, and errors with relative paths and parser messages.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
