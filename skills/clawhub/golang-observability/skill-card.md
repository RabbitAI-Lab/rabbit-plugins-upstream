## Description:

Guides agents adding or reviewing Go production observability across structured logging, Prometheus metrics, OpenTelemetry tracing, profiling, RUM, alerting, and Grafana dashboards.

This skill is ready for commercial/non-commercial use.

## Publisher:

[samber](https://clawhub.ai/user/samber)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to instrument Go services, review observability changes, and audit coverage across logs, metrics, traces, profiles, RUM events, alerts, and dashboards.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Telemetry changes can expose secrets or unnecessary personal data in logs, traces, analytics events, or vendor backends.

Mitigation: Review generated telemetry for secret handling, personal-data minimization, consent checks, and approved vendors or self-hosted backends before deployment.

Risk: Prometheus metrics can create high-cardinality labels that increase cost or reduce monitoring reliability.

Mitigation: Use normalized route labels and bounded label values, and review metric names and labels before shipping.

Risk: Profiling endpoints and continuous profiling can expose sensitive runtime data or add production overhead.

Mitigation: Protect pprof endpoints, keep profiling toggled by environment or policy, and review overhead before enabling it broadly.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/samber/skills/golang-observability)
- [Project homepage](https://github.com/samber/cc-skills-golang)
- [Structured Logging](references/logging.md)
- [Metrics with Prometheus](references/metrics.md)
- [Distributed Tracing with OpenTelemetry](references/tracing.md)
- [Profiling and Continuous Profiling](references/profiling.md)
- [Real User Monitoring and Product Observability](references/rum.md)
- [Alerting](references/alerting.md)
- [Grafana Dashboards for Go Services](references/dashboards.md)
- [Awesome Prometheus Alerts](https://samber.github.io/awesome-prometheus-alerts/)
- [Prometheus Metric Naming](https://prometheus.io/docs/practices/naming/)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with Go code snippets, PromQL and YAML examples, shell commands, and configuration edits.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Go tooling when applying or validating instrumentation changes.]

## Skill Version(s):

1.3.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
