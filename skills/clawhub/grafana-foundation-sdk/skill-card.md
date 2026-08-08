## Description:

Build Grafana dashboards as code with the grafana-foundation-sdk typed builders (TypeScript or Go). Use when creating, modifying, or generating Grafana dashboard JSON programmatically, converting hand-written dashboard JSON to typed code, building monitoring dashboards, or working with Prometheus/Loki queries in dashboards.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tenequm](https://clawhub.ai/user/tenequm)

### License/Terms of Use:

Apache 2.0

## Use Case:

Developers and infrastructure engineers use this skill to create, modify, convert, and generate Grafana dashboards as typed TypeScript or Go code, then serialize them to Grafana dashboard JSON or deployment manifests.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated dashboards and Prometheus or Loki queries may expose sensitive operational data to dashboard viewers.

Mitigation: Review generated dashboards, datasource scopes, variables, and queries before deploying or sharing them.

Risk: Generated dashboard code can rely on pre-1.0 SDK behavior, unchecked TypeScript, or stale generated JSON.

Mitigation: Pin the SDK version, run project-local type checks or builds, regenerate dashboard JSON after generator edits, and review the generated output.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/tenequm/skills/grafana-foundation-sdk)
- [OpenClaw Homepage](https://github.com/tenequm/skills/tree/main/skills/grafana-foundation-sdk)
- [TypeScript API Reference](references/typescript-api.md)
- [Common Dashboard Patterns](references/patterns.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with TypeScript, Go, shell, and JSON snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce dashboard JSON or Kubernetes dashboard/provisioning manifests for review before deployment.]

## Skill Version(s):

0.2.3 (source: evidence release, frontmatter, changelog released 2026-08-07)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
