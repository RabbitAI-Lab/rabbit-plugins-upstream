## Description:

Creates and checks a new yotta- skill scaffold, with optional release files or a smaller self-use layout.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yottameta](https://clawhub.ai/user/yottameta)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and teams use this skill to start a new yotta- skill with consistent naming and structure. They can choose a full publishing scaffold or a smaller private-use scaffold, then write the skill content and scripts themselves.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Automatic installation can persist skill files across multiple agent directories.

Mitigation: Review before installing and select one target explicitly with --agent codex or --dir; avoid -g and no-argument auto-install unless broader placement is intended.

Risk: The Node installer has a symlink-boundary weakness when the skills directory is shared or attacker-writable.

Mitigation: Do not run the Node installer in a shared or attacker-writable skills directory until symlink checks are added.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/yottameta/skills/yotta-skill-creator)
- [Project homepage](https://github.com/YottaMeta/yotta-skill-creator)
- [CLI reference](artifact/references/cli-reference.md)
- [Scaffold structure](artifact/references/scaffold-structure.md)
- [Tutorial](artifact/references/tutorial.md)

## Skill Output:

**Output Type(s):** [Shell commands, Code, Configuration instructions, Guidance]

**Output Format:** [Markdown with inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated scaffolds need manual skill content and script development.]

## Skill Version(s):

0.1.5 (source: frontmatter, package.json, ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
