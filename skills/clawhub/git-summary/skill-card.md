## Description: <br>
Get a quick summary of the current Git repository including status, recent commits, branches, and contributors. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zweack](https://clawhub.ai/user/zweack) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and engineers use this skill to inspect the current state of a Git repository and produce a readable summary of status, recent commits, branches, remotes, uncommitted changes, and contributors. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Generated summaries may expose local Git metadata such as remote URLs, commit messages, branch names, contributor names, and changed file paths. <br>
Mitigation: Review summaries before sharing them externally and redact sensitive repository details when needed. <br>
Risk: The skill inspects the current local Git repository using standard read-only Git commands. <br>
Mitigation: Use it only in repositories whose metadata the agent is allowed to inspect. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zweack/skills/git-summary) <br>
- [Publisher profile](https://clawhub.ai/user/zweack) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, guidance] <br>
**Output Format:** [Markdown summary with inline Git command output guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires the git command-line tool and access to a local Git repository.] <br>

## Skill Version(s): <br>
1.0.0 (source: release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
