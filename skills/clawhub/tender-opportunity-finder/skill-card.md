## Description:

Finds early tender opportunities from proposed projects, procurement intentions, and expiring contracts, then ranks them into an opportunity list with recommended next actions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dragonzu](https://clawhub.ai/user/dragonzu)

### License/Terms of Use:

MIT-0

## Use Case:

Sales, business-development, and market-intelligence users use this skill to discover public-sector and enterprise tender opportunities before or near formal bidding. The skill scans vendor APIs for proposed projects, procurement intentions, and expiring contracts, then produces a ranked Markdown and optional HTML opportunity report.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may read or create ~/.zlbx/config.json and store an API key locally.

Mitigation: Install only in environments where local credential storage for this vendor is acceptable, and avoid sharing the config file or API key.

Risk: The skill sends tender search terms, regions, and related query parameters to the vendor API.

Mitigation: Avoid entering confidential strategy, customer, or prospect information as search terms unless sharing it with the vendor service is acceptable.

Risk: Trial registration may send a MAC-hash device identifier and other device attributes.

Mitigation: Use a preconfigured ZLBX_API_KEY to bypass auto-registration, or decline automatic registration if device fingerprinting is not acceptable.

Risk: Generated reports and returned links may contain sk or auto-login links that grant access.

Mitigation: Treat generated reports and chat transcripts as sensitive and remove login-bearing links before sharing outside trusted recipients.

Risk: Tender opportunity rankings can be incomplete or stale because they depend on external public-tender data.

Mitigation: Use the ranked list as lead-generation support only and verify high-value opportunities against the source platform before acting.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dragonzu/skills/tender-opportunity-finder)
- [API quick reference](references/api-quick.md)
- [Auto-registration workflow](references/auto-register.md)
- [Report template](references/report-template.md)
- [Workflow guide](references/workflow.md)
- [ZLBX API base](https://mcp-server.zhiliaobiaoxun.com/api_v2/)
- [ZLBX web API](https://ai.zhiliaobiaoxun.com/web-api/)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown opportunity list with optional self-contained HTML report]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May write HTML reports under ~/zlbx-opportunity-radar-files/ and may read or create ~/.zlbx/config.json for API-key storage.]

## Skill Version(s):

1.0.6 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
