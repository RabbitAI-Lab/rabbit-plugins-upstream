## Description:

This skill helps sales and business development users generate procurement-focused client background reports from ZLBX tender and award data, including company profile, purchasing history, supplier and customer relationships, competitive overlap, public risk signals, and optional HTML reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dragonzu](https://clawhub.ai/user/dragonzu)

### License/Terms of Use:

MIT-0

## Use Case:

External sales, BD, procurement, and partner-screening users provide one or two organization names to receive a structured company intelligence report before outreach, bidding, supplier review, or competitive comparison. The skill emphasizes public tender records, API-returned evidence, cited public risk sources, and explicit data boundaries.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill stores credentials in local configuration and uses the ZLBX_API_KEY environment variable or ~/.zlbx/config.json.

Mitigation: Treat API keys and ~/.zlbx/config.json as sensitive, prefer preconfigured user-owned credentials, and avoid exposing credentials in conversation or reports.

Risk: Automatic registration may send a hashed MAC-derived device identifier together with platform and CPU architecture.

Mitigation: Run automatic registration only after explicit user consent, skip it when a key is already configured, and keep the collected device data limited to the documented three fields.

Risk: Company pages, tender links, contact details, and saved HTML reports can contain signed or sensitive business information.

Mitigation: Review reports before sharing, preserve API-returned links without modification, and handle saved HTML files and signed links as sensitive artifacts.

Risk: Business conclusions about real organizations could be misleading or reputationally sensitive if unsupported or over-stated.

Mitigation: Use only API-returned amounts, counts, company names, and cited public sources; label data gaps clearly and keep risk language factual rather than accusatory.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dragonzu/skills/client-background-check)
- [ZLBX API base](https://mcp-server.zhiliaobiaoxun.com/api_v2/)
- [ZLBX account and registration API](https://ai.zhiliaobiaoxun.com/web-api/)
- [ZLBX manual registration](https://ai.zhiliaobiaoxun.com/?ch=s127)
- [ZLBX agent platform](https://agent.zhiliaobiaoxun.com)
- [Workflow guide](references/workflow.md)
- [API quick reference](references/api-quick.md)
- [Report template](references/report-template.md)
- [Auto-registration guide](references/auto-register.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown report in the conversation, optional self-contained HTML file, and supporting JSON passed to the local report renderer]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses ZLBX API responses and optional public web search sources; generated reports include cited data boundaries and may save HTML files under the user's home directory.]

## Skill Version(s):

1.0.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
