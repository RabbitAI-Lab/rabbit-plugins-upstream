## Description:

Turns executive talking points or company column copy into serialized corporate podcast episodes with a consistent host voice.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Employees and external communications teams use this skill to turn approved executive talking points, leadership columns, or company copy into labeled podcast episodes that keep one host voice across a series.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The package uses a shared Beatra device credential with broad media, artifact, wallet, and task authority.

Mitigation: Install only when that authorization is acceptable, keep the credential local, and reconnect or revoke access through the documented authorization and uninstall flows.

Risk: Executable package files may self-update silently by default before ordinary Beatra commands.

Mitigation: Disable silent update checks with `python3 scripts/mcp_client.py update --auto off` or manually check updates before use.

Risk: Voice cloning can misuse a speaker sample if consent is unclear.

Mitigation: Upload a host sample only after the user states that the voice is theirs or that the speaker authorized this cloning use.

Risk: Paid clone or synthesis requests can create avoidable duplicate charges if uncertain responses are resubmitted with changed payloads.

Mitigation: Use one opaque `client_request_id` per frozen billable payload, poll existing tasks, and retry only the identical payload when delivery is uncertain.

## Reference(s):

- [Corporate Podcast Studio on ClawHub](https://clawhub.ai/beatra-ai/skills/corporate-podcast-studio)
- [Beatra Skill Homepage](https://beatra.ai/skills/corporate-podcast-studio)
- [Corporate podcast workflow](references/workflow.md)
- [Tasks and results](references/tasks-and-results.md)
- [Billing, errors, and recovery](references/billing-errors-and-recovery.md)
- [Installation and authentication](references/installation-and-auth.md)
- [MCP connection](references/mcp-connection.md)
- [Automatic updates and safety](references/automatic-updates-and-safety.md)
- [Uninstall and disconnect](references/uninstall-and-disconnect.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline JSON and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guides Beatra voice selection, optional voice cloning, text-to-speech synthesis, polling, billing review, and recovery.]

## Skill Version(s):

0.1.2 (source: manifest.json and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
