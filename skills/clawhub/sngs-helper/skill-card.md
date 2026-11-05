## Description:

Search source code with the sngs sparse n-gram index. Use for fast literal or regex searches, repeated repository searches, machine-readable code-search results, index initialization, incremental Git updates, and search diagnostics.

This skill is ready for commercial/non-commercial use.

## Publisher:

[albert-lv](https://clawhub.ai/user/albert-lv)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to search repositories for symbols, strings, configuration values, error messages, and other code patterns. It helps with repeat searches, index setup and updates, and getting results in text or machine-readable form.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Indexes, search results, or local usage statistics may expose private source code or sensitive paths if published.

Mitigation: Keep private indexes and results out of published files; set SNGS_NO_STATS=1 to disable local usage statistics when desired.

Risk: Building from source uses an upstream implementation that was not included in the review of the bundled skill files.

Mitigation: Review and pin the upstream source before building.

## Reference(s):

- [Project homepage](https://github.com/nano-harness/sparse-ngram-search)
- [ClawHub skill page](https://clawhub.ai/albert-lv/skills/sngs-helper)

## Skill Output:

**Output Type(s):** [Text, JSON, Shell commands, Guidance]

**Output Format:** [Search results as text, grep-style output, or JSON, with shell commands and Markdown guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Search output varies by selected format and filters; freshness may reflect the documented dirty-scan cache.]

## Skill Version(s):

1.0.1 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
