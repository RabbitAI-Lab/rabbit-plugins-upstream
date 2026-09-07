## Description:

Turn an official earnings script into one spoken earnings script read per labeled section. This earnings call voice studio writes earnings report narration and quarterly results audio from the prepared remarks the company already wrote, then records 8 to 20 earnings script voice clips. Use it for investor update voice packs that stay one section, one clip.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External teams and agents use this skill to turn already-written official earnings remarks into a planned pack of labeled speech clips. It guides pronunciation collection, clone consent checks, paid Beatra speech generation, task polling, billing reporting, and recovery without adding unsourced financial commentary.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The shared Beatra Device Token has broad media, task, artifact, voice, wallet spend, and task cancellation authority.

Mitigation: Install only in environments where that authority is acceptable, keep the token in the private credential file, and revoke the connected agent from the Beatra Console when access is no longer needed.

Risk: The bundled client checks for and installs package updates silently by default.

Mitigation: Disable automatic updates for managed or sensitive installations with `python3 scripts/mcp_client.py update --auto off`, and use `python3 scripts/mcp_client.py update --check` for explicit review.

Risk: Clone and speech operations can spend account credits and may create duplicate tasks if retried with changed arguments.

Mitigation: Use one opaque `client_request_id` per billable request, retry only byte-identical arguments under transport uncertainty, and report `billing.net_charged_credits` from the terminal task response.

Risk: Local files uploaded as clone or media samples are sent to Beatra.

Mitigation: Inspect files first, upload only content the user intentionally wants sent, and require explicit likeness and voice rights before cloning.

Risk: Earnings narration can become misleading if the agent adds unsupported financial commentary or figures.

Mitigation: Use only the supplied official script, require pronunciations for names and figures, and stop rather than invent revenue, guidance, quotes, or market takes.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/beatra-ai/skills/earnings-script-read)
- [Publisher profile](https://clawhub.ai/user/beatra-ai)
- [Beatra skill homepage](https://beatra.ai/skills/earnings-script-read)
- [Earnings script workflow](references/workflow.md)
- [Installation and authentication](references/installation-and-auth.md)
- [Installation registration](references/installation-registration.md)
- [Tasks and results](references/tasks-and-results.md)
- [Billing, errors, and recovery](references/billing-errors-and-recovery.md)
- [MCP connection](references/mcp-connection.md)
- [Automatic updates and safety](references/automatic-updates-and-safety.md)
- [Uninstall and disconnect](references/uninstall-and-disconnect.md)

## Skill Output:

**Output Type(s):** [Markdown, Shell commands, Configuration instructions, API Calls, Files, Guidance]

**Output Format:** [Markdown guidance with inline shell commands, JSON payloads, generation cards, task status, billing fields, and audio artifact references]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Plans 8 to 20 section-level speech clips from an official script and reports returned MIME type, duration, size, task IDs, and net charged credits when available.]

## Skill Version(s):

0.1.3 (source: server release evidence and manifest.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
