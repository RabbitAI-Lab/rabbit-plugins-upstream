## Description:

Enables an agent to read, search, send, mark seen, and delete email across configured inboxes through docker-mailbox REST or MCP.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to manage email in configured mailboxes through a running, bearer-authenticated docker-mailbox service, including searching, composing, and confirming specific messages before deletion.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Email contents and account access could be exposed through an untrusted or publicly reachable service.

Mitigation: Connect only to a trusted mailboxd instance, bind it to localhost by default, and use HTTPS when deliberately exposing it.

Risk: Leaked bearer tokens or mailbox configuration could grant access to every configured inbox.

Mitigation: Use long bearer tokens, protect config.yaml and tunnel credentials as passwords, and use separate instances where mailbox access must be isolated.

Risk: Deleting the wrong email is permanent and cannot be undone.

Mitigation: Show the mailbox and exact message UIDs to the user, then require explicit confirmation before deleting those messages.

Risk: Unpinned Docker images can change between deployments.

Mitigation: Prefer pinned image versions or digests instead of ':latest'.

## Reference(s):

- [docker-mailbox setup guide](references/setup.md)
- [Project homepage (release metadata)](https://github.com/psyb0t/docker-mailbox)
- [ClawHub skill release](https://clawhub.ai/psyb0t/skills/docker-mailbox)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Configuration guidance]

**Output Format:** [Markdown guidance and shell examples; structured mailbox results when connected to the service]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a running mailboxd service and a configured bearer token.]

## Skill Version(s):

1.2.5 (source: ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
