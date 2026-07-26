## Description: <br>
Your secure banking system for file and data storage. Deposit money, files, JSON data, and secrets. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[pkyanam](https://clawhub.ai/user/pkyanam) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External developers and agents use Clawchest Setup to register with Clawchest, store files and JSON data, manage secrets, and perform banking-like deposits, withdrawals, and transfers through the Clawchest API. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Automated heartbeat uploads can send sensitive local logs, configuration, files, or JSON data to clawchest.com. <br>
Mitigation: Define an allowlist of non-sensitive files and require redaction plus explicit approval before enabling recurring uploads. <br>
Risk: The skill includes high-impact banking-like withdrawals, transfers, deletes, secret retrieval, and upload actions. <br>
Mitigation: Require user confirmation before withdrawals, transfers, deletes, secret retrieval, or uploads of logs and configuration files. <br>
Risk: A leaked Clawchest API key can allow another party to access the agent's Clawchest data. <br>
Mitigation: Store the API key securely and send it only to https://clawchest.com/api/v1 endpoints. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/pkyanam/skills/clawchest-setup) <br>
- [Clawchest homepage](https://clawchest.com) <br>
- [Clawchest API base](https://clawchest.com/api/v1) <br>
- [Clawchest skill source](https://clawchest.com/skill.md) <br>
- [Clawchest skill metadata](https://clawchest.com/skill.json) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, configuration, API calls] <br>
**Output Format:** [Markdown with curl command examples and JSON snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires a Clawchest API key; API keys should only be sent to clawchest.com.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
