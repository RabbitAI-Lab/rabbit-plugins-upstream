## Description:

Generates a new yotta- skill scaffold from embedded templates, validates its naming and structure, and supports a self-use mode.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yottameta](https://clawhub.ai/user/yottameta)

### License/Terms of Use:

MIT

## Use Case:

Developers use this skill to create a consistently structured yotta- agent skill, either as a release scaffold or as a smaller private skill. It checks naming and generated structure so they can focus on writing the skill's content and logic.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installation can delete development files through linked folders.

Mitigation: Review installer cleanup and link handling, back up the target directory, and choose an explicit installation target.

Risk: A private scaffold may still contain a publishing workflow.

Mitigation: Review the generated files and remove the publishing workflow before uploading a private scaffold to GitHub.

## Reference(s):

- [CLI reference](references/cli-reference.md)
- [Scaffold structure](references/scaffold-structure.md)
- [Tutorial](references/tutorial.md)
- [ClawHub skill page](https://clawhub.ai/yottameta/skills/yotta-skill-creator)

## Skill Output:

**Output Type(s):** [Files, Code, Configuration, Guidance]

**Output Format:** [A generated skill directory with Markdown, Python, JavaScript, shell, and JSON files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Creates a release scaffold by default; --self-use creates a smaller skill body scaffold.]

## Skill Version(s):

0.1.6 (source: release evidence, SKILL.md frontmatter, package.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
