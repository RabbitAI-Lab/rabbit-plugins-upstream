## Description: <br>
Automates synchronization, packaging, release creation, and marketplace publishing for skills and agents across Gitee, GitHub, ClawHub, SkillHub, and PyPI, with file filtering and sensitive-data sanitization. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ldxs001](https://clawhub.ai/user/ldxs001) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and release maintainers use git-sync to package, sanitize, version-check, and publish skills or agents across supported repositories and marketplaces. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Automated publishing can push code or packages to remote repositories and marketplaces. <br>
Mitigation: Review the target repository and release intent before execution, and use --skip-market unless marketplace publishing is explicitly intended. <br>
Risk: Git credential handling can persistently weaken credential settings or expose overly broad tokens. <br>
Mitigation: Use scoped tokens, avoid embedded tokens in git remotes, and check global Git credential settings after running the skill. <br>
Risk: The skill handles files that may contain sensitive information before publishing. <br>
Mitigation: Keep the mandatory sensitive-data scan enabled and review sanitization results before publishing public artifacts. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ldxs001/skills/git-sync) <br>
- [Guide](references/guide.md) <br>
- [Command reference](references/reference.md) <br>
- [Permissions and tests](references/permissions.md) <br>
- [Changelog](references/changelog.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown and terminal text with shell commands, JSON snippets, and generated files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May create package archives, release tags, repository updates, and marketplace publication commands depending on selected options.] <br>

## Skill Version(s): <br>
2.32.0 (source: frontmatter, _meta.json, changelog, server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
