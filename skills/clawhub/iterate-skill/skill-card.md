## Description: <br>
Fully automated multi-round code iteration with configurable N-dimension parallel review, onboarding/personalization, and a cross-assistant installer. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jingzhao-l](https://clawhub.ai/user/jingzhao-l) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and engineering teams use Iterate to run structured, multi-round code quality, security, performance, architecture, and test review loops over a repository. The skill can prepare onboarding context, propose or apply fixes, run configured validation, and coordinate user-approved architectural changes. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The workflow can automatically edit files, run configured commands, merge changes, and push to the target branch. <br>
Mitigation: Use protected branches or PR review for important repositories, inspect validation.commands and command_whitelist before execution, and consider setting git.push_per_round to false. <br>
Risk: Rollback behavior can use destructive git reset commands on iteration branches. <br>
Mitigation: Run the skill only in clean worktrees or isolated iteration branches, keep backups for important work, and confirm branch protections prevent destructive operations on main or master. <br>
Risk: Update and uninstall flows can reduce confirmation prompts when --yes is used. <br>
Mitigation: Avoid --yes for updates or uninstall operations unless the source and target are already verified. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/jingzhao-l/skills/iterate-skill) <br>
- [skills.sh package page](https://skills.sh/jingzhao-l/iterate-skill) <br>
- [Agent Skills standard](https://agentskills.io/) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands, generated or edited project files, and configuration snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May run configured validation commands and produce repository changes through the host agent workflow.] <br>

## Skill Version(s): <br>
2.0.1 (source: SKILL.md frontmatter, pyproject.toml, CHANGELOG, server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
