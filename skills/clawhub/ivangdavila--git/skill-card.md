## Description: <br>
Helps agents work with Git repositories, including commits, branches, merges, rebases, conflict resolution, history recovery, remotes, hooks, credentials, and large-repository workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ivangdavila](https://clawhub.ai/user/ivangdavila) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to plan and execute repository work with Git, including everyday commits and branches as well as risky operations such as force-pushes, history rewrites, secret cleanup, and recovery from lost work. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can guide destructive or high-impact Git operations, including force-pushes, history rewrites, hard resets, hook setup, and credential cleanup. <br>
Mitigation: Keep destructive Git actions under explicit review, inspect affected files or commits before execution, and prefer non-destructive recovery or fix-forward workflows when appropriate. <br>
Risk: The skill can remember Git workflow preferences under ~/Clawic/data/git/. <br>
Mitigation: Review or remove that directory if persistent Git preferences are not desired. <br>
Risk: Incorrect Git guidance can overwrite teammates' work, expose credentials, or make repository history harder to recover. <br>
Mitigation: Use Git status, diff, reflog, dry-run, and force-with-lease checks before applying risky changes, and rotate exposed credentials before history cleanup. <br>


## Reference(s): <br>
- [ClawHub Git skill page](https://clawhub.ai/ivangdavila/skills/git) <br>
- [Clawic Git skill page](https://clawic.com/skills/git) <br>
- [Skill overview and core rules](SKILL.md) <br>
- [Setup and preference memory](setup.md) <br>
- [Git memory template](memory-template.md) <br>
- [Collaboration and force-push guidance](collaboration.md) <br>
- [History rewrite and undo guidance](history.md) <br>
- [Recovery playbooks](recovery.md) <br>
- [Committed secrets and unwanted blobs](secrets.md) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, configuration] <br>
**Output Format:** [Markdown guidance with inline Git commands and configuration snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May reference local user preferences stored under ~/Clawic/data/git/ when present.] <br>

## Skill Version(s): <br>
1.0.12 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
