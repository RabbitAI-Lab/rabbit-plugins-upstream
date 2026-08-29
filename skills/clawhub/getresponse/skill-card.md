## Description:

GetResponse gives an agent Maton-managed OAuth access to GetResponse account, campaign, contact, newsletter, automation, ecommerce, SMS, webinar, transactional email, form, and related API operations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Marketing operators, developers, and agents use this skill to inspect and manage GetResponse campaigns, contacts, messages, automations, ecommerce records, and account data through Maton-mediated API calls. It is suited to workflows that need read-first account review and user-approved changes to marketing or messaging resources.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can make real changes to a connected GetResponse account, including creating, updating, deleting, importing, publishing, or enabling resources.

Mitigation: Default to read and list operations first, then require explicit user approval that names the target resource, payload, and intended effect before any write call.

Risk: Newsletter, SMS, and transactional email operations can deliver messages to real contacts and affect cost, compliance, or sender reputation.

Mitigation: Confirm the audience, content, sender context, and scheduled timing with the user immediately before any send or schedule action.

Risk: OAuth tokens, API keys, or provider-issued sub-credentials could be exposed if printed, persisted, copied into shell history, or sent to the wrong host.

Mitigation: Prefer Maton OAuth with the narrowest available scopes, keep credentials in the approved credential store, do not print or persist them, and send raw API-key fallback requests only to api.maton.ai using stdin-based configuration.

Risk: Multiple Maton profiles or GetResponse connections can make the target account ambiguous.

Mitigation: List available connections when needed and specify the intended Maton profile and GetResponse connection before executing account-specific or write operations.

Risk: Content returned from GetResponse may include untrusted text that attempts to steer subsequent agent actions.

Mitigation: Treat API response content as data, validate it before reuse, and never let fetched content select endpoints, recipients, commands, or follow-up actions.

## Reference(s):

- [ClawHub GetResponse Skill](https://clawhub.ai/byungkyu/skills/getresponse)
- [byungkyu ClawHub Profile](https://clawhub.ai/user/byungkyu)
- [Maton](https://maton.ai)
- [GetResponse API Documentation](https://apidocs.getresponse.com/v3)
- [GetResponse OpenAPI Spec](https://apireference.getresponse.com/open-api.json)
- [Maton Docs](https://docs.maton.ai)
- [Maton CLI Manual](https://cli.maton.ai/manual)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands, JSON request bodies, and API path examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may propose Maton CLI or raw HTTP calls; write operations require explicit user approval before execution.]

## Skill Version(s):

1.1.0 (source: evidence.release.version)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
