## Description:

Helps publish skills and agents across Gitee, GitHub, ClawHub, SkillHub, and PyPI, including release creation and assisted file filtering and redaction.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ldxs001](https://clawhub.ai/user/ldxs001)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and maintainers use this skill to synchronize skill or agent repositories, prepare packages and release metadata, and publish to supported code hosts and marketplaces.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Repository and marketplace publishing can push unintended changes or expose project information.

Mitigation: Use --skip-market unless external publication is intended; review generated README content and git diffs before pushing, and avoid casual all-mode runs.

Risk: Untrusted project metadata can trigger command or code injection on the PyPI and ClawHub publishing paths.

Mitigation: Do not run those publishing paths on untrusted projects until the identified injection issues are fixed.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/ldxs001/skills/git-sync)
- [Usage guide](references/guide.md)
- [Command reference](references/reference.md)
- [Permissions](references/permissions.md)
- [Filtering and redaction rules](references/blueprint_rules.md)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Configuration instructions]

**Output Format:** [Markdown with shell commands and status summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can also prepare packages, repository changes, and releases when explicitly run with publishing access.]

## Skill Version(s):

2.47.0 (source: skill frontmatter and ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
