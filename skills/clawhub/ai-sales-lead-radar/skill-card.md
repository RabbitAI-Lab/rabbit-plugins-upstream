## Description:

Helps government and enterprise sales teams find and prioritize sales leads from proposed projects, procurement-intent notices, and expiring contracts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dragonzu](https://clawhub.ai/user/dragonzu)

### License/Terms of Use:

MIT-0

## Use Case:

Sales, business-development, and channel teams use this skill to scan ZLBX bid and project data for early government and enterprise opportunities, rank leads by value and urgency, and produce a concise opportunity list with next actions. It can also generate a local HTML report for sharing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill makes external API calls and may transmit query terms about the user's target market.

Mitigation: Review the domains and data-sharing behavior before use, and avoid submitting confidential sales strategy details as search terms.

Risk: If no API key is configured, the skill can auto-register after user consent using a MAC-derived device hash and store credentials in the user's home directory.

Mitigation: Prefer a preconfigured API key when available, require explicit consent before auto-registration, and treat local ZLBX configuration files as sensitive.

Risk: Generated HTML reports and returned opportunity links may include sensitive signed URLs.

Mitigation: Share reports and signed links only with intended recipients and avoid publishing them broadly.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dragonzu/skills/ai-sales-lead-radar)
- [Publisher profile](https://clawhub.ai/user/dragonzu)
- [Workflow reference](references/workflow.md)
- [API quick reference](references/api-quick.md)
- [Report template](references/report-template.md)
- [Auto-registration workflow](references/auto-register.md)
- [ZLBX API base](https://mcp-server.zhiliaobiaoxun.com/api_v2/)
- [ZLBX skill documentation](https://ai.zhiliaobiaoxun.com/docs/skill)
- [ZLBX opportunity platform](https://agent.zhiliaobiaoxun.com)

## Skill Output:

**Output Type(s):** [text, markdown, API calls, code, shell commands, configuration, guidance]

**Output Format:** [Markdown lead lists with optional local HTML report files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses ZLBX API data and requires ZLBX_API_KEY or user-approved auto-registration; generated reports may contain signed links.]

## Skill Version(s):

1.0.6 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
