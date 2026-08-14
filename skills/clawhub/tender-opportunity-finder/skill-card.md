## Description:

招标商机发现助手，用于根据行业、产品和地区发现拟建项目、采购意向和临期续约机会，并按价值排序输出商机清单。

This skill is ready for commercial/non-commercial use.

## Publisher:

[dragonzu](https://clawhub.ai/user/dragonzu)

### License/Terms of Use:

MIT-0

## Use Case:

Sales, business development, and market-research users use this skill to identify early tender-related opportunities before formal bidding, compare proposed projects, purchase intentions, and expiring contracts, and decide which leads to pursue next.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Search queries and tender-opportunity criteria are sent to the third-party Zhiliaobiaoxun API.

Mitigation: Use the skill only for queries you are comfortable sharing with the vendor and avoid including confidential customer or strategy details in search terms.

Risk: Automatic trial registration can submit a hashed device identifier when no API key is configured.

Mitigation: Set ZLBX_API_KEY yourself before use to bypass auto-registration, and review ~/.zlbx/config.json after use.

Risk: Generated reports and returned opportunity links can include signed sk parameters.

Mitigation: Treat HTML reports and sk-bearing links as sensitive and avoid sharing them beyond intended recipients.

Risk: The skill stores credentials locally for later API calls.

Mitigation: Protect access to ~/.zlbx/config.json and remove or rotate the API key if the environment is shared.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dragonzu/skills/tender-opportunity-finder)
- [Publisher profile](https://clawhub.ai/user/dragonzu)
- [API quick reference](artifact/references/api-quick.md)
- [Workflow guide](artifact/references/workflow.md)
- [Report template](artifact/references/report-template.md)
- [Auto-registration flow](artifact/references/auto-register.md)
- [Tender opportunity API](https://mcp-server.zhiliaobiaoxun.com/api_v2/{tool})
- [Zhiliaobiaoxun opportunity platform](https://agent.zhiliaobiaoxun.com)

## Skill Output:

**Output Type(s):** [text, markdown, files, shell commands, configuration, guidance]

**Output Format:** [Markdown opportunity list with optional self-contained HTML report file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include original tokenized opportunity links and a local HTML report path.]

## Skill Version(s):

1.0.3 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
