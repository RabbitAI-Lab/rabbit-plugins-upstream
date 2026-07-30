## Description: <br>
git-sync is a cross-platform publishing automation skill for syncing skills and agents to Gitee, GitHub, ClawHub, SkillHub, and PyPI, with release creation plus LLM-assisted file filtering and redaction. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ldxs001](https://clawhub.ai/user/ldxs001) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and maintainers use git-sync to package, synchronize, publish, and create releases for skill and agent projects across supported repositories and marketplaces while checking versions and redacting sensitive data. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can copy local skill or agent projects, alter a work repository, push to GitHub or Gitee, publish to marketplaces or PyPI, and use stored credentials. <br>
Mitigation: Run it only for intentional publishing workflows, review the target project and destination before execution, and use least-privilege credentials scoped to the required repositories and services. <br>
Risk: The security evidence flags broad credential access and persistent Git credential helper changes. <br>
Mitigation: Review or patch credential handling before installation, avoid long-lived shared credentials, and test with a disposable account or repository before using production publishing tokens. <br>
Risk: The security evidence highlights shell-based ClawHub publishing and limited explicit confirmation before public publishing. <br>
Mitigation: Review project names and publish commands before use, require a manual approval step for public releases, and prefer non-publishing modes until the release contents are verified. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ldxs001/skills/git-sync) <br>
- [Command reference](references/reference.md) <br>
- [Changelog](references/changelog.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Files] <br>
**Output Format:** [Markdown status text with inline shell commands and generated repository or package files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May produce repository changes, release tags, package archives, README updates, and marketplace or PyPI publishing actions depending on selected flags.] <br>

## Skill Version(s): <br>
2.33.0 (source: server release evidence, SKILL.md frontmatter, _meta.json, changelog) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
