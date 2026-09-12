## Description:

This skill lets agents query and analyze Zhiliaobiaoxun procurement, tender, bid award, company, supplier, competitor, and market data through authenticated APIs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhiliaobiaoxun](https://clawhub.ai/user/zhiliaobiaoxun)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to search tender and award notices, retrieve project details, analyze companies, suppliers, competitors, and market trends, and produce structured procurement-market reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can create an account and send a hashed MAC-derived device identifier during consent-based automatic registration.

Mitigation: Prefer manually configuring ZLBX_API_KEY; if automatic registration is used, require explicit user consent before collecting device features or calling the registration endpoint.

Risk: The skill can store API credentials in ~/.zlbx/config.json.

Mitigation: Protect the config file with user-only permissions and do not disclose API keys in prompts, outputs, logs, or shared transcripts.

Risk: Recharge or login links may act as bearer-style access links if shared.

Mitigation: Avoid sharing transcripts that contain generated recharge or login links, and regenerate links only when the user requests a fresh link.

Risk: Procurement contacts and phone numbers returned by the APIs may be sensitive.

Mitigation: Treat returned contact data as sensitive, preserve server-side masking, and do not use other sources to complete masked phone numbers or perform bulk contact export.

## Reference(s):

- [Skill source](SKILL.md)
- [Bid search API details](references/api-search.md)
- [Company analysis API details](references/api-company.md)
- [Market analysis API details](references/api-market.md)
- [Account query API details](references/api-account.md)
- [Automatic registration flow](references/auto-register.md)
- [ClawHub skill page](https://clawhub.ai/zhiliaobiaoxun/skills/bid-data-intelligent-agent)

## Skill Output:

**Output Type(s):** [text, markdown, API calls, configuration guidance]

**Output Format:** [Markdown summaries, tables, and structured procurement analysis based on JSON REST API responses.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires ZLBX_API_KEY or consent-based account setup; returned contact details may be masked or sensitive.]

## Skill Version(s):

1.0.5 (source: server evidence release.version)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
