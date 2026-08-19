## Description:

Allow any combination of agents, humans, or software to approve MCP tool calls that you flag.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oma3](https://clawhub.ai/user/oma3)

### License/Terms of Use:

MIT-0

## Use Case:

Authorized MPAS signers, maintainers, policy services, and agents use this skill to review pending MPAS Actions and approve or reject exact tool-call proposals according to intent, policy, scope, and risk.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Approving an MPAS Action can authorize a credential-holding adapter to execute the reviewed operation immediately, including high-impact operations.

Mitigation: Install and use this skill only for authorized MPAS maintainers, and verify the exact action, signer identity, scope, policy, and intended effect before approving.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oma3/skills/mpas-maintainer)
- [MPAS project homepage](https://github.com/oma3dao/mpas)

## Skill Output:

**Output Type(s):** [Guidance, API Calls]

**Output Format:** [Markdown guidance with MCP approval operations]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May lead an authorized signer to approve or reject hash-bound MPAS Actions through the configured approval mechanism.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
