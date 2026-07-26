## Description: <br>
Git Log Tracker installs Git post-commit hooks and provides a SQLite-backed CLI for recording, querying, listing, summarizing, deleting, and updating local commit metadata across repositories. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[leeshunee](https://clawhub.ai/user/leeshunee) <br>

### License/Terms of Use: <br>
GNU General Public License v3.0 <br>


## Use Case: <br>
Developers and engineers use this skill to configure Git commit logging, manage repository hooks, and query a local commit index across one or more repositories. It is useful when users need to find which repository contains a commit, inspect recent commit history, or summarize commit activity. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Persistent local commit logging can collect repository paths, authors, branches, subjects, and hashes in ~/.commit-logs/index.db. <br>
Mitigation: Install hooks only for intended repositories, treat ~/.commit-logs/index.db as sensitive local data, and back it up before cleanup or reset operations. <br>
Risk: Global mode changes Git's global init.templateDir so future repositories can inherit the post-commit hook. <br>
Mitigation: Avoid global mode unless future repositories should inherit the hook, and disable it with git-log-tracker global --off when it is no longer needed. <br>
Risk: Reinstall and upgrade cleanup commands can delete the local data directory or database. <br>
Mitigation: Back up ~/.commit-logs/index.db and config.toml before running reinstall, upgrade cleanup, or reset commands. <br>
Risk: The package includes AGENTS.md and CLAUDE.md policy files that an agent may load in addition to the Git logging workflow. <br>
Mitigation: Review or remove AGENTS.md and CLAUDE.md if those agent-behavior policies are not desired in the target environment. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/leeshunee/skills/git-log-tracker) <br>
- [README](README.md) <br>
- [Onboarding guide](references/ONBOARDING.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and CLI output examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Guides local CLI setup, Git hook management, SQLite-backed commit queries, and configuration changes.] <br>

## Skill Version(s): <br>
0.7.0 (source: SKILL.md frontmatter, pyproject.toml, and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
