## Description:

Search source code with the sngs sparse n-gram index. Use for fast literal or regex searches, repeated repository searches, machine-readable code-search results, index initialization, incremental Git updates, and search diagnostics.

This skill is ready for commercial/non-commercial use.

## Publisher:

[albert-lv](https://clawhub.ai/user/albert-lv)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to search repositories for literal strings, regular expressions, and code patterns, and to initialize or refresh a local search index. It also helps agents choose suitable result formats and account for index freshness when reporting search findings.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The executable code built from the upstream source was outside the supplied release artifact.

Mitigation: Review the upstream source and pin the source revision before building.

Risk: Indexes and search output may contain private source code or sensitive paths.

Mitigation: Limit indexing to intended repositories and keep indexes and search output private.

Risk: Local usage statistics are enabled unless disabled.

Mitigation: Set SNGS_NO_STATS=1 to disable the documented local statistics.

## Reference(s):

- [sparse-ngram-search project homepage](https://github.com/nano-harness/sparse-ngram-search)
- [sngs-helper release on ClawHub](https://clawhub.ai/albert-lv/skills/sngs-helper)

## Skill Output:

**Output Type(s):** [Text, JSON, Shell commands, Guidance]

**Output Format:** [Search results as text, grep-style lines, or JSON, with Markdown usage guidance and inline shell commands.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Search results may include matching file paths, lines, and counts; output depends on the selected sngs format.]

## Skill Version(s):

1.0.0 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
