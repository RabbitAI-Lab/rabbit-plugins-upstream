## Description:

Turns user-supplied customer-service macro titles and talk tracks into a four-to-eight still CS macro card set.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Support and customer-service teams use this skill through an agent to plan and generate matching still cards from already-approved macro titles and talk tracks, one card per named script.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses a shared bearer credential with broad paid-media and account capabilities.

Mitigation: Install only when those account permissions are acceptable, keep the device token out of chat and logs, avoid uploading sensitive reference files, and revoke the Beatra device authorization from the console when finished.

Risk: The bundled client silently checks for and installs package updates by default.

Mitigation: Disable automatic updates with `python3 scripts/mcp_client.py update --auto off` when manual review of executable package changes is required.

Risk: Generation calls consume Beatra credits and transport uncertainty can otherwise create duplicate paid work.

Mitigation: Confirm the live model price before billable work, use one opaque `client_request_id` per still, retry uncertain submissions only with the identical payload and original request identity, and report returned `billing.net_charged_credits`.

## Reference(s):

- [CS macro card pack workflow](references/workflow.md)
- [Installation and authentication](references/installation-and-auth.md)
- [Installation registration](references/installation-registration.md)
- [Tasks and results](references/tasks-and-results.md)
- [Billing, errors, and recovery](references/billing-errors-and-recovery.md)
- [MCP connection](references/mcp-connection.md)
- [Automatic updates and safety](references/automatic-updates-and-safety.md)
- [Uninstall and disconnect](references/uninstall-and-disconnect.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Files, Guidance]

**Output Format:** [Markdown with labeled pack lists, confirmation cards, inline shell commands, JSON payload examples, and returned image artifacts.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces one planned or generated still per named macro, normally four to eight stills, with task IDs, resolved models, dimensions, formats, and net charged credits when generation succeeds.]

## Skill Version(s):

0.1.2 (source: server release evidence and manifest.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
