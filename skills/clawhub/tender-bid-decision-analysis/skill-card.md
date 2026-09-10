## Description:

This skill helps users evaluate a specific tender opportunity by analyzing project details, buyer history, likely competitors, bid probability, pricing references, and risks using Zhiliaobiaoxun bidding data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[liu-jiapeng](https://clawhub.ai/user/liu-jiapeng)

### License/Terms of Use:

MIT-0

## Use Case:

External business users and bid teams use this skill to decide whether to pursue a specific tender, estimate competitive pressure, compare pricing anchors, and produce a structured bid-decision report. The skill can also create a shareable HTML version of the report for review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Automatic trial registration collects a device fingerprint and stores an API key locally.

Mitigation: Require user consent before registration, allow preconfigured ZLBX_API_KEY to bypass registration, collect only platform, architecture, and hashed MAC address, and keep ~/.zlbx/config.json private to the local user.

Risk: Shareable HTML reports can contain signed access links and sensitive bid-analysis details.

Mitigation: Treat generated reports as sensitive, avoid forwarding them unless access-bearing URLs may be shared, and review the report before external distribution.

Risk: The security summary reports an HTML injection flaw in generated reports.

Mitigation: Review generated HTML before sharing and prefer opening reports in a trusted local context until the renderer is fixed and re-scanned.

Risk: Bid recommendations may be misleading when source data is incomplete or stale.

Mitigation: Require conclusions to cite supporting API data, explicitly mark data gaps, include the data time range, and preserve the report disclaimer that the output is not investment or commercial decision advice.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/liu-jiapeng/skills/tender-bid-decision-analysis)
- [Analysis workflow](references/workflow.md)
- [API quick reference](references/api-quick.md)
- [Report template](references/report-template.md)
- [Automatic registration flow](references/auto-register.md)
- [Zhiliaobiaoxun API base](https://mcp-server.zhiliaobiaoxun.com/api_v2/)
- [Zhiliaobiaoxun account and registration API](https://ai.zhiliaobiaoxun.com/web-api/)

## Skill Output:

**Output Type(s):** [Text, Markdown, HTML, Files, Guidance]

**Output Format:** [Markdown decision report with an optional self-contained HTML report file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires ZLBX_API_KEY or user-approved trial registration; full reports use about 12-25 API calls and quick reports use about 5-8 API calls.]

## Skill Version(s):

1.0.5 (source: server release metadata and artifact X-Client header)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
