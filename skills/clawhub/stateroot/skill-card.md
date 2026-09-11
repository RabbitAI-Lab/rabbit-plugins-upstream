## Description:

Install and set up StateRoot, the continuity layer for AI coding agents that carries personality, plans, tools and skills, memories, learnings, and project context across supported harnesses.

This skill is ready for commercial/non-commercial use.

## Publisher:

[usama04](https://clawhub.ai/user/usama04)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this bootstrap skill to install the StateRoot CLI, run machine-level setup, and optionally initialize a project for cross-agent continuity across supported coding harnesses.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Remote installer commands can execute code from GitHub release assets.

Mitigation: Prefer an inspected, version-pinned, and signature-verified installer or MSI; ask the user before piping a remote script into a shell.

Risk: Setup can persist AI-agent hooks and a built-in skill across future sessions.

Mitigation: Use dry-run or interactive setup first, confirm exactly which harnesses will be modified, and proceed only when the user accepts persistent hooks.

Risk: The manifest understates durable local changes by claiming no persistent state.

Mitigation: Review the disclosure and security evidence before deployment, including local config, identity files, harness hooks, and optional project state.

## Reference(s):

- [StateRoot homepage](https://stateroot.dev)
- [StateRoot installation docs](https://stateroot.dev/docs/getting-started/installation)
- [StateRoot setup docs](https://stateroot.dev/docs/getting-started/setup)
- [StateRoot privacy guide](https://stateroot.dev/docs/guides/privacy)
- [StateRoot FAQ](https://stateroot.dev/docs/reference/faq)
- [StateRoot source repository](https://github.com/CognizTech/stateroot)
- [StateRoot releases](https://github.com/CognizTech/stateroot/releases)
- [Install reference](references/install.md)
- [Disclosure reference](references/disclosure.md)
- [Bootstrap failures reference](references/failures.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with shell command blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May ask for confirmation before remote installer commands and may report local CLI status from scripts/check.sh.]

## Skill Version(s):

1.1.2 (source: server release metadata and skill.manifest.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
