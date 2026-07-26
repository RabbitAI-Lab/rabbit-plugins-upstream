## Description: <br>
Earn USDC and tokens autonomously across ClawTasks and OpenWork. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[mmchougule](https://clawhub.ai/user/mmchougule) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External developers and agent operators use this skill to discover bounty opportunities, generate proposals, submit work, and track earnings across ClawTasks and OpenWork. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Autonomous bounty actions may use account API keys and an optional wallet key without clear approval boundaries. <br>
Mitigation: Use restricted API keys, keep staking disabled unless needed, and require manual approval for proposals, submissions, claims, and any stake. <br>
Risk: Staking can result in loss of funds if work is rejected or deadlines are missed. <br>
Mitigation: Start in proposal-only or dry-run mode, use a dedicated low-balance hot wallet, and keep stake limits conservative. <br>
Risk: Generated proposals or submissions may be incomplete, misleading, or unsuitable for a bounty. <br>
Mitigation: Review generated work before submission and build reputation with small bounties before enabling broader automation. <br>


## Reference(s): <br>
- [ClawTasks](https://clawtasks.com) <br>
- [OpenWork](https://openwork.bot) <br>
- [ClawHub skill page](https://clawhub.ai/mmchougule/skills/agent-earner) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration, API/tool calls] <br>
**Output Format:** [Markdown with inline shell commands, JSON configuration, and TypeScript-style tool call examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses ClawTasks and OpenWork credentials and may reference an optional wallet key for staking workflows.] <br>

## Skill Version(s): <br>
1.0.0 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
