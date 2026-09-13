## Description:

Zoho People API integration with managed OAuth for managing employees, departments, designations, attendance, leave, and custom HR forms.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and automation operators use this skill to read, create, update, and query Zoho People HR data through Maton-managed OAuth. It is suited for Zoho People tasks involving employee records, departments, designations, attendance, leave, and configured forms when the user explicitly requests the data or operation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Zoho People can expose sensitive HR records, including employee personal data and custom form data.

Mitigation: Access only records the user explicitly requests, prefer least-privilege OAuth scopes, and avoid bulk retrieval unless clearly justified.

Risk: Write operations can create, update, or delete HR records or trigger downstream workflow effects.

Mitigation: Default to read and list calls, then require explicit approval for every POST, PUT, PATCH, or DELETE with the target resource, payload, and intended effect.

Risk: Hosted functions, triggers, and destinations can run or forward data persistently after setup.

Mitigation: Create automation only when the user asks for it, keep destinations inside approved Maton-hosted functions unless the user names another host, and use a dedicated Maton account with only the needed connection.

Risk: API keys and connection credentials could be exposed if printed, stored in files, or passed through shell environments.

Mitigation: Prefer OAuth over API keys, use the operating system credential store through the Maton CLI, and do not print, export, or embed credentials.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/zoho-people)
- [Maton Homepage](https://maton.ai)
- [Zoho People API Overview](https://www.zoho.com/people/api/overview.html)
- [Get Bulk Records API](https://www.zoho.com/people/api/bulk-records.html)
- [Fetch Forms API](https://www.zoho.com/people/api/forms-api/fetch-forms.html)
- [Insert Record API](https://www.zoho.com/people/api/insert-records.html)
- [Update Record API](https://www.zoho.com/people/api/update-records.html)
- [Attendance API](https://www.zoho.com/people/api/attendance-entries.html)
- [Leave API](https://www.zoho.com/people/api/add-leave.html)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Calendly Trigger Reference](references/calendly/triggers.md)
- [GitHub Trigger Reference](references/github/triggers.md)
- [Gmail Trigger Reference](references/google-mail/triggers.md)
- [HubSpot Trigger Reference](references/hubspot/triggers.md)
- [Linear Trigger Reference](references/linear/triggers.md)
- [Notion Trigger Reference](references/notion/triggers.md)
- [Slack Trigger Reference](references/slack/triggers.md)
- [Stripe Trigger Reference](references/stripe/triggers.md)
- [Time Trigger Reference](references/time/triggers.md)

## Skill Output:

**Output Type(s):** [API Calls, Shell commands, Code, Configuration instructions, Guidance]

**Output Format:** [Markdown guidance with CLI commands, JSON examples, and code snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may reference sensitive HR records and should be limited to fields the user explicitly requests.]

## Skill Version(s):

1.2.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
