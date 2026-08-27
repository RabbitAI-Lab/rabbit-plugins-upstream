## Description:

Turn a written incident briefing script into one incident brief voice clip per labeled cue.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Operations and safety desk teams use this skill to convert a written incident briefing script into a labeled pack of short spoken clips. It helps plan, confirm, generate, poll, review, and recover Beatra text-to-speech or voice-clone work without adding facts beyond the supplied brief.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The server security summary says the package grants and uses broad Beatra account authority, shared credentials, and paid Beatra operations.

Mitigation: Install only after reviewing the Beatra scopes, protect the shared credential file, and revoke or reconnect through the documented authorization flow when access should change.

Risk: The server security guidance calls out silent package updates enabled by default.

Mitigation: Use the documented update controls, including `python3 scripts/mcp_client.py update --auto off`, when the environment requires explicit change control.

Risk: Paid speech or clone requests can be duplicated if a response is uncertain and the request is replayed with changed arguments.

Mitigation: Use one opaque `client_request_id` per paid operation, retry only byte-identical uncertain requests with the same identity, and poll existing tasks before submitting replacements.

Risk: Voice cloning can create likeness or consent risk when a staff voice is requested.

Mitigation: Require explicit likeness and voice rights, inspect only authorized samples, and treat file access as insufficient consent.

Risk: Incident brief audio can mislead listeners if it adds cause, blame, outcome, or status details not present in the source briefing.

Mitigation: Read only the supplied briefing script, collect pronunciations for names, and keep each clip line grounded in the written brief.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/beatra-ai/skills/incident-brief-voice)
- [Beatra Skill Homepage](https://beatra.ai/skills/incident-brief-voice)
- [Incident brief voice workflow](references/workflow.md)
- [Installation and authentication](references/installation-and-auth.md)
- [Installation registration](references/installation-registration.md)
- [MCP connection](references/mcp-connection.md)
- [Tasks and results](references/tasks-and-results.md)
- [Billing, errors, and recovery](references/billing-errors-and-recovery.md)
- [Automatic updates and safety](references/automatic-updates-and-safety.md)
- [Uninstall and disconnect](references/uninstall-and-disconnect.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, files, guidance]

**Output Format:** [Markdown guidance with JSON payloads and shell commands; generated audio clips are returned as Beatra task artifacts.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Plans 8 to 20 labeled speech slots, uses one request identity per paid operation, and reports returned task IDs, audio metadata, usage, and net charged credits.]

## Skill Version(s):

0.1.1 (source: server release evidence and package manifest)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
