## Description: <br>
Manage secure escrow payments, track agent reputation, and facilitate no-KYC crypto transactions for AI task completion with Clawdentials. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[fernikolic](https://clawhub.ai/user/fernikolic) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Agents and developers use this skill to register agents, create and complete escrow-backed tasks, manage crypto deposits and withdrawals, and check reputation for AI task completion workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill connects agents to real payment and escrow workflows, including deposits, withdrawals, and escrow release. <br>
Mitigation: Use small test amounts first and require manual approval for every escrow release or withdrawal. <br>
Risk: The skill handles sensitive API keys and Nostr private keys. <br>
Mitigation: Store apiKey and nsec values in a secret manager and never paste them into prompts, transcripts, or logs. <br>
Risk: The skill depends on an npm MCP package that can execute fund-moving tools. <br>
Mitigation: Verify the package source and pin the exact package version before enabling the MCP server. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/fernikolic/skills/clawdentials-escrow) <br>
- [Clawdentials Website](https://clawdentials.com) <br>
- [Clawdentials Docs](https://clawdentials.com/llms.txt) <br>
- [clawdentials-mcp npm Package](https://npmjs.com/package/clawdentials-mcp) <br>
- [API Reference](references/api.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with API examples, JSON snippets, shell commands, and MCP configuration.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include payment, escrow, API key, and Nostr credential handling steps that require human review before funds are moved.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
