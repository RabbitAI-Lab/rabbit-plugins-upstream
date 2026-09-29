## Description:

Helps an agent access SharePoint sites, lists, document libraries, and files through Microsoft Graph using a user-authorized Maton connection.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Employees and developers use this skill to find and manage SharePoint sites, lists, and documents through an authorized account. It also describes optional scheduled or event-driven workflows that act on SharePoint content.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A connected account can expose or change SharePoint documents and lists.

Mitigation: Confirm the account, resource, access scope, and exact payload before connecting or writing; prefer read-only access.

Risk: Sharing links may grant broader access to sensitive files.

Mitigation: Explain the intended audience and obtain approval for the narrowest available sharing scope.

Risk: Hosted functions and trigger destinations can continue forwarding data automatically.

Mitigation: Require separate approval for the function, destination host, forwarded fields, and ongoing delivery; remove destinations when no longer needed.

Risk: Credentials or personal data could leak through commands, destinations, or logs.

Mitigation: Keep credentials in the operating system's credential store, exclude them from destination payloads, and limit response output to needed fields.

## Reference(s):

- [ClawHub Microsoft SharePoint skill](https://clawhub.ai/byungkyu/skills/sharepoint)
- [Maton](https://maton.ai)
- [Maton documentation](https://docs.maton.ai)
- [Maton CLI manual](https://cli.maton.ai/manual)
- [Microsoft Graph SharePoint sites](https://learn.microsoft.com/en-us/graph/api/resources/sharepoint)
- [Microsoft Graph drive items](https://learn.microsoft.com/en-us/graph/api/resources/driveitem)
- [Microsoft Graph lists](https://learn.microsoft.com/en-us/graph/api/resources/list)
- [Time trigger reference](artifact/references/time/triggers.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Code, API calls]

**Output Format:** [Markdown with command and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read and list by default; confirm writes, sharing, new connections, and automation with the user.]

## Skill Version(s):

1.2.5 (source: ClawHub release; skill frontmatter lists 1.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
