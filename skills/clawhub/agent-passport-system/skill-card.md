## Description:

Helps agents establish cryptographic identities, delegate scoped authority, enforce constraints, and record auditable work and contributions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[aeoess](https://clawhub.ai/user/aeoess)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill to create agent passports, delegate limited authority, check constraints, and produce signed receipts and contribution proofs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Unpinned remote packages can change between installs.

Mitigation: Install only when the publisher and package source are trusted; prefer pinned versions or a lockfile-managed local install.

Risk: MCP setup can persistently change local agent-tool configuration.

Mitigation: Review proposed Claude Desktop or Cursor configuration changes before accepting them.

Risk: Generated passport files contain sensitive key material.

Mitigation: Treat passport files like private keys and restrict access to them.

## Reference(s):

- [Agent Passport on ClawHub](https://clawhub.ai/aeoess/skills/agent-passport-system)
- [Agent Passport npm package](https://www.npmjs.com/package/agent-passport-system)
- [Project homepage (artifact metadata)](https://github.com/aeoess/agent-passport-system)
- [Agent Passport documentation](https://agent-passport.org/llms-full.txt)
- [Remote MCP endpoint](https://mcp.aeoess.com/sse)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Code, Configuration]

**Output Format:** [Markdown with command and code examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Workflows can create passport files, signed delegations and receipts, and Merkle proofs.]

## Skill Version(s):

6.0.4 (source: ClawHub release evidence and artifact metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
