## Description:

git-sync is a cross-platform release automation skill for synchronizing and publishing skills and agents to Gitee, GitHub, ClawHub, SkillHub, PyPI, and release channels with file filtering and sensitive-data sanitization.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ldxs001](https://clawhub.ai/user/ldxs001)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and release maintainers use git-sync to synchronize, package, and publish skills or agents across repository, marketplace, package, and release workflows. It supports version checks, repository updates, packaging, LLM-assisted file filtering, and sensitive-data sanitization decisions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can publish code, push repositories, create releases, upload packages, and read local publishing credentials.

Mitigation: Run it only on trusted projects with reviewed configuration, and use --skip-market or pack-only modes when marketplace or package publishing is not intended.

Risk: The security evidence flags Git credential handling changes and shell command execution built from project metadata.

Mitigation: Avoid untrusted skill metadata, review repository and credential settings before execution, and confirm that command construction and credential-helper behavior have been fixed before broad use.

Risk: The workflow can pause for file-filtering or sensitive-data sanitization decisions, and incorrect decisions can publish unwanted files or retained secrets.

Mitigation: Review generated decision JSON carefully and sanitize critical secrets before rerunning the release command.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/ldxs001/skills/git-sync)
- [Publisher profile](https://clawhub.ai/user/ldxs001)
- [Usage guide](references/guide.md)
- [Command reference](references/reference.md)
- [Permissions and test report](references/permissions.md)
- [Changelog](references/changelog.md)
- [Blueprint rules](references/blueprint_rules.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON decision snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May require follow-up decision JSON for file filtering or sensitive-data sanitization before rerunning the same release command.]

## Skill Version(s):

2.45.6 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
