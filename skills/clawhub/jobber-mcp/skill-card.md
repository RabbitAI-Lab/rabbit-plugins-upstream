## Description:

Read your Jobber Client Hub, the customer portal a service business uses to send appointments, quotes, and invoices, from a shell with the fpx CLI instead of running the jobber-mcp server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to read their own Jobber Client Hub data from a signed-in browser tab and turn appointment, invoice, quote, and work request pages into JSON for shell workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill relies on authenticated browser-tab fetch access to private Jobber Client Hub data, and each hub URL functions like a credential.

Mitigation: Install only if authenticated fetch access to getjobber.com is acceptable, keep hub URLs private, and store them outside committed files and shared shell history.

Risk: Expanding the fpx or Transporter permission profile beyond the documented fetch-only use could expose more browser data than the skill needs.

Mitigation: Keep the fpx profile scoped to fetch access for getjobber.com and do not add cookies, storage, DOM, downloads, or unrelated capabilities unless explicitly reviewed.

Risk: The parser reads server-rendered HTML, so Jobber markup changes can produce empty or incomplete results.

Mitigation: Treat parser empty-result warnings as a signal to verify the live page and selectors before relying on the output.

## Reference(s):

- [ClawHub jobber-mcp release page](https://clawhub.ai/chrischall/skills/jobber-mcp)
- [Recipes](references/recipes.md)
- [Why this skill does not use Jobber's documented API](references/why-not-the-api.md)
- [Jobber Client Hub parser](references/parse-clienthub.mjs)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces read-oriented command guidance and structured JSON parsing examples; the bundled parser writes JSON records to stdout.]

## Skill Version(s):

0.3.0 (source: release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
