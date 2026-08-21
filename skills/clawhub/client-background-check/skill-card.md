## Description:

Helps sales and BD users prepare for customer meetings by generating procurement-background reports from Zhiliaobiaoxun tender data, including customer profiles, purchasing history, budget scale, supplier relationships, competitors, and public-risk notes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dragonzu](https://clawhub.ai/user/dragonzu)

### License/Terms of Use:

MIT-0

## Use Case:

Sales and BD teams use this skill before prospect meetings, bids, or partner reviews to understand an organization's procurement history, budget scale, active suppliers, competitive landscape, and public-risk signals. It supports single-customer background reports and two-organization comparisons.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses Zhiliaobiaoxun services for report generation and may send company queries to external APIs.

Mitigation: Use it only when the user is comfortable with the Zhiliaobiaoxun service and disclose that report data comes from that service before running the workflow.

Risk: If no API key is preconfigured, the skill can create an external account using platform, CPU architecture, and a hashed MAC-derived value.

Mitigation: Preconfigure ZLBX_API_KEY to avoid auto-registration, or require explicit user consent before collecting those device features or making registration requests.

Risk: API keys and generated reports are stored in the user's home directory, and reports or company links may include signed access parameters.

Mitigation: Protect ~/.zlbx/config.json and generated report files, and share signed report or company links only with intended recipients.

Risk: Procurement background reports are based on public tender data and may omit private contracts, unpublished procurement, or delayed records.

Mitigation: State data boundaries in the report, distinguish facts from inferences, cite sources for public-risk notes, and avoid treating the report as a sole business decision basis.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dragonzu/skills/client-background-check)
- [Workflow guide](artifact/references/workflow.md)
- [API quick reference](artifact/references/api-quick.md)
- [Report template](artifact/references/report-template.md)
- [Auto-registration flow](artifact/references/auto-register.md)
- [Zhiliaobiaoxun API endpoint pattern](https://mcp-server.zhiliaobiaoxun.com/api_v2/{tool_name})
- [Zhiliaobiaoxun AI platform](https://ai.zhiliaobiaoxun.com/?ch=s127)
- [Zhiliaobiaoxun business intelligence portal](https://agent.zhiliaobiaoxun.com)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance, Files]

**Output Format:** [Markdown reports and self-contained HTML files, with API-result links preserved when present.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires ZLBX_API_KEY or consent-gated auto-registration; generated HTML reports default to ~/zlbx-company-intel-files/.]

## Skill Version(s):

1.0.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
