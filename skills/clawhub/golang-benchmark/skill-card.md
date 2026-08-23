## Description:

Golang benchmarking, profiling, and performance measurement for writing, running, comparing, and interpreting Go benchmarks, pprof profiles, execution traces, CI regressions, and Prometheus runtime metrics.

This skill is ready for commercial/non-commercial use.

## Publisher:

[samber](https://clawhub.ai/user/samber)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to create statistically sound Go benchmarks, compare optimization variants, profile CPU and memory hot paths, inspect traces, and set up benchmark regression checks. It is intended for Go projects where performance claims need measurement, reproducibility, and clear interpretation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Profiles, traces, goroutine dumps, and Prometheus investigation data can expose sensitive runtime behavior or application details.

Mitigation: Treat diagnostic artifacts as sensitive, share them only with authorized reviewers, and store or delete them according to the project's data-handling rules.

Risk: pprof and trace HTTP endpoints or browser UIs can expose diagnostics if reachable beyond the local investigation context.

Mitigation: Keep pprof and trace UIs local or behind access controls, and disable temporary investigation endpoints after the session.

Risk: Insecure TLS profile collection can weaken confidentiality when used against production services.

Mitigation: Use verified TLS and appropriate client credentials for production diagnostics; reserve insecure TLS examples for controlled non-production environments.

Risk: Privileged CPU-tuning commands for benchmark runners can affect host behavior and other workloads.

Mitigation: Run sudo CPU-tuning commands only on dedicated benchmark runners administered for that purpose, and restore runner settings after measurement.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/samber/skills/golang-benchmark)
- [Homepage](https://github.com/samber/cc-skills-golang)
- [pprof Reference](references/pprof.md)
- [benchstat Reference](references/benchstat.md)
- [Trace Reference](references/trace.md)
- [Diagnostic Tools Quick Reference](references/tools.md)
- [Compiler Analysis Reference](references/compiler-analysis.md)
- [CI Benchmark Regression Detection](references/ci-regression.md)
- [Investigation Session Setup](references/investigation-session.md)
- [Prometheus Go Runtime Metrics Reference](references/prometheus-go-metrics.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with Go code snippets and shell command blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose benchmark commands, profile collection steps, PromQL queries, CI configuration, and Go code changes for measurement workflows.]

## Skill Version(s):

1.3.0 (source: artifact frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
