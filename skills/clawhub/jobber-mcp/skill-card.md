## Description:

Read your Jobber Client Hub from a shell with the fpx CLI, parse appointments, invoices, quotes, and work requests into JSON, and use that data without running the jobber-mcp server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and technically comfortable Jobber Client Hub customers use this skill to fetch their own hub pages through a signed-in browser tab and convert appointments, invoices, quotes, and work requests into JSON for shell scripts or jq workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The Jobber hub URL and fetched outputs can expose private customer, billing, invoice, quote, and appointment data.

Mitigation: Keep the hub URL out of committed files and shared shell history, store saved HTML or JSON securely, and treat parsed outputs as private data.

Risk: Using this skill grants fpx/Transporter fetch access to getjobber.com from a signed-in browser tab.

Mitigation: Install only when that access is acceptable, scope the fpx profile to getjobber.com, and revoke or remove the profile or extension access when finished.

Risk: Empty parser output can mean either no records or changed page markup, depending on whether the parser emitted a warning.

Mitigation: Check stderr warnings and re-verify selectors against the live page before trusting unexpected empty results.

Risk: The skill is read-only and cannot safely automate payments, approvals, quote responses, work requests, PDFs, or file downloads.

Mitigation: Use the browser-based Jobber Client Hub directly for payments, approvals, form submissions, and downloads.

## Reference(s):

- [Skill Page](https://clawhub.ai/chrischall/skills/jobber-mcp)
- [Parser Script](references/parse-clienthub.mjs)
- [Recipes](references/recipes.md)
- [Why this skill does not use Jobber's documented API](references/why-not-the-api.md)
- [Jobber Client Hub](https://clienthub.getjobber.com)
- [Jobber GraphQL API endpoint](https://api.getjobber.com/api/graphql)

## Skill Output:

**Output Type(s):** [guidance, shell commands, code, configuration, text]

**Output Format:** [Markdown guidance with shell commands and a JavaScript parser that emits JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Parser output is JSON records for appointments, invoices, quotes, and work requests; saved hub HTML or parsed JSON can contain private customer, billing, and schedule data.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
