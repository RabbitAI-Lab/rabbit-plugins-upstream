## Description:

Guides agents to read a customer's Jobber Client Hub from a shell with @fetchproxy/cli and parse appointments, invoices, quotes, and work requests without running the MCP server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and automation agents use this skill to fetch and summarize their own customer-side Jobber Client Hub data from a signed-in browser session. It supports read-only workflows for appointments, invoices, quotes, and work requests when the Jobber Developer API is not the correct customer-facing surface.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow grants fpx and the Transporter extension persistent authenticated read access to private Jobber Client Hub data.

Mitigation: Use a pinned reviewed @fetchproxy/cli version, restrict browser site access to clienthub.getjobber.com or getjobber.com where possible, and revoke the fpx profile or extension grant when the workflow is no longer needed.

Risk: A Jobber hub URL functions like a credential and can expose customer appointments, invoices, quotes, or work requests to anyone who has it.

Mitigation: Store hub URLs in local environment variables or other private storage, keep them out of shared shell history and repositories, and rotate or revoke access through normal Jobber account controls if exposed.

Risk: Saved HTML captures such as invoice.html can retain private customer or billing data after parsing is complete.

Mitigation: Delete local page captures after use and avoid committing or sharing captured hub HTML.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/jobber-mcp)
- [Recipes](references/recipes.md)
- [Why this skill does not use Jobber's documented API](references/why-not-the-api.md)
- [Client Hub parser](references/parse-clienthub.mjs)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON parsing examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The bundled parser reads Jobber Client Hub HTML from stdin and emits JSON records for supported page types.]

## Skill Version(s):

0.3.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
