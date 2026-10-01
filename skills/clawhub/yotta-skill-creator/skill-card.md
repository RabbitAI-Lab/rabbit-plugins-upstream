## Description:

Creates a yotta- skill scaffold with naming checks and a structure self-check, either as a full release package or a self-use skill body.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yottameta](https://clawhub.ai/user/yottameta)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and teams use this skill to create consistently named yotta- skill directories with release files or a smaller self-use scaffold. They must write the generated skill's substantive instructions and code themselves.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installers can persistently copy skills into multiple agent directories without strong confirmation or conflict controls.

Mitigation: Review before installing; prefer explicit --agent or --dir targets over --global and avoid no-argument auto-detection in repositories with multiple agent directories.

Risk: Generated installer files may carry installation behavior into published scaffolds.

Mitigation: Inspect generated installer files before publishing a scaffold.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/yottameta/skills/yotta-skill-creator)
- [Project homepage](https://github.com/YottaMeta/yotta-skill-creator)
- [CLI reference](references/cli-reference.md)
- [Scaffold structure](references/scaffold-structure.md)

## Skill Output:

**Output Type(s):** [Files, Code, Configuration]

**Output Format:** [Generated skill directory with Markdown, scripts, and optional release files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Self-use mode omits release files; generated content needs manual completion and review.]

## Skill Version(s):

0.1.4 (source: skill frontmatter, release metadata, package.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
