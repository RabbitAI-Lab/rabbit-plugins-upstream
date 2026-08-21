## Description:

Claude Code plugin lifecycle management for creating, installing, updating, cleaning, troubleshooting, and configuring plugin-related workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[drumrobot](https://clawhub.ai/user/drumrobot)

### License/Terms of Use:

MIT

## Use Case:

Developers and engineers use this skill to manage Claude Code plugin authoring, marketplace cloning and updates, cache cleanup, local dev reflection, HUD configuration, plugin troubleshooting, and skill bundle planning.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can guide persistent changes to Claude Code plugin settings, marketplace clones, and runtime cache content.

Mitigation: Use dry-run paths first, review proposed filesystem and settings edits, and back up plugin settings and directories before applying changes.

Risk: Marketplace update and reflection workflows can pull or copy plugin content from local or remote repositories.

Mitigation: Enable only plugins from trusted local repositories or marketplaces, and review repository changes before updating or reflecting them.

Risk: Cache cleanup can remove older plugin cache versions and temporary directories.

Mitigation: Run cache cleanup with --dry-run before deletion and keep a backup when the current runtime state is important.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/drumrobot/skills/cc-plugin)
- [Skill overview](artifact/SKILL.md)
- [Cache cleanup guide](artifact/cache.md)
- [Dev reflect guide](artifact/dev-reflect.md)
- [Troubleshooting guide](artifact/troubleshoot.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline JSON and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose filesystem and settings changes for Claude Code plugin state; users should review commands and use dry-run options where provided.]

## Skill Version(s):

0.6.0 (source: server release metadata and changelog, released 2026-08-20)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
