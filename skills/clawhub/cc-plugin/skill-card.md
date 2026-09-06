## Description:

Claude Code plugin lifecycle management for creating, installing, updating, cleaning, clustering, reflecting, and troubleshooting plugins.

This skill is ready for commercial/non-commercial use.

## Publisher:

[drumrobot](https://clawhub.ai/user/drumrobot)

### License/Terms of Use:

MIT

## Use Case:

Developers and engineers use this skill to manage Claude Code plugin lifecycles, including plugin authoring, marketplace operations, local development reflection, cache cleanup, HUD configuration, clustering decisions, and troubleshooting installation or load failures.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Plugin lifecycle workflows can mutate Claude Code plugin state under ~/.claude, including marketplace clones, cache directories, and settings.

Mitigation: Use dry-run modes where available, inspect marketplace and plugin diffs before applying changes, and keep backups for settings changes.

Risk: Development reflection can copy or delete files in a marketplace clone, and may be destructive if the clone is the same repository or worktree as the source.

Mitigation: Resolve the source, clone, and common git directory before running dev-reflect.sh; do not run it when they refer to the same repository or worktree.

Risk: Marketplace and update guidance may pull or operate on untrusted repositories.

Mitigation: Avoid untrusted marketplace URLs and review repository provenance, manifests, scripts, and plugin diffs before enabling or rebuilding plugins.

Risk: Cache cleanup removes old plugin cache versions and temporary git directories.

Mitigation: Run cache cleanup with --dry-run first and verify the target paths before allowing deletion.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/drumrobot/skills/cc-plugin)

## Skill Output:

**Output Type(s):** [guidance, markdown, code, shell commands, configuration]

**Output Format:** [Markdown with inline JSON and bash code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes procedural routing guidance and optional shell helper usage; review commands before execution.]

## Skill Version(s):

0.7.0 (source: server release metadata and CHANGELOG, released 2026-09-06; SKILL.md frontmatter reports 0.1.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
