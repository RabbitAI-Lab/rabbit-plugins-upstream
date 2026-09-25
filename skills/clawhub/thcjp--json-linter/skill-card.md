## Description:

Validates JSON syntax across a workspace, identifies configuration syntax errors, and returns a structured JSON report of scanned files and parsing errors.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thcjp](https://clawhub.ai/user/thcjp)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to scan workspace JSON files, find syntax errors in configuration or data files, and receive a concise machine-readable validation report.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security evidence marks the release as suspicious because it requests broader read, execute, and write powers than a simple JSON syntax checker appears to need.

Mitigation: Review before installing, use only in a workspace where those powers are acceptable, and constrain the skill to JSON validation.

Risk: The artifact mentions API key and network/API behavior even though those capabilities are not clearly needed for local JSON linting.

Mitigation: Do not provide an API key or allow network/API behavior unless the publisher clarifies why it is required for linting.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thcjp/skills/json-linter)
- [Skill homepage](https://skillhub.cn/skill/)

## Skill Output:

**Output Type(s):** [JSON, Guidance]

**Output Format:** [JSON report]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes scanned_at, total_files, valid_files, invalid_files, and per-file error details.]

## Skill Version(s):

1.0.1 (source: server release metadata; artifact frontmatter lists 1.0.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
