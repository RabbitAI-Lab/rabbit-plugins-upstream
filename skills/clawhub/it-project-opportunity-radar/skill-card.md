## Description:

IT information opportunity radar helps agents discover early-stage Chinese IT, Xinchuang, software, systems integration, cloud, data center, cybersecurity, and smart-city opportunities from proposed projects, purchase intentions, and expiring service contracts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dragonzu](https://clawhub.ai/user/dragonzu)

### License/Terms of Use:

MIT-0

## Use Case:

External sales, business-development, and channel teams use this skill to find and prioritize early IT project opportunities in China by industry, product area, region, budget, maturity, and contract renewal timing.

### Deployment Geography for Use:

China

## Known Risks and Mitigations:

Risk: Auto-registration may send a stable device fingerprint and create a locally stored API key.

Mitigation: Prefer a manually provided ZLBX_API_KEY when possible, obtain user consent before auto-registration, and store ~/.zlbx/config.json with restrictive permissions.

Risk: Generated sk links, auto-login links, and exported reports can provide access to sensitive opportunity details.

Mitigation: Treat generated reports and links as sensitive, share them only with intended recipients, and redact or remove direct-access links before broad distribution.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/dragonzu/skills/it-project-opportunity-radar)
- [API Quick Reference](references/api-quick.md)
- [Workflow](references/workflow.md)
- [Report Template](references/report-template.md)
- [Auto Registration](references/auto-register.md)
- [Zhiliaobiaoxun API Base](https://mcp-server.zhiliaobiaoxun.com/api_v2/)
- [Zhiliaobiaoxun Account and Registration](https://ai.zhiliaobiaoxun.com/web-api/)
- [Zhiliaobiaoxun Opportunity Platform](https://agent.zhiliaobiaoxun.com)

## Skill Output:

**Output Type(s):** [Text, Markdown, Files, Guidance]

**Output Format:** [Markdown opportunity list with an optional HTML report file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include source links returned by the API and data-citation summaries; generated links and reports should be treated as sensitive.]

## Skill Version(s):

1.0.5 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
