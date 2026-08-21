## Description:

Entry point for Rotifer Protocol onboarding, Gene scaffolding, diagnostics, registry search, and fidelity upgrades, scoped only to Rotifer Genes and the Rotifer CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xiaoba-dev](https://clawhub.ai/user/xiaoba-dev)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill when working with Rotifer to choose the right workflow, run Rotifer CLI onboarding, scaffold Genes, diagnose compile or F(g) issues, search the Gene registry, and plan fidelity upgrades.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can guide npm installs, MCP setup, project file creation, Rotifer service calls, and public Gene publishing.

Mitigation: Review proposed commands before execution, especially installs, MCP configuration changes, publish actions, Arena submissions, and Web Studio generation.

Risk: Service-backed scaffold and scan paths can transmit user prompts, generated source, or phenotype metadata to Rotifer services.

Mitigation: Use the local CLI path when the prompt or generated Gene source contains information the user would not share with Rotifer services.

Risk: Generated or migrated Gene code can change security posture and fitness behavior.

Mitigation: Run Rotifer tests, compilation, and V(g) scanning after scaffold or fidelity upgrade work before publishing or submitting to Arena.

## Reference(s):

- [Rotifer Protocol](https://rotifer.dev)
- [Rotifer Documentation](https://rotifer.dev/docs)
- [Rotifer Protocol Specification](https://github.com/rotifer-protocol/rotifer-spec)
- [Rotifer Web Studio](https://rotifer.ai/studio/)
- [Rotifer Guide on ClawHub](https://clawhub.ai/xiaoba-dev/skills/rotifer-guide)

## Skill Output:

**Output Type(s):** [guidance, markdown, shell commands, configuration, code]

**Output Format:** [Markdown with inline shell commands, JSON configuration snippets, and workflow guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands that install, publish, overwrite, or contact Rotifer services should be proposed for user approval before execution.]

## Skill Version(s):

1.2.1 (source: server-resolved release metadata and clawhub.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
