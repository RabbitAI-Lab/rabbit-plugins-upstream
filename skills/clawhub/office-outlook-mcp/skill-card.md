## Description:

Read and act on the user's Outlook / Microsoft 365 mailbox, including mail, folders, calendar, contacts, and tasks, via the Outlook REST API using a bearer token captured from the user's signed-in browser tab.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Employees and agents use this skill to inspect and act on a user's Microsoft 365 Outlook mailbox, calendar, contacts, and tasks when the user has intentionally provided access through a signed-in Outlook browser session. It supports mailbox queries, calendar lookup, contact and task retrieval, and carefully reviewed write operations such as sending mail, marking messages read, moving messages, creating drafts, and creating events.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill is designed to access and change a real Outlook mailbox using a browser bearer token and broad raw API or curl capabilities.

Mitigation: Install only when the user intentionally wants agent access to the live signed-in Outlook session, and review commands before write operations.

Risk: Mailbox data can include sensitive message bodies, recipients, calendar details, contacts, tasks, and attachments.

Mitigation: Surface only information the user requested, avoid broad body or attachment reads, and prefer selected fields and plain-text bodies for review.

Risk: The captured token is stored locally in ~/.outlook-fpx/curlrc for reuse until expiry or revocation.

Mitigation: Remove ~/.outlook-fpx/curlrc when finished and prefer a properly scoped OAuth-based integration where available.

## Reference(s):

- [Outlook REST v2.0 API endpoint](https://outlook.office.com/api/v2.0)
- [API recipes](references/api-recipes.md)
- [Outlook environment helpers](references/outlook-env.sh)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/office-outlook-mcp)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include Outlook REST request shapes, curl-based helper commands, setup guidance, and concise mailbox or calendar summaries.]

## Skill Version(s):

0.3.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
