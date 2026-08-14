## Description:

Read a customer's Jobber Client Hub appointments, invoices, quotes, and work requests from a shell by using the fpx CLI with an existing signed-in browser session, instead of running the jobber-mcp server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to fetch and parse their own Jobber Client Hub pages into JSON for shell workflows, reporting, and jq-based queries. It is intended for read-only access to customer portal data when the Jobber Developer API is not usable for that customer-side view.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Hub URLs, fetched HTML, and parsed invoice data may expose private customer information.

Mitigation: Keep hub URLs in private environment variables, avoid committing captures or command history that contains them, and delete local page captures such as invoice.html when they are no longer needed.

Risk: The workflow depends on fpx and the Transporter browser extension fetching pages through an existing signed-in Jobber Client Hub tab.

Mitigation: Install only if that browser-bridge access pattern is acceptable, keep Chrome signed into the intended hub, and check fpx health or parser exit codes before trusting an empty result.

Risk: Client Hub markup changes or using the wrong parser kind can produce empty or misleading results.

Mitigation: Treat parser warnings as review signals, match the parser kind to the page being fetched, and re-check the live page before relying on empty output.

Risk: The skill is designed for read-only access and does not support payments, quote approval, appointment confirmation, form submission, or PDF downloads.

Mitigation: Open the Jobber Client Hub manually for payment or approval workflows and for files that require browser navigation.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/jobber-mcp)
- [Recipes](references/recipes.md)
- [Why this skill does not use Jobber's documented API](references/why-not-the-api.md)
- [Parser source](references/parse-clienthub.mjs)
- [Jobber Client Hub](https://clienthub.getjobber.com)
- [Jobber GraphQL API endpoint](https://api.getjobber.com/api/graphql)
- [Jobber OAuth token endpoint](https://api.getjobber.com/api/oauth/token)
- [Jobber OAuth authorization endpoint](https://api.getjobber.com/api/oauth/authorize)

## Skill Output:

**Output Type(s):** [guidance, shell commands, code, configuration, JSON]

**Output Format:** [Markdown guidance with shell commands and a bundled JavaScript parser that emits JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only workflows; parser reads HTML from stdin and writes structured records for appointments, invoices, quotes, or work requests.]

## Skill Version(s):

0.1.0 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
