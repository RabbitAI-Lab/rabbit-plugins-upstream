## Description:

Finds procurement opportunities by scanning proposed projects, purchase intentions, and contracts expiring within 0-180 days, then ranks renewal or replacement opportunities by value and urgency.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dragonzu](https://clawhub.ai/user/dragonzu)

### License/Terms of Use:

MIT-0

## Use Case:

External business development, sales, and procurement-market teams use this skill to find early opportunities from proposed projects, purchase intentions, and renewal windows for expiring contracts. It returns prioritized opportunity lists with next actions and optional report export.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can create or use a vendor account and store an API key under the user's home directory.

Mitigation: Prefer a user-provided ZLBX_API_KEY when available and restrict permissions on ~/.zlbx/config.json.

Risk: Auto-registration sends a stable hashed device identifier for trial deduplication.

Mitigation: Use auto-registration only after explicit user consent, or preconfigure ZLBX_API_KEY to bypass device registration.

Risk: Opportunity links and exported reports can contain signed sk links that may grant access without an additional login prompt.

Mitigation: Avoid sharing generated chats or HTML reports unless the signed links are safe to disclose.

Risk: The skill can generate local HTML reports.

Mitigation: Review generated report contents before opening, distributing, or archiving them, especially when they contain signed links or procurement contact details.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dragonzu/skills/expiring-contract-renewal-finder)
- [Workflow](artifact/references/workflow.md)
- [API quick reference](artifact/references/api-quick.md)
- [Report template](artifact/references/report-template.md)
- [Auto-registration workflow](artifact/references/auto-register.md)
- [ZhiLiaoBiaoXun API base](https://mcp-server.zhiliaobiaoxun.com/api_v2/)
- [ZhiLiaoBiaoXun AI platform](https://ai.zhiliaobiaoxun.com/web-api/)

## Skill Output:

**Output Type(s):** [text, markdown, files, configuration, guidance]

**Output Format:** [Markdown opportunity list with optional self-contained HTML report]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires ZLBX_API_KEY. Generated reports may include API-returned signed sk links and may be saved under ~/zlbx-opportunity-radar-files/.]

## Skill Version(s):

1.0.5 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
