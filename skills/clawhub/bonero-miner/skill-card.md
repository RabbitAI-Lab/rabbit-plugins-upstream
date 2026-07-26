## Description: <br>
Mine Bonero - private cryptocurrency for AI agents. RandomX CPU mining, Monero-based privacy. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[happybigmtn](https://clawhub.ai/user/happybigmtn) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and external users use this skill to install or build Bonero, create a wallet, start RandomX CPU mining, check daemon and wallet status, and troubleshoot node connectivity. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The default install path runs an unpinned remote shell script. <br>
Mitigation: Download and inspect the installer first, and pin a trusted release or commit before running it. <br>
Risk: Mining starts a detached CPU-consuming daemon that can continue running in the background. <br>
Mitigation: Limit mining threads, monitor CPU load and power use, and stop the daemon when mining is no longer intended. <br>
Risk: Wallet seed phrases are sensitive and cannot be recovered if exposed or lost. <br>
Mitigation: Keep seed phrases out of chats and shared files, and store them only in an approved secure location. <br>


## Reference(s): <br>
- [Bonero repository](https://github.com/happybigmtn/bonero) <br>
- [ClawHub skill page](https://clawhub.ai/happybigmtn/skills/bonero-miner) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Configuration instructions] <br>
**Output Format:** [Markdown with bash commands, JSON-RPC examples, tables, and short operational guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Output may include commands that install software, create wallets, start or stop a detached mining daemon, query local JSON-RPC status, and tune CPU thread usage.] <br>

## Skill Version(s): <br>
2.0.0 (source: frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
