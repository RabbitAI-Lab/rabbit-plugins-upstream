## Description:

Agent Desktop guides agents in using the agent-desktop CLI to observe and automate desktop applications through native OS accessibility trees.

This skill is ready for commercial/non-commercial use.

## Publisher:

[lahfir](https://clawhub.ai/user/lahfir)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill when an agent needs structured guidance for reading desktop UI state, issuing safe GUI actions, managing windows, using the clipboard, handling notifications, taking screenshots, and verifying outcomes through the agent-desktop CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill recommends installing a global agent-desktop package without pinning an exact package version.

Mitigation: Review the package source and pin a trusted agent-desktop version before installation.

Risk: The alternative bun installation path uses trusted lifecycle scripts.

Mitigation: Avoid `bun install -g --trust` unless the package and its install scripts have been reviewed.

Risk: Desktop automation permissions can allow inspection and control of local applications.

Mitigation: Grant Accessibility and Screen Recording only in environments where this level of desktop access is acceptable.

Risk: Screenshots, clipboard reads, traces, and exported session artifacts can contain sensitive user or application data.

Mitigation: Treat generated screenshots, clipboard outputs, trace files, and exported session artifacts as sensitive data and limit retention or sharing.

Risk: Physical or headed desktop actions may focus windows, move input, or mutate the visible desktop state.

Mitigation: Prefer headless semantic actions where possible, use `--headed` only when physical interaction is intended, and verify UI state after each action.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/lahfir/skills/agent-desktop)
- [Observation commands](references/commands-observation.md)
- [Interaction commands](references/commands-interaction.md)
- [System commands](references/commands-system.md)
- [Common automation workflows](references/workflows.md)
- [macOS platform notes](references/macos.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guidance expects the calling agent to execute commands, inspect JSON envelopes, and verify desktop state after actions.]

## Skill Version(s):

0.1.28 (source: server release metadata; artifact frontmatter reports 0.4.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
