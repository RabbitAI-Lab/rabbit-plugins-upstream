## Description:

Provides gRPC usage guidelines, protobuf organization, and production-ready patterns for Golang microservices.

This skill is ready for commercial/non-commercial use.

## Publisher:

[samber](https://clawhub.ai/user/samber)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to implement, review, test, and debug Go gRPC services and clients with production-oriented patterns for protobufs, status codes, deadlines, interceptors, TLS/mTLS, health checks, graceful shutdown, and streaming RPCs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can guide an agent to edit Go files and run Go, protobuf, linting, and code-navigation tooling in a development workspace.

Mitigation: Review generated code, proposed file edits, dependency installation commands, and tool output before merging or deploying changes.

Risk: Incorrect gRPC guidance could affect authentication, TLS, deadlines, retries, or service operability.

Mitigation: Validate security-sensitive and production configuration changes against project standards and test expected gRPC status codes, deadlines, and shutdown behavior.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/samber/skills/golang-grpc)
- [Publisher profile](https://clawhub.ai/user/samber)
- [Project homepage](https://github.com/samber/cc-skills-golang)
- [Protobuf & Code Generation Reference](references/protoc-reference.md)
- [gRPC Testing Reference](references/testing.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration]

**Output Format:** [Markdown with inline Go, protobuf, YAML, JSON, and shell examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose edits to Go source files and commands for Go, protobuf, linting, gopls, and related documentation lookup tools.]

## Skill Version(s):

1.2.0 (source: server evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
