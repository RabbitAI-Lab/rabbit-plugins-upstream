## Description: <br>
A Chinese-language Git workflow helper for independent developers that provides guidance for branch management, merge conflict handling, Conventional Commits messages, common Git command lookup, and rollback operations. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and independent engineers use this skill to plan Git branches, generate Conventional Commits messages, inspect and resolve common merge conflicts, and get command guidance for everyday repository maintenance. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can direct an agent to run repository-changing or destructive Git commands such as push, pull, reset, branch deletion, merge abort, stash clear/drop, and git clean. <br>
Mitigation: Review every proposed Git command before execution, create a backup branch before risky changes, and avoid using the skill on shared repositories unless the remote impact is acceptable. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/git-workflow-cn-tool-free) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, shell commands, configuration] <br>
**Output Format:** [Markdown with inline shell commands and structured JSON examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May propose repository-changing Git commands that require user review before execution.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
