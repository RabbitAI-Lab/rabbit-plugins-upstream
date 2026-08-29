## Description:

Turns user-supplied fund factsheet points into one still per page for prospectus and factsheet layouts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to plan and generate page-by-page fund factsheet or prospectus stills from facts the user has already approved. It is designed for Beatra image-generation workflows that require explicit confirmation before billable generation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill stores a shared Beatra Device Token under ~/.beatra and requests broad Beatra media, wallet, task, and artifact scopes.

Mitigation: Install only where this shared authorization model is acceptable, keep token files private, and use the bundled authorization and uninstall flows to reconnect or retire the device connection.

Risk: The bundled client performs verified automatic package updates by default.

Mitigation: Review organizational policy for managed or regulated environments and disable automatic updates with python3 scripts/mcp_client.py update --auto off when silent updates are not acceptable.

Risk: Generation work is billable and retrying changed or uncertain requests can create duplicate paid tasks.

Mitigation: Show the production card before billable calls, use one opaque client_request_id per approved page, and retry only identical payloads with the same request identity after transport uncertainty.

Risk: Generated small text in fund page stills may be unreadable or misleading if treated as certified disclosure.

Mitigation: Review visible printed lines against the confirmed page list and report unreadable small type as a review item rather than a certified disclosure.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/beatra-ai/skills/fund-page-set)
- [Publisher profile](https://clawhub.ai/user/beatra-ai)
- [Fund-page workflow](references/workflow.md)
- [Installation and authentication](references/installation-and-auth.md)
- [Billing, errors, and recovery](references/billing-errors-and-recovery.md)
- [Tasks and results](references/tasks-and-results.md)
- [MCP connection](references/mcp-connection.md)
- [Automatic updates and safety](references/automatic-updates-and-safety.md)
- [Uninstall and disconnect](references/uninstall-and-disconnect.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration, API Calls]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces a free labeled page plan first, then Beatra task outputs, generated still files, task IDs, resolved model details, dimensions, formats, and net charged credits after approved generation.]

## Skill Version(s):

0.1.1 (source: server release evidence and packaged manifest)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
