## Description: <br>
Build Grafana dashboards as code with grafana-foundation-sdk typed builders for TypeScript or Go. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[tenequm](https://clawhub.ai/user/tenequm) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and infrastructure engineers use this skill to create, modify, generate, or convert Grafana dashboard JSON through typed builder APIs. It is suited for monitoring dashboard work that includes Prometheus and Loki queries, reusable dashboard components, and generated dashboard files. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill pins a pre-1.0 Grafana Foundation SDK version, so API changes may affect generated dashboard code. <br>
Mitigation: Confirm the pinned SDK version is acceptable for the target project before adopting or updating generated code. <br>
Risk: Generated dashboard JSON may include project-specific datasource UIDs, namespaces, or output paths. <br>
Mitigation: Review dashboard JSON diffs before committing or deploying generated files. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/tenequm/skills/grafana-foundation-sdk) <br>
- [ClawHub metadata homepage](https://github.com/tenequm/skills/tree/main/skills/grafana-foundation-sdk) <br>
- [Common Dashboard Patterns](references/patterns.md) <br>
- [TypeScript API Reference](references/typescript-api.md) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, code, shell commands, configuration] <br>
**Output Format:** [Markdown with TypeScript, Go, JSON, and shell command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces dashboard-as-code guidance and examples that may generate Grafana dashboard JSON.] <br>

## Skill Version(s): <br>
0.2.2 (source: server release metadata, SKILL.md metadata, CHANGELOG.md released 2026-07-22) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
