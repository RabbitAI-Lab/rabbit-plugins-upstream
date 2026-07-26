## Description: <br>
Agent-native security signal feed by PromptIntel for reporting threats, fetching protection feeds, applying security rules, and maintaining SHIELD.md policy updates. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[fr0gger](https://clawhub.ai/user/fr0gger) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agent operators use MoltThreats to submit defensive threat reports, consume a curated protection feed, and keep local SHIELD.md enforcement policy current with user-approved rules. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can become part of an agent's ongoing security policy by proposing SHIELD.md and related configuration changes. <br>
Mitigation: Review proposed edits to SHIELD.md, SOUL.md, AGENTS.md, and HEARTBEAT.md before enabling them, and only install the skill when ongoing policy integration is desired. <br>
Risk: Heartbeat or feed sync behavior may apply new protections after initial consent. <br>
Mitigation: Disable autonomous sync or require tight approval for feed updates when background policy changes are not acceptable. <br>
Risk: Threat reports and samples may disclose secrets, internal URLs, private infrastructure, or incident details. <br>
Mitigation: Manually redact submissions before sending reports and keep PROMPTINTEL_API_KEY only in an environment variable. <br>


## Reference(s): <br>
- [MoltThreats Homepage](https://promptintel.novahunting.ai/molt) <br>
- [PromptIntel API Base](https://api.promptintel.novahunting.ai/api/v1) <br>
- [SHIELD.md Specification](https://nova-hunting.github.io/shield.md/) <br>
- [Feed Consumption and Enforcement](references/feed-and-enforcement.md) <br>
- [Reporting Guide](references/reporting-guide.md) <br>
- [SHIELD.md Template](references/shield-md-template.md) <br>
- [Integration Example](references/integration-example.md) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration] <br>
**Output Format:** [Markdown guidance with JSON examples, curl commands, and SHIELD.md policy content] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May propose SHIELD.md updates and API-backed threat report or feed workflows that require PROMPTINTEL_API_KEY and user consent.] <br>

## Skill Version(s): <br>
0.6.3 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
