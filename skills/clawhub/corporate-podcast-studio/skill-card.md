## Description:

Turn executive talking points or company column copy into a serialized corporate podcast with one consistent host voice.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Employees, external communications teams, and agents use this skill to turn approved executive talking points or company column copy into branded serialized podcast episodes while managing host voice selection, pronunciation review, paid task submission, and recovery.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requests a shared Beatra device token with broad media-generation and spending authority.

Mitigation: Review the authorization before installing, keep the token only in the private Beatra credential file, and revoke the connected agent from Beatra if the package is no longer trusted.

Risk: The bundled client performs silent package update checks and may install a newer package release automatically.

Mitigation: Use `python3 scripts/mcp_client.py update --auto off` to disable silent updates for the installation, or `python3 scripts/mcp_client.py update --check` to inspect the available version.

Risk: Paid voice cloning and speech synthesis can create duplicate or unexpected charges if uncertain requests are resubmitted with changed inputs.

Mitigation: Confirm estimates before paid work, submit each frozen payload once with one opaque `client_request_id`, and recover uncertain responses only with the identical payload and request identity.

Risk: Voice cloning can misuse a speaker sample if consent is assumed from file access alone.

Mitigation: Clone a host voice only after the user explicitly attests that the speaker authorized this cloning use, and otherwise select a catalog voice.

## Reference(s):

- [Corporate podcast workflow](references/workflow.md)
- [Installation and authentication](references/installation-and-auth.md)
- [Installation registration](references/installation-registration.md)
- [Tasks and results](references/tasks-and-results.md)
- [Billing, errors, and recovery](references/billing-errors-and-recovery.md)
- [MCP connection](references/mcp-connection.md)
- [Automatic updates and safety](references/automatic-updates-and-safety.md)
- [Uninstall and disconnect](references/uninstall-and-disconnect.md)
- [ClawHub skill page](https://clawhub.ai/beatra-ai/skills/corporate-podcast-studio)
- [Beatra skill homepage](https://beatra.ai/skills/corporate-podcast-studio)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, JSON, Audio artifact references]

**Output Format:** [Markdown guidance with inline shell commands and JSON tool payloads; final results include labeled audio artifacts, duration, usage, and billing details.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses asynchronous Beatra tasks for paid voice cloning or speech synthesis and reports returned task status, usage, and billing fields.]

## Skill Version(s):

0.1.1 (source: evidence release, artifact manifest, and bundled script constants)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
