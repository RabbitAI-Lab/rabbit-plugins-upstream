## Description:

Build and maintain GitLab CI/CD pipelines with the CI Tools Components Catalog at ci-tools.xrow.de. Use when creating or fixing .gitlab-ci.yml files, choosing CI Tools components, validating component inputs, or designing continuous delivery pipelines for applications, Helm charts, containers, packages, documentation, infrastructure, and GitOps.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xrowgmbh](https://clawhub.ai/user/xrowgmbh)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and platform engineers use this skill to design, update, and validate GitLab CI/CD pipelines with reusable CI Tools components.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: GitLab CI linting uploads pipeline YAML to the configured GitLab instance, so embedded secrets could be exposed.

Mitigation: Keep secrets out of pipeline YAML and lint only against the intended GitLab instance using a project-scoped token.

Risk: Pipeline component changes can trigger CI actions or affect deployments.

Mitigation: Review component versions and pipeline effects before pushing or starting CI, and retain deployment gates.

## Reference(s):

- [CI Tools Catalog](https://ci-tools.xrow.de/)
- [CI Tools Components](https://ci-tools.xrow.de/Components/)
- [xrow-public CI Tools project](https://gitlab.com/xrow-public/ci-tools)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, YAML configuration, Shell commands]

**Output Format:** [Markdown with GitLab CI YAML examples and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires glab, curl, jq, and a GitLab token for the documented workflow.]

## Skill Version(s):

1.117.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
