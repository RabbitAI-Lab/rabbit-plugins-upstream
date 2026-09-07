## Description:

Helps agents find early construction and infrastructure opportunities by searching proposed projects, procurement intents, and expiring service contracts, then ranking them by value, maturity, urgency, and match quality.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dragonzu](https://clawhub.ai/user/dragonzu)

### License/Terms of Use:

MIT-0

## Use Case:

External business development, sales, and market intelligence users can give an industry, product, region, or budget threshold and receive a ranked opportunity list for early construction-project pursuit. The skill is intended to support lead discovery and follow-up planning, not to replace independent commercial judgment.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends construction-opportunity search terms and related query filters to a third-party vendor service.

Mitigation: Use the skill only when sharing those search terms with Zhiliaobiaoxun is acceptable for the intended workflow.

Risk: Automatic registration can collect a stable hashed MAC-derived device identifier and store credentials locally.

Mitigation: Prefer a preconfigured ZLBX_API_KEY from a secure environment variable; use automatic registration only after informed user consent.

Risk: Generated reports and returned announcement links can contain sk-style access-bearing links.

Mitigation: Treat report files and returned links as share-sensitive and avoid posting them broadly.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dragonzu/skills/construction-project-opportunity-radar)
- [Publisher profile](https://clawhub.ai/user/dragonzu)
- [Workflow reference](references/workflow.md)
- [API quick reference](references/api-quick.md)
- [Report template](references/report-template.md)
- [Auto-registration reference](references/auto-register.md)
- [Zhiliaobiaoxun API base](https://mcp-server.zhiliaobiaoxun.com/api_v2/)
- [Zhiliaobiaoxun account and registration API](https://ai.zhiliaobiaoxun.com/web-api/)
- [Zhiliaobiaoxun opportunity platform](https://agent.zhiliaobiaoxun.com)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance, files]

**Output Format:** [Markdown opportunity list in chat, optional self-contained HTML report file, and concise follow-up guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires ZLBX_API_KEY or user-approved automatic registration; complete scans are documented as about 8-15 API calls, with single-route scans about 2-6 calls.]

## Skill Version(s):

1.0.5 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
