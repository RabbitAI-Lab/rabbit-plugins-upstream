## Description:

This skill helps users discover early public procurement opportunities by scanning proposed projects, procurement intents, and expiring contracts before formal bid publication.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dragonzu](https://clawhub.ai/user/dragonzu)

### License/Terms of Use:

MIT-0

## Use Case:

External users, sales teams, and procurement analysts use this skill to identify and prioritize upcoming government or enterprise procurement opportunities by industry, region, budget, maturity, and renewal timing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Procurement search terms and scan criteria are sent to the vendor service.

Mitigation: Tell users what scope will be queried and avoid sending unrelated local files or sensitive business context.

Risk: The skill can create or use a vendor account and store a vendor API key under ~/.zlbx/config.json.

Mitigation: Prefer a user-provided ZLBX_API_KEY when available, obtain consent before auto-registration, and review local file permissions after first use.

Risk: Shareable reports and announcement links may contain signed login-free access parameters.

Mitigation: Keep API-returned links intact for functionality, but avoid broad redistribution of exported reports unless the user accepts that access model.

Risk: Automatic registration uses device fingerprinting for free-trial de-duplication.

Mitigation: Use the documented consent gate before registration and allow users to skip fingerprinting by pre-configuring their own API key.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dragonzu/skills/procurement-intent-monitor)
- [Publisher profile](https://clawhub.ai/user/dragonzu)
- [API quick reference](references/api-quick.md)
- [Auto-registration workflow](references/auto-register.md)
- [Report template](references/report-template.md)
- [Execution workflow](references/workflow.md)
- [ZhiLiaoBiaoXun API base](https://mcp-server.zhiliaobiaoxun.com/api_v2/)
- [ZhiLiaoBiaoXun registration API base](https://ai.zhiliaobiaoxun.com/web-api/)
- [ZhiLiaoBiaoXun opportunity portal](https://agent.zhiliaobiaoxun.com)

## Skill Output:

**Output Type(s):** [text, markdown, files, shell commands, configuration, guidance]

**Output Format:** [Markdown opportunity lists with optional self-contained HTML report files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include source links returned by the vendor API; credentials should not be included in user-visible responses.]

## Skill Version(s):

1.0.5 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
