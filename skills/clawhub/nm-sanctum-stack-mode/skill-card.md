## Description: <br>
Detects shared stack membership and iterates a command across all PRs in base-to-tip order. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[athola](https://clawhub.ai/user/athola) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineering agents use this skill when a PR workflow supports stack mode and needs to resolve, process, and summarize a stack of dependent PRs in base-to-tip order. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The workflow can write a consolidated stack summary comment to a root PR when the agent has repository permissions. <br>
Mitigation: Install only where the agent is allowed to read PR metadata and post PR comments, and review repository permissions before use. <br>
Risk: Readers may treat the skill as read-only because it describes itself as read/orchestration oriented. <br>
Mitigation: Account for the disclosed PR comment write during approval and deployment, while noting that the security evidence says it does not push, rebase, edit branches, or run persistently. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-sanctum-stack-mode) <br>
- [OpenClaw homepage metadata](https://github.com/athola/claude-night-market/tree/master/plugins/sanctum) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, shell commands] <br>
**Output Format:** [Markdown guidance with shell command examples and a PR summary comment template] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May direct a caller to post one consolidated stack summary comment on the root PR.] <br>

## Skill Version(s): <br>
1.9.17 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
