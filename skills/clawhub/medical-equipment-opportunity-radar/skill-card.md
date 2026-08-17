## Description:

帮助代理根据产品线和地区扫描医院及卫健采购的拟建项目、采购意向和临期续约机会，并按价值与紧急度输出跟进清单。

This skill is ready for commercial/non-commercial use.

## Publisher:

[dragonzu](https://clawhub.ai/user/dragonzu)

### License/Terms of Use:

MIT-0

## Use Case:

External sales, business development, and procurement-intelligence users use this skill to find early hospital and health-system purchasing opportunities before formal tenders are published. The agent scans proposed construction projects, purchase intentions, and expiring service contracts, then ranks opportunities and recommends next actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The vendor API receives search terms such as product lines, regions, and procurement interests.

Mitigation: Install only when that sharing is acceptable, and avoid entering sensitive private strategy terms that should not leave the agent environment.

Risk: Auto-registration can send a hashed device identifier to the vendor when no API key is configured.

Mitigation: Prefer configuring ZLBX_API_KEY manually; if auto-registration is used, require explicit user consent before collecting device features or registering.

Risk: Generated auto-login URLs and sk-bearing report or announcement links can grant convenient access to vendor-hosted pages.

Mitigation: Treat those links as sensitive and avoid sharing exported HTML reports or account links outside the intended audience.

Risk: The skill may consume paid query credits during full scans.

Mitigation: Tell the user the estimated credit cost before scanning and pause for approval before exceeding the documented default query budget.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dragonzu/skills/medical-equipment-opportunity-radar)
- [Publisher profile](https://clawhub.ai/user/dragonzu)
- [Workflow guide](artifact/references/workflow.md)
- [API quick reference](artifact/references/api-quick.md)
- [Report template](artifact/references/report-template.md)
- [Auto-registration guide](artifact/references/auto-register.md)
- [Zhiliaobiaoxun opportunity platform](https://agent.zhiliaobiaoxun.com)

## Skill Output:

**Output Type(s):** [text, markdown, files, guidance]

**Output Format:** [Markdown opportunity list in the conversation, with an optional self-contained HTML report file.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Ranks opportunities by budget, urgency or maturity, and product match; default full scans are capped at about 8-15 query credits unless the user approves more.]

## Skill Version(s):

1.0.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
