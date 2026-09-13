## Description:

Helps agents and developers treat model JSON as untrusted input by validating required fields, types, enums, and nested structure before downstream code consumes it.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhaoxinghua09-cell](https://clawhub.ai/user/zhaoxinghua09-cell)

### License/Terms of Use:

MIT

## Use Case:

Developers and agent builders use this skill to add a schema guard around LLM structured output before sending it to APIs, databases, forms, function calls, or other code paths.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The advertised validation gate can fail open, so callers may treat invalid model output as accepted if they rely only on the CLI exit status.

Mitigation: Review validation output explicitly and do not use the CLI exit status as a CI or security gate until the fail-open behavior is fixed.

Risk: The documented installation path uses mutable, unpinned sources.

Mitigation: Install from a pinned, reviewable source and verify the release hash before deploying the skill.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zhaoxinghua09-cell/skills/output-schema-guard)
- [Publisher profile](https://clawhub.ai/user/zhaoxinghua09-cell)
- [LGD hub homepage](https://zhaoxinghua09-cell.github.io/lgd-hub/)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON schema examples and optional shell command usage]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The included CLI can emit JSON validation results with pass status and per-field issues.]

## Skill Version(s):

1.0.0 (source: server release metadata; artifact frontmatter lists 1.1.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
