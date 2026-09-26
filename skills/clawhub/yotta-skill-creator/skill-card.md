## Description:

Creates validated yotta- agent-skill scaffolds with release files or a smaller self-use layout, leaving skill content and publishing to the developer.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yottameta](https://clawhub.ai/user/yottameta)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to generate a new yotta- skill directory, check its structure, and optionally scaffold a CLI. They must write the skill's substantive content and handle publication separately.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installers may persist the skill in multiple agent skill folders without confirmation or strong overwrite controls.

Mitigation: Review installer behavior and choose an explicit --agent or --dir target; avoid --global unless all supported agents should be changed, and check existing target directories first.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/yottameta/skills/yotta-skill-creator)
- [Publisher-listed project homepage (not verified import provenance)](https://github.com/YottaMeta/yotta-skill-creator)
- [CLI reference](references/cli-reference.md)
- [Scaffold structure](references/scaffold-structure.md)
- [Tutorial](references/tutorial.md)

## Skill Output:

**Output Type(s):** [Code, Configuration, Markdown, Shell commands]

**Output Format:** [Generated skill directory with Markdown, scripts, and configuration files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Self-use mode omits release artifacts; generated structure is checked before success.]

## Skill Version(s):

0.1.3 (source: ClawHub release, SKILL.md frontmatter, package.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
