## Description:

Golang performance optimization patterns and methodology - if X bottleneck, then apply Y.

This skill is ready for commercial/non-commercial use.

## Publisher:

[samber](https://clawhub.ai/user/samber)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to review and optimize Go code after profiling or benchmarks identify a bottleneck. It helps select appropriate allocation, CPU, memory layout, runtime, caching, I/O, observability, and hot-path optimization patterns.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may use benchmarks, profiling tools, Go tooling, git commands, web lookups, and code edits during optimization work.

Mitigation: Review proposed commands and changes before applying them to production systems, and run profiling or benchmarks in a controlled environment.

Risk: Performance changes can be misleading if they are made without a measured baseline or statistical comparison.

Mitigation: Start from profile or benchmark evidence, change one thing at a time, and re-measure with tools such as benchstat before accepting an optimization.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/samber/skills/golang-performance)
- [Project Homepage](https://github.com/samber/cc-skills-golang)
- [Memory Optimization](references/memory.md)
- [CPU Optimization](references/cpu.md)
- [I/O & Networking Optimization](references/io-networking.md)
- [Runtime Tuning](references/runtime.md)
- [Caching Patterns](references/caching.md)
- [Production Observability for Performance](references/observability.md)
- [Prometheus Alert Rules](assets/prometheus-alerts.yml)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline code blocks and command snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include benchmark comparison guidance, profiling recommendations, code edits, and configuration snippets.]

## Skill Version(s):

1.3.0 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
