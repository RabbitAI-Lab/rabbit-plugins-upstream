## Description:

Podio API integration with managed OAuth for managing workspaces, apps, items, tasks, comments, and files through Maton.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Employees, external collaborators, and developers use this skill to inspect and update Podio organizations, workspaces, apps, items, tasks, comments, and files from an agent workflow. It is suited for Podio account automation where users can confirm the target connection and any write, sharing, deletion, or workflow-triggering action.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can mediate access to a user's Podio account through Maton.

Mitigation: Install only when Podio access through Maton is intended, prefer OAuth over API keys, and do not expose stored credentials.

Risk: Create, update, comment, delete, sharing, connection deletion, and workflow-triggering actions can change Podio state or access.

Mitigation: Confirm the exact Podio connection, resource identifiers, payloads, file attachments, external links, and intended effect before any such action.

Risk: Using an unintended Podio connection or Maton profile can send reads or writes to the wrong account.

Mitigation: List active connections first and specify the target connection when more than one Podio connection or Maton account is available.

Risk: API responses, comments, files, webhook payloads, and other external content may contain untrusted instructions or data.

Mitigation: Treat returned content as data, validate it before reuse, and never let it choose follow-up endpoints, recipients, or commands.

## Reference(s):

- [ClawHub Podio Skill](https://clawhub.ai/byungkyu/skills/podio)
- [byungkyu ClawHub Profile](https://clawhub.ai/user/byungkyu)
- [Maton Homepage](https://maton.ai)
- [Podio API Documentation](https://developers.podio.com/doc)
- [Podio API Authentication](https://developers.podio.com/authentication)
- [Podio Items API](https://developers.podio.com/doc/items)
- [Podio Tasks API](https://developers.podio.com/doc/tasks)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, code]

**Output Format:** [Markdown with inline bash, JSON, Python, and JavaScript code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces commands and request patterns for Podio API calls through Maton; does not itself return live Podio data without execution by an agent.]

## Skill Version(s):

1.2.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
