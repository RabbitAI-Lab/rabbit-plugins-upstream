## Description:

API code generator. Generate RESTful endpoints, GraphQL schemas, OpenAPI/Swagger docs, API clients, mock servers, authentication, rate limiting.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ckchzh](https://clawhub.ai/user/ckchzh)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to scaffold API endpoints, GraphQL schemas, OpenAPI documents, clients, mock servers, authentication, rate limiting, and tests as starting points for implementation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated authentication scaffolding may be unsafe if copied directly into production code.

Mitigation: Review and harden generated JWT, OAuth, and API-key handling before use, including secret management and validation.

Risk: Generator inputs and generated API code may need project-specific validation before use.

Mitigation: Validate inputs, inspect generated endpoints and schemas, and add application-specific tests before deployment.

Risk: The auxiliary script can write local usage history when invoked.

Mitigation: Review local data-writing behavior and set an appropriate data directory or avoid commands that record history if that is not acceptable.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/ckchzh/skills/api-generator)
- [BytesAgain homepage](https://bytesagain.com)
- [BytesAgain feedback](https://bytesagain.com/feedback)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [stdout text containing code, JSON, Markdown, shell snippets, and implementation guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated output is scaffolding that should be reviewed and hardened before production use.]

## Skill Version(s):

2.0.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
