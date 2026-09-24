## Description:

Reducto document processing API integration with managed API key authentication for parsing, extracting, splitting, and editing documents.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to connect an agent to Reducto through Maton for document parsing, structured extraction, splitting, editing, uploads, and job checks. It is intended for user-approved document workflows that need managed authentication and explicit confirmation before writes or automation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected documents and extracted document contents may be sent to Reducto through Maton.

Mitigation: Confirm the user is comfortable with that data flow and process only the documents and fields required for the approved task.

Risk: Long-lived API keys or raw credentials can be exposed through environment variables, command history, logs, or destination configuration.

Mitigation: Prefer OAuth and the CLI credential store, avoid embedding credentials in headers or body templates, and rotate any key that was printed, committed, or pasted.

Risk: Uploads, edits, connection changes, functions, triggers, and destinations can modify data or create persistent automation.

Mitigation: Default to read and list operations, then require explicit user confirmation for each write, upload, edit, connection, deployment, trigger, destination, or replay action.

Risk: Triggers and destinations can continuously forward document-related or third-party event data beyond the original interactive request.

Mitigation: Create them only for a specific approved workflow, scope them narrowly, forward minimum fields, and prefer Maton-hosted destinations unless the user approves an exact external host.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/reducto)
- [Maton Homepage](https://maton.ai)
- [Reducto Documentation](https://docs.reducto.ai)
- [Reducto API Reference](https://docs.reducto.ai/api-reference)
- [Reducto Studio](https://studio.reducto.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Time Trigger Reference](references/time/triggers.md)
- [Calendly Trigger Reference](references/calendly/triggers.md)
- [GitHub Trigger Reference](references/github/triggers.md)
- [Gmail Trigger Reference](references/google-mail/triggers.md)
- [HubSpot Trigger Reference](references/hubspot/triggers.md)
- [Linear Trigger Reference](references/linear/triggers.md)
- [Notion Trigger Reference](references/notion/triggers.md)
- [Slack Trigger Reference](references/slack/triggers.md)
- [Stripe Trigger Reference](references/stripe/triggers.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands, JSON examples, and code snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires network access, a Maton account, and user-approved Reducto connection actions.]

## Skill Version(s):

1.2.4 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
