## Description:

Agent Passport helps agents and developers create cryptographic identities, delegate scoped authority, enforce policy boundaries, record signed work receipts, and generate audit or contribution proofs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[aeoess](https://clawhub.ai/user/aeoess)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill to add identity, scoped delegation, revocation, commerce controls, coordination receipts, data attribution, and governance checks to AI agent workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing or running the MCP and SDK packages can change local agent client configuration.

Mitigation: Pin packages to the reviewed version and review any setup changes made to Claude Desktop or Cursor before deployment.

Risk: Local passport key material can authorize agent actions if exposed.

Mitigation: Keep .passport/agent.json private, use restrictive file permissions, and exclude it from source control.

Risk: Remote MCP and API use may send agent identity, intent, or governance data to third-party services.

Mitigation: Use only approved endpoints and review network use against the deployment's data handling requirements.

Risk: A chain of individually valid delegations may compose into an unsafe aggregate target that per-hop narrowing does not detect.

Mitigation: Use composition-hazard checks with trusted external attestors and treat each pass result as scoped to the named profile and bound context.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/aeoess/skills/agent-passport-system)
- [npm SDK package](https://www.npmjs.com/package/agent-passport-system)
- [npm MCP package](https://www.npmjs.com/package/agent-passport-system-mcp)
- [PyPI package](https://pypi.org/project/agent-passport-system/)
- [crates.io package](https://crates.io/crates/agent-passport-system)
- [Go package documentation](https://pkg.go.dev/github.com/aeoess/agent-passport-go)
- [Agent Passport documentation](https://agent-passport.org/llms-full.txt)
- [Agent Passport paper](https://doi.org/10.5281/zenodo.18749779)
- [Remote MCP server](https://mcp.aeoess.com/sse)
- [Intent Network API](https://api.aeoess.com)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands, code snippets, and structured JSON-style outputs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce or modify local passport files, signed receipts, signed delegations, Merkle proofs, and MCP or client configuration.]

## Skill Version(s):

6.0.1 (source: server release metadata and artifact metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
