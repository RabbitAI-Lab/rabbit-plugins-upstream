## Description: <br>
内容验证网关免费版 helps individual developers review AI-generated content with blocklist and allowlist checks, content classification, and basic verification logging. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers use this skill to guide an agent through local pre-publication checks for AI-generated content, including rule management, sensitive-pattern classification, filtering, and verification logs. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may persist sensitive input-derived content in local logs or filtered files. <br>
Mitigation: Avoid secrets, personal data, and regulated content unless previews are redacted, output paths are explicit, and retention is reviewed before use. <br>
Risk: Agent execution may create or modify local rule files, filtered files, and verification logs. <br>
Mitigation: Run in a scoped workspace, review proposed commands before execution, and keep backups of important rule files. <br>
Risk: The free/basic checks may miss nuanced policy issues or produce false positives. <br>
Mitigation: Use human review for high-impact or regulated publishing workflows and maintain the blocklist and allowlist for the target domain. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/block-monitor-tool-free) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration] <br>
**Output Format:** [Markdown instructions with Python and shell command snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May write local rule files, filtered output files, and verification logs when the agent executes the suggested commands.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
