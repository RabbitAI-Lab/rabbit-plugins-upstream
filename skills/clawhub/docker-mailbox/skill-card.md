## Description:

docker-mailbox lets an agent use a single REST API or streamable HTTP MCP server to read, search, send, mark seen, and delete messages across configured IMAP/SMTP mailboxes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and automation agents use this skill to operate one or more real mail accounts through mailboxd without building provider-specific IMAP/SMTP clients or webmail tooling.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can let an agent read, send, and delete mail from real configured accounts.

Mitigation: Install it only when agent access to those accounts is intended, and scope mailboxd configuration to the accounts the agent should operate.

Risk: If auth.tokens is empty, reachable HTTP and MCP endpoints can expose mailbox read, send, and delete access without authentication.

Mitigation: Configure long random bearer tokens, keep them private, and bind to loopback or place the service behind strong access controls before network exposure.

Risk: Delete operations are permanent because messages are marked deleted and expunged immediately.

Mitigation: Require explicit confirmation of the exact mailbox and message UID before every delete action, especially after broad searches.

Risk: Mailbox configuration contains email credentials and bearer tokens.

Mitigation: Treat config.yaml as secret material, keep it out of source control and chat, restrict file permissions, and mount it read-only where possible.

## Reference(s):

- [docker-mailbox setup](references/setup.md)
- [docker-mailbox ClawHub page](https://clawhub.ai/psyb0t/skills/docker-mailbox)
- [docker-mailbox repository](https://github.com/psyb0t/docker-mailbox)
- [html2text project](https://github.com/Alir3z4/html2text)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, JSON, Guidance]

**Output Format:** [Markdown guidance with curl commands, JSON request and response examples, and MCP configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires MAILBOX_URL and, when server auth is enabled, MAILBOX_TOKEN.]

## Skill Version(s):

1.2.3 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
