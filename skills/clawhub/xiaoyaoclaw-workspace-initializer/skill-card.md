## Description:

Initializes and standardizes OpenClaw workspaces by proposing reviewed directory creation, WORKSPACE.md rules, multi-agent configuration safety guidance, and a memory log.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dtsola](https://clawhub.ai/user/dtsola)

### License/Terms of Use:

MIT

## Use Case:

Developers and agent operators use this skill to initialize or repair a confirmed OpenClaw workspace root with a standard directory layout, persistent workspace rules, and safer multi-agent configuration practices.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Workspace governance files such as WORKSPACE.md and AGENTS.md can affect future agent behavior.

Mitigation: Review the proposed WORKSPACE.md content and exact AGENTS.md diff before approving any write.

Risk: Workspace initialization creates files and directories in the selected workspace.

Mitigation: Run the skill only in a workspace root the user has confirmed, create only missing items, and leave existing files untouched unless the user approves a shown diff.

Risk: Configuration guidance for shared multi-agent setups can change how future config edits are performed.

Mitigation: Use the proposed config.patch guidance only after confirming it matches the workspace's shared configuration model.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dtsola/skills/xiaoyaoclaw-workspace-initializer)
- [Project documentation](https://github.com/dtsola/xiaoyaoclaw-workspace-initializer)
- [XiaoyaoClaw guide](https://www.yuque.com/dtsola/igp1aa/adcicbai2zlem0bz)
- [WORKSPACE.md template](templates/WORKSPACE.md)
- [AGENTS config safety template](templates/AGENTS-config-safety.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with proposed diffs, shell commands, workspace templates, and concise status messages]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces user-reviewed workspace file changes and guidance; it does not install persistent services or overwrite existing governance files without approval.]

## Skill Version(s):

1.0.6 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
