## Description:

Turns confirmed shop booking facts into labeled booking-confirmation voice clips for confirmed, rescheduled, canceled, and related appointment notices.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External shop staff and agents use this skill to plan and produce short labeled voice clips from already-confirmed booking facts, including confirmation, reschedule, cancellation, reminder, and related notices. The skill is intended for booking voice packs where each notice stays one line and one clip.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses a shared Beatra device authorization that can access more than speech tools.

Mitigation: Review the authorization before installation, protect the local credential file, and revoke the device from the Beatra Console or documented uninstall flow when no longer needed.

Risk: The bundled client can check for and install silent automatic updates.

Mitigation: Use scripts/mcp_client.py update --auto off when silent updates are not acceptable; the documented updater verifies discovery data, archives, manifests, and packaged files.

Risk: Paid voice clone and speech tasks can consume Beatra credits.

Mitigation: Review the live pricing card before each paid stage, use one client_request_id per logical request, and avoid resubmitting changed work under the same identity.

Risk: Voice cloning can involve likeness or voice rights.

Mitigation: Use only authorized samples and require explicit rights confirmation before uploading or cloning a voice.

## Reference(s):

- [Booking confirmation workflow](references/workflow.md)
- [Installation and authentication](references/installation-and-auth.md)
- [Installation registration](references/installation-registration.md)
- [Tasks and results](references/tasks-and-results.md)
- [Billing, errors, and recovery](references/billing-errors-and-recovery.md)
- [MCP connection](references/mcp-connection.md)
- [Automatic updates and safety](references/automatic-updates-and-safety.md)
- [Uninstall and disconnect](references/uninstall-and-disconnect.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, audio]

**Output Format:** [Markdown guidance with JSON payload examples and generated MP3 audio artifacts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces 8 to 20 labeled booking notice clips; paid clone and speech work uses Beatra task polling and reported billing fields.]

## Skill Version(s):

0.1.2 (source: evidence release and artifact manifest)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
