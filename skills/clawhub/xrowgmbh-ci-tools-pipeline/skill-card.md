## Description:

Build and maintain GitLab CI/CD pipelines with the CI Tools Components Catalog at ci-tools.xrow.de.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xrowgmbh](https://clawhub.ai/user/xrowgmbh)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to create, repair, and validate GitLab CI/CD pipelines that rely on the CI Tools Components Catalog for application, container, Helm, package, documentation, infrastructure, and GitOps workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Mutable CI component references such as @main can change the code that runs in a user's pipelines after the configuration is accepted.

Mitigation: Prefer immutable commit SHAs or protected version tags for CI component includes, and review generated .gitlab-ci.yml changes before use.

Risk: Generated pipeline changes may grant registry, release, or deployment jobs broader credentials or permissions than needed.

Mitigation: Confirm that write-capable jobs receive only the credentials and permissions required for the intended workflow.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/xrowgmbh/skills/xrowgmbh-ci-tools-pipeline)
- [CI Tools Catalog](https://ci-tools.xrow.de/)
- [CI Tools Components Index](https://ci-tools.xrow.de/Components/)
- [CI Tools Source](https://gitlab.com/xrow-public/ci-tools)

## Skill Output:

**Output Type(s):** [Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with YAML and bash code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include GitLab CI configuration snippets, component include guidance, validation commands, and review checklist items.]

## Skill Version(s):

1.91.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
