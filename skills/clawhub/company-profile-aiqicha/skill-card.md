## Description:

This skill helps agents produce Chinese company intelligence reports from a bidding and tendering perspective, covering company profiles, business keywords, bid-winning strength, customer and supplier relationships, competitors, public risk signals, and optional contact channels.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dragonzu](https://clawhub.ai/user/dragonzu)

### License/Terms of Use:

MIT-0

## Use Case:

External business, procurement, sales, and competitive-intelligence users use this skill to investigate one company or compare two companies using bidding and tendering evidence. It is designed to generate a concise report with traceable data, source links, stated data boundaries, and optional contact lookup.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Company queries, regions, and related search parameters are sent to external ZLBX APIs.

Mitigation: Tell users when external API access is required, avoid uploading local file contents, and use only the configured business-intelligence endpoints described by the skill.

Risk: Automatic trial registration may use a stable hashed device identifier and can store an API key locally.

Mitigation: Require explicit user consent before registration, collect only the documented minimal device features, and prefer a user-provided API key when available.

Risk: Generated HTML reports, signed direct-access links, and contact information may expose business or contact data if shared broadly.

Mitigation: Review generated reports before sharing, preserve access controls for saved report files, and display contacts only in the form returned by the API.

Risk: Company intelligence and public-risk sections can mislead readers if unsupported claims or accusatory wording are introduced.

Mitigation: Keep claims tied to returned data or cited public sources, separate facts from interpretations, and retain the report disclaimer and data-boundary notes.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dragonzu/skills/company-profile-aiqicha)
- [Publisher profile](https://clawhub.ai/user/dragonzu)
- [API quick reference](references/api-quick.md)
- [Auto-registration workflow](references/auto-register.md)
- [Report template](references/report-template.md)
- [Seven-step workflow](references/workflow.md)
- [ZLBX API base URL](https://mcp-server.zhiliaobiaoxun.com/api_v2/)
- [ZLBX account and registration API base URL](https://ai.zhiliaobiaoxun.com/web-api/)
- [ZLBX skill documentation](https://ai.zhiliaobiaoxun.com/docs/skill)
- [ZLBX business-intelligence platform](https://agent.zhiliaobiaoxun.com)

## Skill Output:

**Output Type(s):** [text, markdown, files, guidance]

**Output Format:** [Markdown report in conversation plus an optional generated HTML report file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports should include traceable citations, original signed URLs where returned by the API, data-boundary notes, and disclaimers.]

## Skill Version(s):

1.0.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
