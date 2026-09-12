## Description:

Desktop automation via native OS accessibility trees using the agent-desktop CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[lahfir](https://clawhub.ai/user/lahfir)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and automation engineers use this skill to guide agents through observing, interacting with, and automating desktop applications with the agent-desktop CLI. It is most relevant for macOS desktop workflows that need accessibility-tree observation, ref-based actions, screenshots, window management, clipboard operations, notifications, and session tracing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill guides agents through desktop automation that can read and control applications after powerful OS permissions are granted.

Mitigation: Grant Accessibility and Screen Recording only when the task requires them, and review planned actions before execution.

Risk: The documented global install commands are unpinned, and the Bun trusted install path can run package install scripts.

Mitigation: Prefer a pinned, reviewed agent-desktop package version and avoid the Bun trusted install path unless the package source and install scripts have been reviewed.

Risk: Session tracing and screenshot artifacts can persist sensitive desktop state.

Mitigation: Use no-trace or session cleanup for sensitive workflows, and treat trace exports and screenshots as sensitive artifacts.

## Reference(s):

- [Observation Commands](references/commands-observation.md)
- [Interaction Commands](references/commands-interaction.md)
- [System Commands](references/commands-system.md)
- [Common Automation Workflows](references/workflows.md)
- [macOS Platform](references/macos.md)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration]

**Output Format:** [Markdown with inline shell commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Agent-desktop command results are expected to be JSON envelopes from the CLI.]

## Skill Version(s):

0.1.28 (source: ClawHub release metadata; artifact frontmatter reports 0.4.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
