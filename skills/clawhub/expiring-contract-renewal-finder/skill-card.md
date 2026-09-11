## Description:

Finds expiring contract renewal opportunities and adjacent early procurement signals, then ranks them into an opportunity shortlist for a requested industry, product, region, or budget threshold.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dragonzu](https://clawhub.ai/user/dragonzu)

### License/Terms of Use:

MIT-0

## Use Case:

External business development, sales, and procurement users use this skill to discover China-focused expiring public contract renewal windows, proposed projects, and purchase-intent opportunities before or near tender activity. It returns a prioritized opportunity list with objective next-step suggestions and optional local HTML reporting.

### Deployment Geography for Use:

China

## Known Risks and Mitigations:

Risk: Search terms and automatic-signup device identifiers are sent to the vendor service.

Mitigation: Use only when those search terms are appropriate to share with the vendor, and preconfigure ZLBX_API_KEY manually to avoid the automatic signup flow when possible.

Risk: Credentials are stored locally in ~/.zlbx/config.json.

Mitigation: Check local file permissions, avoid placing the file in shared backups or repositories, and rotate the key if it may have been exposed.

Risk: Generated reports and opportunity links can contain sk-bearing or login-bypass URLs.

Mitigation: Share reports and links only with intended recipients, and remove sensitive links before broader distribution.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dragonzu/skills/expiring-contract-renewal-finder)
- [API quick reference](artifact/references/api-quick.md)
- [Workflow guide](artifact/references/workflow.md)
- [Auto-registration guide](artifact/references/auto-register.md)
- [Report template](artifact/references/report-template.md)
- [Zhiliao Biaoxun API base](https://mcp-server.zhiliaobiaoxun.com/api_v2/)
- [Zhiliao Biaoxun skill documentation](https://ai.zhiliaobiaoxun.com/docs/skill)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown opportunity shortlist, with optional self-contained HTML report file and concise configuration guidance.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May use ZLBX_API_KEY for authenticated API access; optional reports are written locally under the user's opportunity-radar report directory.]

## Skill Version(s):

1.0.6 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
