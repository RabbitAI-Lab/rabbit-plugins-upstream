## Description:

Keap API integration with managed OAuth for managing contacts, companies, tags, tasks, orders, products, opportunities, subscriptions, affiliates, users, campaign sequences, automations, and transactional email in CRM and marketing automation workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to let an agent read and manage Keap CRM and marketing automation records through Maton-managed OAuth. It supports contact, company, tag, task, order, product, opportunity, subscription, affiliate, user, campaign sequence, automation, and transactional email workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can perform account-level Keap API writes, including sends, campaign enrollment, billing-related changes, and deletions.

Mitigation: Use OAuth with the narrowest scopes available and confirm exact records, recipients, payloads, and effects before allowing any write.

Risk: Transactional email and campaign sequence operations can contact people outside the account and may not be reversible after execution.

Mitigation: Review recipient lists, subject lines, message bodies, campaign identifiers, and sequence effects with the user before execution.

Risk: Raw API passthrough can reach endpoints beyond the documented surface if the connection permits them.

Mitigation: Default to documented read/list calls and use undocumented paths only when the user requests the specific call and approves the resulting action.

Risk: Fallback API-key use increases credential exposure risk compared with the managed CLI flow.

Mitigation: Prefer Maton OAuth through the CLI; when a Maton API key is unavoidable, keep it out of logs, files, shell history, and command arguments.

## Reference(s):

- [Keap Skill on ClawHub](https://clawhub.ai/byungkyu/skills/keap)
- [Publisher Profile](https://clawhub.ai/user/byungkyu)
- [Maton](https://maton.ai)
- [Keap Developer Portal](https://developer.infusionsoft.com/)
- [Keap REST API V2 Documentation](https://developer.infusionsoft.com/docs/restv2/)
- [Keap Getting Started Guide](https://developer.infusionsoft.com/getting-started/)
- [Keap OAuth 2.0 Authentication](https://developer.infusionsoft.com/authentication/)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, code, text]

**Output Format:** [Markdown with inline shell commands, JSON examples, and code snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guidance is oriented around Maton CLI and API calls, with read-first behavior and confirmation before writes.]

## Skill Version(s):

1.2.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
