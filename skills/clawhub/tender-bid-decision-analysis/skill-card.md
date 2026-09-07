## Description:

This skill helps agents assess whether to bid on a specific tender by analyzing procurement history, likely competitors, pricing signals, and risk into a structured decision report with an optional HTML version.

This skill is ready for commercial/non-commercial use.

## Publisher:

[liu-jiapeng](https://clawhub.ai/user/liu-jiapeng)

### License/Terms of Use:

MIT-0

## Use Case:

External tender, sales, and business-development teams use this skill to decide whether to pursue a specific bid opportunity, estimate competitive pressure, identify pricing signals, and produce a decision report. The skill is intended for grounded analysis from tender data, with explicit data gaps and disclaimers when evidence is incomplete.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Automatic registration can collect a stable device fingerprint when no API key is already configured.

Mitigation: Prefer setting ZLBX_API_KEY yourself, or review and accept the documented registration behavior before using auto-registration.

Risk: API credentials are stored in ~/.zlbx/config.json.

Mitigation: Treat ~/.zlbx/config.json as a sensitive credential file and avoid sharing it or including it in support bundles.

Risk: Generated reports can preserve signed sk links from tender records.

Mitigation: Avoid sharing generated HTML reports unless the audience is allowed to access the underlying linked records.

Risk: Local HTML report generation is flagged by the security evidence as having a security flaw.

Mitigation: Review generated HTML before distribution and keep report sharing limited until the flaw is resolved or accepted.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/liu-jiapeng/skills/tender-bid-decision-analysis)
- [Workflow guide](artifact/references/workflow.md)
- [API quick reference](artifact/references/api-quick.md)
- [Auto-registration flow](artifact/references/auto-register.md)
- [Report template](artifact/references/report-template.md)
- [Zhiliaobiaoxun API base](https://mcp-server.zhiliaobiaoxun.com/api_v2/)
- [Zhiliaobiaoxun account and registration service](https://ai.zhiliaobiaoxun.com/web-api/)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown decision report, optional self-contained HTML report, and supporting local JSON for report rendering]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create a local HTML report under the user's home directory and may include source citations from API-returned records.]

## Skill Version(s):

1.0.4 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
