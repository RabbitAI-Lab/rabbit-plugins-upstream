## Description:

Semantic code navigation with `cx` CLI for understanding code structure, finding symbol definitions, tracing references before refactoring, and exploring large codebases efficiently.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wei840222](https://clawhub.ai/user/wei840222)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to navigate supported codebases semantically before reading files, editing named symbols, or refactoring. It guides agents toward `cx overview`, `cx symbols`, `cx definition`, and `cx references` commands for scoped code understanding.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installer commands can execute code locally, especially the disclosed curl-to-shell installation path.

Mitigation: Prefer the brew or cargo installation commands when available; if using curl-to-shell, review the script source before execution.

Risk: cx creates local cache and index data for projects it inspects.

Mitigation: Use an appropriate cache location when needed and clean the cache only when comfortable rebuilding local state.

## Reference(s):

- [cx ClawHub Skill Page](https://clawhub.ai/wei840222/skills/cx-cli)
- [cx Command Reference](artifact/references/command-reference.md)
- [cx Decision Tree](artifact/references/decision-tree.md)
- [cx Output Examples](artifact/references/output-examples.md)
- [cx Setup and Recovery](artifact/references/setup-and-recovery.md)
- [Complete Usage Inventory](artifact/references/usage-inventory.md)
- [cx install script source](https://raw.githubusercontent.com/ind-igo/cx/master/install.sh)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration]

**Output Format:** [Markdown with inline shell commands and concise procedural guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only navigation guidance; directs agents to use normal read and edit tools for full-file context or code changes.]

## Skill Version(s):

1.1.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
