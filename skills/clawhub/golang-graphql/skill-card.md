## Description:

Implements GraphQL APIs in Golang using gqlgen or graphql-go.

This skill is ready for commercial/non-commercial use.

## Publisher:

[samber](https://clawhub.ai/user/samber)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to build, review, and maintain Go GraphQL services with gqlgen or graph-gophers/graphql-go, including schema design, resolver implementation, subscriptions, testing, and production safety checks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can help an agent read and edit Go GraphQL code and run Go-related commands.

Mitigation: Review proposed code changes and command effects before applying them in production repositories.

Risk: Generated gqlgen files and configuration can be overwritten or misconfigured during code generation.

Mitigation: Keep custom logic outside generated files, review gqlgen configuration, and rerun tests after generation.

Risk: Public GraphQL handlers can expose schema details or allow expensive nested queries if production safeguards are omitted.

Mitigation: Require handler review for introspection gating, query complexity or depth limits, and error sanitization before deployment.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/samber/skills/golang-graphql)
- [Publisher profile](https://clawhub.ai/user/samber)
- [Project homepage](https://github.com/samber/cc-skills-golang)
- [gqlgen reference](references/gqlgen.md)
- [graph-gophers/graphql-go reference](references/graphql-go.md)
- [Testing reference](references/testing.md)
- [gqlgen](https://github.com/99designs/gqlgen)
- [graph-gophers/graphql-go](https://github.com/graph-gophers/graphql-go)
- [Relay cursor connections spec](https://relay.dev/graphql/connections.htm)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline Go, GraphQL, YAML, and shell code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May suggest Go source edits, generated-code workflows, gqlgen configuration, resolver tests, and production GraphQL hardening steps.]

## Skill Version(s):

0.2.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
