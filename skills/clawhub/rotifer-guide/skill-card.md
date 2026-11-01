## Description:

Entry point for Rotifer Protocol — onboarding to Rotifer Genes, scaffolding a Gene from a description, diagnosing a Gene's F(g) or compile failure, searching the Rotifer Gene registry, and upgrading a Gene's fidelity from Wrapped to Native. Invoke explicitly when starting with Rotifer, or when unsure which Rotifer capability to use. Do NOT use for general onboarding, tutorials, troubleshooting, or search — every capability here operates on Rotifer Genes and the Rotifer CLI, and nothing else.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xiaoba-dev](https://clawhub.ai/user/xiaoba-dev)

### License/Terms of Use:

MIT-0

## Use Case:

Developers working with Rotifer use this skill to learn the protocol, scaffold Genes, diagnose failures, search the Gene registry, and plan fidelity upgrades through the Rotifer CLI. It is intended for requests specifically about Rotifer.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The remote scaffold and publish workflows can transmit a user's description or generated Gene source to Rotifer services, and publishing makes the Gene public.

Mitigation: Use the local CLI path for private work, and review the content and destination before approving any remote generation or publication.

Risk: Global npm installation and MCP configuration may affect locations outside the project, despite the guide's brief filesystem assurance.

Mitigation: Prefer a project-local CLI installation and check the scope of MCP configuration before applying it.

## Reference(s):

- [Rotifer Documentation](https://rotifer.dev/docs)
- [Rotifer Protocol](https://rotifer.dev)
- [Rotifer Protocol Specification](https://github.com/rotifer-protocol/rotifer-spec)
- [ClawHub Skill Page](https://clawhub.ai/xiaoba-dev/skills/rotifer-guide)

## Skill Output:

**Output Type(s):** [Guidance, Text, Shell commands, Configuration instructions]

**Output Format:** [Markdown with inline shell commands and configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [None]

## Skill Version(s):

1.2.8 (source: server-resolved release evidence, artifact/clawhub.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
