## Description:

Turn a coworking or daytime office brief into one office background music playlist of 8 to 15 low-stimulation instrumentals.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External workspace operators and agents use this skill to plan and generate reusable daytime background music packs for coworking floors, offices, and daytime cafe work areas. It produces a labeled low-stimulation instrumental track list before any paid generation and guides approved generation, task polling, billing checks, and recovery.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses a shared broad Beatra device credential.

Mitigation: Install only when the user trusts Beatra for the granted scope, keep credentials in the private Beatra state directory, and use the bundled uninstall flow or Beatra Console revocation when access should end.

Risk: Silent package updates are enabled by default.

Mitigation: Disable automatic updates with `python3 scripts/mcp_client.py update --auto off` when review-before-update is required, and use `--check` to inspect available updates.

Risk: The bundled client can upload local files when invoked.

Mitigation: Avoid upload paths unless the user explicitly needs them, confirm the file and purpose before upload, and do not place sensitive local content in tool inputs.

Risk: Paid music generation can create billing or duplicate-submission risk if retried incorrectly.

Mitigation: Show the live model price before paid generation, use one opaque `client_request_id` per slot, poll returned tasks, and retry only byte-identical uncertain requests with the same request identity.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/beatra-ai/skills/coworking-day-pack)
- [Beatra skill homepage](https://beatra.ai/skills/coworking-day-pack)
- [Daytime playlist workflow](references/workflow.md)
- [Installation and authentication](references/installation-and-auth.md)
- [Installation registration](references/installation-registration.md)
- [Tasks and results](references/tasks-and-results.md)
- [Billing, errors, and recovery](references/billing-errors-and-recovery.md)
- [MCP connection](references/mcp-connection.md)
- [Automatic updates and safety](references/automatic-updates-and-safety.md)
- [Uninstall and disconnect](references/uninstall-and-disconnect.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with playlist plans, confirmation summaries, command examples, and task-result guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include generated media artifact references, actual durations, and billing fields returned by Beatra tasks.]

## Skill Version(s):

0.1.2 (source: release evidence and manifest.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
