## Description: <br>
Generate a full Phoenix JSON API from an OpenAPI spec or natural language description. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[gchapim](https://clawhub.ai/user/gchapim) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and engineers use this skill to scaffold Phoenix REST APIs from OpenAPI YAML or natural language descriptions, including contexts, schemas, migrations, controllers, JSON renderers, routes, authentication plugs, tenant scoping, and tests. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Tenant-security examples could lead generated applications to expose or modify another tenant's data. <br>
Mitigation: Derive tenant identity from verified authentication or membership, scope every read, update, and delete query by tenant at the context or query layer, and add tests that deny cross-tenant access. <br>
Risk: Generated authorization code may be incomplete for a production application. <br>
Mitigation: Review generated authentication and authorization code before use and adapt it to the application's verified identity, role, and membership model. <br>


## Reference(s): <br>
- [Phoenix Conventions Reference](references/phoenix-conventions.md) <br>
- [Ecto Patterns Reference](references/ecto-patterns.md) <br>
- [Test Patterns Reference](references/test-patterns.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with Elixir, Phoenix, Ecto, migration, router, plug, and ExUnit code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Generated API code should be reviewed before writing files, especially authentication and tenant-scoping logic.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
