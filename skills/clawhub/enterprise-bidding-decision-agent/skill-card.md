## Description:

Enterprise bidding decision assistant that analyzes a specific tender or procurement opportunity and produces a decision report covering whether to bid, pricing, likely competitors, win probability, buyer patterns, and disqualification risks using Zhiliaobiaoxun tender data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhiliaobiaoxun](https://clawhub.ai/user/zhiliaobiaoxun)

### License/Terms of Use:

MIT-0

## Use Case:

External users and business teams use this agent to evaluate concrete tender opportunities, estimate competition and pricing, and decide whether to bid. The skill is designed for Chinese bidding/procurement analysis backed by Zhiliaobiaoxun historical tender and award data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The provider receives bid and project queries, and may receive registration device features when no API key is configured.

Mitigation: Use a preconfigured ZLBX_API_KEY when possible, share only project information needed for the analysis, and proceed with automatic registration only after informed consent.

Risk: Generated reports and API-returned signed sk links may expose confidential tender or business context.

Mitigation: Treat HTML reports and signed links as confidential, restrict sharing, and delete reports from ~/zlbx-bid-decision-files/ when no longer needed.

Risk: The skill handles credentials, paid API calls, and persistent local configuration.

Mitigation: Review ~/.zlbx/config.json, keep API keys out of chat, disclose expected credit use before full analysis, and remove stored credentials when the skill is no longer trusted.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zhiliaobiaoxun/skills/enterprise-bidding-decision-agent)
- [Publisher profile](https://clawhub.ai/user/zhiliaobiaoxun)
- [API quick reference](references/api-quick.md)
- [Workflow guide](references/workflow.md)
- [Report template](references/report-template.md)
- [Auto-registration flow](references/auto-register.md)
- [Zhiliaobiaoxun API base](https://mcp-server.zhiliaobiaoxun.com/api_v2/{tool_name})
- [Zhiliaobiaoxun AI platform](https://ai.zhiliaobiaoxun.com/?ch=s65)
- [Zhiliaobiaoxun business platform](https://agent.zhiliaobiaoxun.com)
- [Bailian bid-writing product](https://biaoshu.zhiliaobiaoxun.com/)

## Skill Output:

**Output Type(s):** [text, markdown, files, code, shell commands, configuration, guidance]

**Output Format:** [Markdown decision report in chat, with an optional self-contained HTML report file.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Full reports estimate and disclose paid API-call credit use, preserve API-returned signed links, and provide an absolute path for generated HTML reports.]

## Skill Version(s):

1.0.2 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
