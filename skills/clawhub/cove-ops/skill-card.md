## Description: <br>
Cove platform operations: channel files, cove.md, webhooks, channels, messages, members, reactions, roles, and permissions. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[kagura-agent](https://clawhub.ai/user/kagura-agent) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this skill to operate Cove channels, channel files, cove.md, webhooks, messages, members, reactions, roles, and permissions through documented API calls and configuration patterns. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Bot credentials and webhook URLs can grant Cove access if exposed. <br>
Mitigation: Keep bot tokens and webhook URLs out of chat, logs, cove.md, and committed files; rotate them if exposure is suspected. <br>
Risk: The documented commands can modify or delete channels, files, messages, roles, and permissions. <br>
Mitigation: Review destructive commands before execution and verify target IDs, role hierarchy, and required permissions. <br>
Risk: cove.md and channel files are shared mutable context rather than trusted policy. <br>
Mitigation: Treat channel files as shared state and verify operational instructions before relying on them. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/kagura-agent/skills/cove-ops) <br>
- [Cove Staging API Endpoint](https://staging.cove.kagura-agent.com) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration] <br>
**Output Format:** [Markdown with inline bash, JSON, and curl examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Provides operational command patterns and guardrails; the skill itself does not generate files.] <br>

## Skill Version(s): <br>
1.0.0 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
