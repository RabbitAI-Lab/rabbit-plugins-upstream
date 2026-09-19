## Description:

Read Jobber Client Hub appointments, invoices, quotes, and work requests from a shell using the fpx CLI and a signed-in browser tab.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to fetch and parse their own customer-side Jobber Client Hub pages into JSON for command-line review and scripts. It is aimed at reading appointments, invoices, quotes, and work requests without using the Jobber MCP server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow grants fpx and the Transporter extension fetch access to getjobber.com from a signed-in Chrome tab.

Mitigation: Install only when that browser-bridged access is acceptable, keep the pairing under user control, and use the read-only fetch profile described by the skill.

Risk: A Jobber Client Hub URL functions like a credential because anyone holding it can read that hub.

Mitigation: Keep the hub URL private, store it outside committed files and shared shell history, and use separate environment variables for separate vendors.

Risk: Fetched page HTML may be saved locally during troubleshooting or scripted use.

Mitigation: Review or delete saved files such as page.html or invoice.html after use because they may contain customer portal data.

Risk: Payment, approval, and other sensitive actions should not be automated through this skill.

Mitigation: Perform payments, quote approvals, and appointment confirmations manually in the browser, consistent with the skill's read-only behavior.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/chrischall/skills/jobber-mcp)
- [Recipes](references/recipes.md)
- [Why this skill does not use Jobber's documented API](references/why-not-the-api.md)
- [Client Hub parser](references/parse-clienthub.mjs)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Code, JSON]

**Output Format:** [Markdown guidance with shell commands and a Node.js parser that emits JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only workflow; parser consumes Jobber Client Hub HTML from stdin and writes structured records to stdout.]

## Skill Version(s):

0.4.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
