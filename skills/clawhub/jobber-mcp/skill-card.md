## Description:

Read your Jobber Client Hub, the customer portal a service business uses to send you appointments, quotes and invoices, from a shell with the fpx CLI instead of running the jobber-mcp server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to retrieve their own Jobber Client Hub appointments, invoices, quotes, and work requests through a browser-backed fpx fetch flow when the Jobber MCP server is unavailable or unnecessary.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill relies on a browser bridge and extension to fetch Jobber Client Hub pages.

Mitigation: Install it only when you trust the fpx CLI and Transporter extension, and keep extension site access scoped as narrowly as possible.

Risk: A Jobber Client Hub URL can grant access to customer portal data.

Mitigation: Treat each hub URL like a password, store it outside committed files, and avoid sharing shell history or saved exports that contain it.

Risk: Persisted browser bridge pairing can continue to authorize fetches after setup.

Mitigation: Revoke fpx pairing or extension access when the skill is no longer needed.

## Reference(s):

- [Recipes](references/recipes.md)
- [Why this skill does not use Jobber's documented API](references/why-not-the-api.md)
- [Parser script](references/parse-clienthub.mjs)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/jobber-mcp)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Code, Configuration]

**Output Format:** [Markdown guidance with shell commands and JSON parser output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The included parser emits structured JSON records for supported Jobber Client Hub pages.]

## Skill Version(s):

0.3.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
