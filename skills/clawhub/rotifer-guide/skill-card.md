## Description:

Rotifer Guide routes Rotifer-related requests into onboarding, Gene scaffolding, diagnostics, registry search, and fidelity-upgrade workflows for the Rotifer CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xiaoba-dev](https://clawhub.ai/user/xiaoba-dev)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent builders use this skill when working with Rotifer Genes to choose the right workflow for learning Rotifer concepts, creating Genes, diagnosing compile or fitness issues, searching the registry, or planning fidelity upgrades.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Web Studio scaffold and publish workflows can send the user's prompt and generated Gene source to rotifer.ai, and publishing makes the Gene public.

Mitigation: Use the local CLI scaffold path for private work and confirm publish intent before running any command that uploads or publishes a Gene.

Risk: The skill proposes Rotifer CLI commands that may install packages, read project Genes or Agent definitions, and write generated files in the project workspace.

Mitigation: Review proposed commands before execution, keep Rotifer package versions pinned, and commit lockfiles for reproducible installs.

## Reference(s):

- [Rotifer Protocol](https://rotifer.dev)
- [Rotifer Documentation](https://rotifer.dev/docs)
- [Rotifer Protocol Specification](https://github.com/rotifer-protocol/rotifer-spec)
- [Rotifer Playground Repository](https://github.com/rotifer-protocol/rotifer-playground)

## Skill Output:

**Output Type(s):** [guidance, markdown, shell commands, configuration]

**Output Format:** [Markdown guidance with inline shell commands and JSON configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Routes the user to one of five Rotifer workflows and proposes install, scaffold, diagnostic, search, publish, or upgrade commands for review before execution.]

## Skill Version(s):

1.2.2 (source: server release metadata and clawhub.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
