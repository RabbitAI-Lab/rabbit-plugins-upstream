## Description: <br>
节点免费版 guides an agent through configuring a Base-network Jinn worker, running a single task test, and checking wallet balances without continuous operation or withdrawal features. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent operators use this skill to set up and test a Jinn worker on the Base network, including environment setup, one single-task worker run, and wallet balance checks. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill asks users to fund and stake real crypto assets while the free version does not provide withdrawal or recovery workflows. <br>
Mitigation: Use a fresh wallet with only funds you can afford to risk, verify the generated wallet address and staking requirements independently, and do not proceed without a separate recovery or withdrawal plan. <br>
Risk: The setup flow depends on sensitive RPC, Gemini, wallet, and operator credentials. <br>
Mitigation: Keep secrets out of tracked files, prefer environment variables or local untracked configuration, and restrict access to any generated wallet or operator files. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/jinn-node-free) <br>
- [Poetry installer](https://install.python-poetry.org) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, configuration] <br>
**Output Format:** [Markdown with inline bash code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Guidance may include commands that create local wallet state and require Base ETH, OLAS, RPC credentials, and Gemini credentials.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence; artifact frontmatter lists 1.0.1) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
