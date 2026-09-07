## Description:

GetResponse API integration with managed OAuth for managing email marketing campaigns, contacts, newsletters, autoresponders, segments, workflows, ecommerce, SMS, landing pages, webinars, transactional emails, forms, and account data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to manage GetResponse marketing, automation, ecommerce, messaging, and account resources through Maton-authenticated API calls. It is suited for read/list workflows by default and for write or messaging workflows only after explicit user approval.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can use Maton OAuth or API access to operate on a connected GetResponse account.

Mitigation: Install only when Maton should connect to the account, review OAuth scopes during authorization, and use the intended connection explicitly when multiple connections exist.

Risk: Messaging and write actions can send communications, modify records, trigger workflows, or delete GetResponse resources.

Mitigation: Require the agent to show recipients, content, timing, target resource IDs, payloads, and intended effects before any send, update, create, delete, or workflow action.

Risk: Long-lived API keys or provider-issued tokens can be exposed if printed, logged, persisted, or passed through command lines.

Mitigation: Prefer OAuth, keep credentials in the configured credential store or process environment, never print or persist secrets, and rotate any key that was exposed.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/getresponse)
- [Maton Homepage](https://maton.ai)
- [GetResponse API Documentation](https://apidocs.getresponse.com/v3)
- [GetResponse OpenAPI Spec](https://apireference.getresponse.com/open-api.json)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, code, configuration, guidance]

**Output Format:** [Markdown with inline shell commands, API paths, JSON payload examples, and SDK code snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include Maton CLI commands, GetResponse API endpoints, JSON request bodies, Python or JavaScript SDK examples, and confirmation guidance for write or messaging actions.]

## Skill Version(s):

1.2.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
