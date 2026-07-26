## Description: <br>
Run Kilo CLI via background process for programmatic control. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[nathansebhastian](https://clawhub.ai/user/nathansebhastian) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and engineers use this skill to run Kilo CLI as a supervised background coding agent for implementation work, PR review, issue fixing, and GitHub-assisted workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Background Kilo CLI sessions can execute local commands and use GitHub write access. <br>
Mitigation: Use the narrowest GitHub token possible, run work in isolated temporary clones or worktrees, and supervise background sessions before publishing changes. <br>
Risk: Reviews, pull request comments, and session logs may expose secrets, private prompts, internal paths, or raw logs. <br>
Mitigation: Review all generated comments, pushes, pull requests, and logs before external publication and remove sensitive content. <br>


## Reference(s): <br>
- [GitHub CLI installation](https://github.com/cli/cli#installation) <br>
- [ClawHub skill page](https://clawhub.ai/nathansebhastian/skills/kilocli-coding-agent) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with inline shell commands and workflow instructions] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include commands that start background Kilo CLI or tmux sessions, monitor logs, review pull requests, and post GitHub comments.] <br>

## Skill Version(s): <br>
0.0.9 (source: SKILL.md frontmatter, claw.json, server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
