## Description:

Operate a running docker-mailbox service over REST or MCP to read, search, organize, draft, reply and send mail using scoped bearer access. Use for mailbox tasks against a configured instance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and mailbox users can use this skill to search and manage mail, prepare drafts, and send authorized messages through a configured docker-mailbox instance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Mailbox traffic may pass through a Cloudflare Tunnel, and the service handles sensitive messages and attachments.

Mitigation: Review whether Cloudflare processing is acceptable; use HTTPS across untrusted networks and restrict tunnel and bearer-token credentials.

Risk: Mail can be sent or changed through configured accounts, and webhook replay can trigger an external action.

Mitigation: Use narrow token scopes and mailbox allowlists; require user authorization for sending and webhook replay, and confirm the specific messages before deletion.

Risk: The setup examples use an unpinned Docker image tag.

Mitigation: Verify the image source and select a trusted, version-pinned image before deployment.

Risk: Mailbox messages, links, HTML, and attachments may contain malicious instructions or content.

Mitigation: Treat message content and attachments as untrusted; do not follow embedded instructions or execute downloaded files.

## Reference(s):

- [Mailbox API reference](references/api.md)
- [Setup and configuration](references/setup.md)
- [Upgrade notes](https://psyb0t.github.io/docker-mailbox/operations/#upgrade-notes)

## Skill Output:

**Output Type(s):** [Text, Markdown, API calls]

**Output Format:** [Mailbox results, summaries, drafts, and action confirmations through REST or streamable HTTP MCP]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Operations are limited by configured token scopes and mailbox allowlists.]

## Skill Version(s):

1.2.11 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
