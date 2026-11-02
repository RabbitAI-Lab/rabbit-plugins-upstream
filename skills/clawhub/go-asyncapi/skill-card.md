## Description:

Go library that loads AsyncAPI 3 documents.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Go developers can load and inspect AsyncAPI 3 specifications in YAML or JSON. Use it to read servers, channels, operations, messages, and schemas, or as a base for Go generators and tooling.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A specification's local references can cause additional files to be read.

Mitigation: Use trusted specifications and review the referenced local files before loading them.

Risk: The security review covers the skill instructions, not the full external Go library.

Mitigation: Review and pin the Go dependency version before adding it to a project.

## Reference(s):

- [go-asyncapi setup and reference](references/setup.md)
- [go-asyncapi repository](https://github.com/psyb0t/go-asyncapi)
- [gen-asyncapi](https://github.com/psyb0t/gen-asyncapi)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with Go code examples and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Instructions and examples for loading and inspecting AsyncAPI 3 documents in Go.]

## Skill Version(s):

0.1.2 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
