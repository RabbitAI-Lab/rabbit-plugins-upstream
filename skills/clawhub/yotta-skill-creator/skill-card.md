## Description:

YuanZao generates YottaMeta-style agent skill scaffolds, validates naming and required release files, replaces template placeholders, and runs a structure self-check.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yottameta](https://clawhub.ai/user/yottameta)

### License/Terms of Use:

MIT

## Use Case:

Developers and agent-skill maintainers use this skill to create new yotta-* skill directories, generate optional CLI and test skeletons, and catch structural issues before handoff to publishing checks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can write generated content into agent skill directories.

Mitigation: Run it in a controlled workspace, choose the output directory deliberately, and review generated files before enabling or publishing them.

Risk: Untrusted or multiline --desc input can become persistent generated skill instructions.

Mitigation: Use trusted description text, review generated SKILL.md content, and avoid untrusted multiline input until the template escaping issue is fixed.

Risk: The generated scaffold is a starting point, not completed skill logic.

Mitigation: Manually implement and review the skill body and any scripts, then run the intended publication checks before release.

## Reference(s):

- [CLI Reference](references/cli-reference.md)
- [Scaffold Structure](references/scaffold-structure.md)
- [YuanZao Tutorial](references/tutorial.md)
- [ClawHub Skill Page](https://clawhub.ai/yottameta/skills/yotta-skill-creator)
- [npm Package](https://www.npmjs.com/package/@yottameta/yotta-skill-creator)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with bash commands and generated skill files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated files are written to a new target directory; validation failures return nonzero exit codes and no overwrite is performed.]

## Skill Version(s):

0.1.2 (source: SKILL.md frontmatter, package.json, CHANGELOG, ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
