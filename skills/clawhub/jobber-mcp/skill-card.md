## Description:

Read Jobber Client Hub appointments, quotes, invoices, and work requests from a signed-in browser tab using fpx, returning shell-friendly JSON without running the MCP server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to retrieve their own Jobber Client Hub records into scripts or command-line workflows when the documented Jobber API is not available to them as customers.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill depends on fpx and the Transporter extension reading through a signed-in Jobber browser session.

Mitigation: Install only when comfortable granting that read path, keep the fpx profile fetch-only for getjobber.com, and review Chrome site access before use.

Risk: A Jobber Client Hub URL and saved hub HTML can expose private appointment, quote, invoice, and request data.

Mitigation: Store hub URLs in environment variables, avoid committing URLs or captured pages, and delete local page captures when no longer needed.

Risk: Wrong parser mode or changed Client Hub markup can produce empty or misleading results.

Mitigation: Check parser stderr, match the parser kind to the fetched page, and re-verify selectors before relying on an unexpected empty result.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/jobber-mcp)
- [Recipes](references/recipes.md)
- [Why this skill does not use Jobber's documented API](references/why-not-the-api.md)
- [Client Hub parser](references/parse-clienthub.mjs)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and a JavaScript parser that emits JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Parser output is structured JSON for appointments, invoices, quotes, and work requests.]

## Skill Version(s):

1.0.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
