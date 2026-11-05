## Description:

Build and maintain GitLab CI/CD pipelines with the CI Tools Components Catalog at ci-tools.xrow.de. Use when creating or fixing .gitlab-ci.yml files, choosing CI Tools components, validating component inputs, or designing continuous delivery pipelines for applications, Helm charts, containers, packages, documentation, infrastructure, and GitOps.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xrowgmbh](https://clawhub.ai/user/xrowgmbh)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and platform engineers use this skill to create or repair GitLab CI/CD pipelines by selecting CI Tools catalog components, validating inputs, and planning gated delivery workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The recommended label component may automatically delete existing project labels.

Mitigation: Omit the label component or set prune:false unless deleting unlisted labels is intended.

Risk: External component behavior was not verified and may change between revisions.

Mitigation: Review and pin component revisions before using them.

Risk: Overly broad credentials or ungated deployment jobs can allow unintended writes.

Mitigation: Limit token permissions and retain deployment gates.

Risk: Sensitive configuration may be linted against the wrong GitLab destination.

Mitigation: Verify the GitLab destination before linting sensitive configuration.

## Reference(s):

- [CI Tools catalog](https://ci-tools.xrow.de/)
- [CI Tools components index](https://ci-tools.xrow.de/Components/)
- [CI Tools source project](https://gitlab.com/xrow-public/ci-tools)

## Skill Output:

**Output Type(s):** [Guidance, Configuration, Shell commands]

**Output Format:** [Markdown with YAML pipeline examples and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Project-specific pipeline recommendations and configuration examples.]

## Skill Version(s):

1.129.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
