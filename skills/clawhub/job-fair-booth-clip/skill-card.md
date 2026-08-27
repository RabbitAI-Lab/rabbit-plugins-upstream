## Description:

Turn authorized stills and already-written job-fair role notes into one booth talking clip per still.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Recruiters and hiring teams use this skill to turn authorized booth photos or portraits plus already-written role notes into short campus recruiting booth talking clips. It helps an agent plan clip lists, confirm billable clone, speech, and video stages, and deliver one generated clip per approved still.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses a shared persistent Beatra authorization that can access multiple media and task tools.

Mitigation: Install only when the publisher and Beatra connection are trusted, keep the token out of chat and logs, and revoke the device from Beatra Console when the connection is no longer needed.

Risk: The bundled client checks for and installs package updates silently by default.

Mitigation: Disable automatic update checks with `python3 scripts/mcp_client.py update --auto off` when silent package changes are not acceptable.

Risk: Clone, speech, and video generation are billable and can create duplicate charges if retried incorrectly.

Mitigation: Require a separate confirmation card for each paid stage, use one opaque `client_request_id` per logical request, and retry only byte-identical arguments with the same request identity after transport uncertainty.

Risk: The workflow can involve likeness, voice, and recruiting facts that require permission and accuracy.

Mitigation: Use only authorized stills and voice samples, treat file access as insufficient consent, and avoid inventing salaries, booth numbers, headcount, workplace facts, or faces.

Risk: Generated booth clips may have imperfect speech clarity, identity preservation, or mouth timing.

Mitigation: Review each terminal result visually and audibly, report only observable quality, and avoid promising perfect lip sync or unsupported editing steps.

## Reference(s):

- [Job-fair booth talking workflow](references/workflow.md)
- [Installation and authentication](references/installation-and-auth.md)
- [Installation registration](references/installation-registration.md)
- [MCP connection](references/mcp-connection.md)
- [Tasks and results](references/tasks-and-results.md)
- [Billing, errors, and recovery](references/billing-errors-and-recovery.md)
- [Automatic updates and safety](references/automatic-updates-and-safety.md)
- [Uninstall and disconnect](references/uninstall-and-disconnect.md)
- [ClawHub skill page](https://clawhub.ai/beatra-ai/skills/job-fair-booth-clip)
- [Beatra skill homepage](https://beatra.ai/skills/job-fair-booth-clip)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON request examples; completed generation tasks may return audio or video artifact files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Plans 2 to 8 clips, confirms paid stages separately, uses 2 to 15 second video segments, and reports task outputs with MIME, duration, size, and net charged credits when available.]

## Skill Version(s):

0.1.1 (source: server release evidence and manifest.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
