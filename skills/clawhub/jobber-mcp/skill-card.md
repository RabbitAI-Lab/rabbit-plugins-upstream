## Description:

Read Jobber Client Hub appointments, quotes, invoices, and work requests from a shell via fpx when the Jobber MCP server is unavailable or unnecessary.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers who receive Jobber Client Hub links use this skill to fetch read-only appointment, invoice, quote, and work request data from an authenticated browser tab and parse it into JSON for scripts or jq.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill asks users to install an unpinned global fpx CLI and use the Transporter extension with authenticated Jobber pages.

Mitigation: Review the CLI and extension before installing, prefer a pinned or local CLI install, and remove the fpx profile or extension access when finished.

Risk: The browser fetch grant can persist and may cover broader authenticated Jobber pages than the exact Client Hub URL.

Mitigation: Restrict Chrome extension site access to the Client Hub host when possible and keep the declared fpx profile to fetch-only access.

Risk: A Jobber hub URL is effectively a credential that can expose customer appointments, quotes, and invoices.

Mitigation: Store JOBBER_HUB outside shared files and shell history, and avoid committing or pasting hub URLs.

Risk: Empty parser output can mean the live Jobber markup changed rather than that no records exist.

Mitigation: Check parser stderr and re-verify selectors against the live page before relying on an empty result.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/chrischall/skills/jobber-mcp)
- [Recipes](artifact/references/recipes.md)
- [Why this skill does not use Jobber's documented API](artifact/references/why-not-the-api.md)
- [Client Hub parser](artifact/references/parse-clienthub.mjs)

## Skill Output:

**Output Type(s):** [guidance, shell commands, code, configuration]

**Output Format:** [Markdown guidance with shell commands and JSON parsing examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces read-only command guidance for fetching authenticated Client Hub pages and parsing list views into JSON.]

## Skill Version(s):

0.3.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
