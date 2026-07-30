## Description: <br>
节点工作工具 guides an agent through single-node setup, wallet configuration, task execution, balance checks, and completion tracking for a personal node rewards workflow. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External developers and individual node operators use this skill to configure one idle machine as a worker node, run single tasks, inspect wallet status, and track completion records. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The node-and-wallet workflow can lead to staking, funding, wallet creation or import, backups, restores, and continuous worker execution without clear confirmation gates for real funds. <br>
Mitigation: Require manual confirmation before wallet creation or import, transfers, staking, backups, restores, and continuous worker execution; verify the underlying project and network independently before providing funds. <br>
Risk: The workflow may require wallet passwords, API keys, and GitHub credentials. <br>
Mitigation: Keep credentials local, do not commit or log them, use strong passwords, and avoid shared or CI environments for wallet operations. <br>


## Reference(s): <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, JSON] <br>
**Output Format:** [Markdown instructions with bash command blocks and JSON response examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May request environment variables, wallet passwords, API credentials, and wallet-related confirmation during execution.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release metadata; artifact front matter says 1.0.1) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
