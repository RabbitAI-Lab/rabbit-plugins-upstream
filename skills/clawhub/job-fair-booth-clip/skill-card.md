## Description:

Turn authorized stills and already-written job-fair role notes into one booth talking clip per still.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Recruiters, founders, and campus hiring teams use this skill to turn authorized booth stills and confirmed job-fair role notes into short, separate talking clips for recruiting booths or campus job fairs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses a persistent Beatra device token with broad account capabilities, including spending credits and accessing Beatra artifacts and tasks beyond this single workflow.

Mitigation: Install only when the user trusts Beatra for that account access, keep the token private, and require explicit approval before unrelated Beatra tool calls or paid work.

Risk: The bundled client can silently replace package files through automatic updates.

Mitigation: Review the package before installation and consider disabling silent updates with `python3 scripts/mcp_client.py update --auto off` before use.

Risk: Paid clone, speech, and video calls can spend credits and may be duplicated if uncertain responses are replayed with changed arguments.

Mitigation: Show a cost and work confirmation before each paid stage, use one opaque `client_request_id` per logical request, and retry only byte-identical requests with the same identity.

## Reference(s):

- [Job-fair booth talking-clip workflow](references/workflow.md)
- [Installation and authentication](references/installation-and-auth.md)
- [Installation registration](references/installation-registration.md)
- [MCP connection](references/mcp-connection.md)
- [Tasks and results](references/tasks-and-results.md)
- [Billing, errors, and recovery](references/billing-errors-and-recovery.md)
- [Automatic updates and safety](references/automatic-updates-and-safety.md)
- [Uninstall and disconnect](references/uninstall-and-disconnect.md)
- [Beatra MCP endpoint](https://mcp.beatra.ai/mcp)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline JSON and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces a free labeled clip plan before paid clone, speech, or video generation; final media artifacts are created by Beatra tasks.]

## Skill Version(s):

0.1.2 (source: server release evidence and manifest.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
