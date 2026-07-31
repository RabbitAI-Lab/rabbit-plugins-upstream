## Description: <br>
git-sync automates packaging, version checks, file filtering, sanitization, repository synchronization, marketplace publishing, and release creation for skills and agents across Gitee, GitHub, ClawHub, SkillHub, and PyPI. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ldxs001](https://clawhub.ai/user/ldxs001) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and release maintainers use this skill to synchronize skill or agent projects, compare versions, package releases, publish to supported marketplaces, and create repository releases after review. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can publish remotely and synchronize broad sets of projects, which may push or upload unintended files or changes. <br>
Mitigation: Review file-filter decisions, generated packages, remotes, release targets, and broad or all-project commands before execution. <br>
Risk: The skill can read or reuse local credentials and alter Git credential handling. <br>
Mitigation: Use least-privileged throwaway tokens where possible and review or remove persistent credential-helper changes before use. <br>
Risk: Foreground LLM decision steps are required for filtering and sanitization, and unattended runs can hang or proceed with fallback decisions. <br>
Mitigation: Run the skill only in a foreground agent session and verify allow-list and sanitization decision files before publishing. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ldxs001/skills/git-sync) <br>
- [Usage guide](references/guide.md) <br>
- [Command reference](references/reference.md) <br>
- [Permissions and test summary](references/permissions.md) <br>
- [Blueprint filtering and sanitization rules](references/blueprint_rules.md) <br>
- [Changelog](references/changelog.md) <br>
- [FAQ](references/faq.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, files, guidance] <br>
**Output Format:** [Markdown and terminal status text with inline shell commands, JSON decision files, ZIP packages, repository commits, and release artifacts] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May modify a fixed work repository, create package files, and publish to remote services when invoked with publishing options.] <br>

## Skill Version(s): <br>
2.34.0 (source: frontmatter, _meta.json, changelog, server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
