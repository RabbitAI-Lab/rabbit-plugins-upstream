## Description:

Turns contractor-supplied project names, unit names, and handover dates into three handover sign stills, then extends accepted work into a matching completion-sign set.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External contractors, general contractors, supervisors, and their agents use this skill to plan and generate project handover sign stills from confirmed sign titles and statutory inscriptions. It also guides approvals, billing checks, task recovery, and delivery review for a matching sign set.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses a broad shared Beatra Device Token with authority for paid media generation, file uploads, task access, cancellation, and wallet spending.

Mitigation: Install only where that account-level authorization is acceptable, keep the token in the private ~/.beatra credential file, and revoke the connected agent from the Beatra Console or bundled uninstall workflow when no longer needed.

Risk: Paid image generation can spend credits, and the final billed amount may differ from the prepaid estimate.

Mitigation: Require the documented approval card before billable work, read the live model price immediately before submission, submit each approved still once with a unique client_request_id, and report billing.net_charged_credits from the completed task.

Risk: Optional uploads make selected local files available to Beatra.

Mitigation: Upload only user-approved reference files with the exact MIME type, avoid sensitive local files unless the destination trust model is acceptable, and treat uploaded scans as visual references rather than sources for missing statutory inscriptions.

Risk: The bundled client silently checks for and installs package updates by default.

Mitigation: Review this behavior before sensitive deployments and disable automatic checks with python3 scripts/mcp_client.py update --auto off when silent package updates are not acceptable.

Risk: Generated sign stills may contain unreadable or incorrect small text and should not be treated as official completion filings or legal certificates.

Mitigation: Review visible printed text against the confirmed pack list, report unreadable text as unreadable, and require a new approved correction request for changes.

## Reference(s):

- [Project handover sign workflow](references/workflow.md)
- [Installation and authentication](references/installation-and-auth.md)
- [Installation registration](references/installation-registration.md)
- [MCP connection](references/mcp-connection.md)
- [Tasks and results](references/tasks-and-results.md)
- [Billing, errors, and recovery](references/billing-errors-and-recovery.md)
- [Automatic updates and safety](references/automatic-updates-and-safety.md)
- [Uninstall and disconnect](references/uninstall-and-disconnect.md)
- [ClawHub skill page](https://clawhub.ai/beatra-ai/skills/project-handover-sign-set)
- [Publisher profile](https://clawhub.ai/user/beatra-ai)
- [Beatra skill homepage](https://beatra.ai/skills/project-handover-sign-set)
- [Beatra MCP endpoint](https://mcp.beatra.ai/mcp)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with JSON payloads and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces pack lists, approval cards, Beatra MCP calls, task status summaries, billing summaries, and generated image artifact references.]

## Skill Version(s):

0.1.2 (source: server release evidence and manifest.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
