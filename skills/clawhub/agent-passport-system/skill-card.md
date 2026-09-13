## Description:

Agent Passport provides identity, delegation, enforcement, commerce, reputation, and audit-trail workflows for AI agents through SDK, CLI, and MCP interfaces.

This skill is ready for commercial/non-commercial use.

## Publisher:

[aeoess](https://clawhub.ai/user/aeoess)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill to create and verify agent passports, delegate scoped authority, record signed work receipts, enforce commerce and policy checks, and generate audit evidence.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup can run mutable npm or MCP code.

Mitigation: Use pinned package versions, inspect packages before running npx, and run setup in a least-privilege environment.

Risk: The skill can create local agent key material and configuration.

Mitigation: Protect .passport/agent.json like a private key, keep it out of version control, and limit file access to trusted users.

Risk: MCP setup can change local Claude Desktop or Cursor configuration.

Mitigation: Review the exact configuration changes before enabling the MCP server.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/aeoess/skills/agent-passport-system)
- [npm SDK package](https://www.npmjs.com/package/agent-passport-system)
- [npm MCP package](https://www.npmjs.com/package/agent-passport-system-mcp)
- [PyPI package](https://pypi.org/project/agent-passport-system/)
- [crates.io package](https://crates.io/crates/agent-passport-system)
- [Go package documentation](https://pkg.go.dev/github.com/aeoess/agent-passport-go)
- [Project documentation](https://agent-passport.org/llms-full.txt)
- [Project paper](https://doi.org/10.5281/zenodo.18749779)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands, code examples, and configuration instructions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce local identity files, signed delegations, signed receipts, Merkle proofs, and MCP or editor setup guidance.]

## Skill Version(s):

6.0.1 (source: server release evidence and artifact metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
