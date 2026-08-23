## Description:

Golang OpenAPI/Swagger documentation with swaggo/swag, including annotation comments, swag init code generation, framework integrations, security definitions, and struct tags for Go projects.

This skill is ready for commercial/non-commercial use.

## Publisher:

[samber](https://clawhub.ai/user/samber)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to add, maintain, and audit Swagger/OpenAPI documentation for Go APIs that use swaggo/swag. It helps generate docs, wire Swagger UI endpoints, document handlers and models, and avoid common annotation mistakes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated Swagger documentation can become incorrect or misleading if it is not reviewed against the Go implementation.

Mitigation: Review generated docs changes before committing and rerun swag generation after annotation or handler changes.

Risk: The disclosed swag CLI install uses the latest upstream version, so behavior can change as upstream releases change.

Mitigation: Pin the swag CLI version in production or regulated workflows and validate generated OpenAPI output after upgrades.

Risk: Swagger UI can expose internal routes or protected API details when shipped without environment controls or access restrictions.

Mitigation: Disable or gate Swagger UI in production and use swag tag filtering for endpoints that should not appear in public specs.

## Reference(s):

- [swag CLI Reference](references/swag-cli.md)
- [ClawHub Skill Page](https://clawhub.ai/samber/skills/golang-swagger)
- [cc-skills-golang Homepage](https://github.com/samber/cc-skills-golang)
- [swaggo/swag Issues](https://github.com/swaggo/swag/issues)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with Go code snippets and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May recommend changes to Swagger annotations, Go imports, generated docs commands, and framework route configuration.]

## Skill Version(s):

1.1.0 (source: release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
