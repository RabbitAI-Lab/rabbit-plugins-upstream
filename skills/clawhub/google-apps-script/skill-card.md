## Description:

Provides managed OAuth access to the Google Apps Script API so an agent can create and update Apps Script projects, manage deployments and versions, execute script functions, and monitor script processes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and automation engineers use this skill to operate Google Apps Script projects through Maton-mediated OAuth, including project content updates, deployments, version management, remote function execution, process monitoring, and approved hosted automations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Google Apps Script access can include sensitive write, deploy, run, or trigger actions under the user's authorized account.

Mitigation: Review OAuth scopes, default to read/list operations, and require explicit confirmation before connection creation, write calls, deployments, function runs, trigger setup, or destination changes.

Risk: Persistent triggers or destinations can continue running after the immediate agent session ends.

Mitigation: Scope triggers narrowly, state the destination and transmitted data before approval, prefer Maton-hosted destinations where appropriate, and remove unused automations when the task is complete.

Risk: API keys, raw HTTP calls, logs, or forwarded event payloads can expose credentials or private business data.

Mitigation: Prefer OAuth through the Maton CLI credential store, avoid long-lived environment credentials when possible, minimize forwarded fields, and do not log raw responses or secrets.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/google-apps-script)
- [Maton Homepage](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Apps Script API Overview](https://developers.google.com/apps-script/api)
- [Apps Script API Reference](https://developers.google.com/apps-script/api/reference/rest)
- [Projects Resource](https://developers.google.com/apps-script/api/reference/rest/v1/projects)
- [Deployments Guide](https://developers.google.com/apps-script/api/how-tos/manage-deployments)
- [Executing Functions](https://developers.google.com/apps-script/api/how-tos/execute)
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

**Output Type(s):** [Guidance, Shell commands, Code, Configuration]

**Output Format:** [Markdown with inline bash, Python, and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include OAuth connection steps, API endpoints, function or trigger setup, and user approval prompts.]

## Skill Version(s):

1.2.3 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
