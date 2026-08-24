## Description:

Provides Go package and module documentation, API references, symbols, examples, versions, importers, licenses, and known vulnerability lookups through the godig CLI or MCP server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[samber](https://clawhub.ai/user/samber)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to inspect published Go modules and packages before writing or reviewing code. It is suited for looking up documentation, symbols, examples, versions, importers, licenses, and known vulnerabilities from the Go package ecosystem.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill declares broader local editing, git, and agent permissions than its documented read-only package lookup workflow requires.

Mitigation: Review the requested permissions before installation and prefer using the read-only godig commands or MCP operations for documentation, version, importer, license, and vulnerability lookups.

Risk: Some godig commands can return large documentation, examples, README, or license text that may consume substantial context.

Mitigation: Start with overview or symbol-specific commands, pass Markdown output, and scope large commands with package, symbol, version, filter, or limit options.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/samber/skills/golang-pkg-go-dev)
- [Publisher Profile](https://clawhub.ai/user/samber)
- [Homepage](https://github.com/samber/cc-skills-golang)
- [pkg.go.dev](https://pkg.go.dev)
- [Hosted godig MCP Server](https://godig.samber.dev/mcp)
- [Sample Output](references/sample-output.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and command output summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only Go ecosystem lookups; large documentation, examples, README, and license outputs should be scoped when possible.]

## Skill Version(s):

1.4.0 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
