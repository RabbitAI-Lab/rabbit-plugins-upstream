## Description:

Build Grafana dashboards as code with the grafana-foundation-sdk typed builders (TypeScript or Go). Use when creating, modifying, or generating Grafana dashboard JSON programmatically, converting hand-written dashboard JSON to typed code, building monitoring dashboards, or working with Prometheus/Loki queries in dashboards.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tenequm](https://clawhub.ai/user/tenequm)

### License/Terms of Use:

Apache 2.0

## Use Case:

Developers and operations engineers use this skill to create, modify, or convert Grafana dashboards as typed TypeScript or Go code, including Prometheus and Loki dashboard patterns.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated dashboard files can overwrite existing dashboard JSON when examples or generated scripts are run.

Mitigation: Review file paths and generated diffs before committing or deploying dashboard output.

Risk: The referenced SDK is pre-1.0, so API behavior can change between releases.

Mitigation: Pin the SDK version and review changes before updating the dependency.

Risk: Incorrect queries, thresholds, or transformations can produce misleading monitoring dashboards.

Mitigation: Review generated dashboard JSON and validate Prometheus, Loki, and Grafana behavior before deployment.

## Reference(s):

- [Common Dashboard Patterns](references/patterns.md)
- [TypeScript API Reference](references/typescript-api.md)
- [ClawHub skill page](https://clawhub.ai/tenequm/skills/grafana-foundation-sdk)
- [Project homepage](https://github.com/tenequm/skills/tree/main/skills/grafana-foundation-sdk)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration]

**Output Format:** [Markdown with TypeScript, Go, JSON, and bash code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include generated Grafana dashboard JSON or Kubernetes dashboard manifests when requested.]

## Skill Version(s):

0.2.4 (source: frontmatter and changelog, released 2026-08-21)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
