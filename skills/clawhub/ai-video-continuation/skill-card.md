## Description:

AI Video Continuation helps an agent extend one short source video before or after its existing action by building a continuity state, selecting the next visual beat, using Beatra video-extension tools, and reviewing the returned clip for continuity.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators, marketers, product teams, and agents use this skill when they already have one source clip and need a natural lead-in, longer hold, reveal completion, action continuation, or ending extension. The workflow plans the extension against live model constraints, submits one paid Beatra task after approval, and reports returned artifacts, billing, and continuity review notes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The package uses a shared Beatra device token with broader Beatra account authority than video continuation alone requires.

Mitigation: Install only after reviewing Beatra account access, keep the credential file private, and disconnect or uninstall when the package is no longer needed.

Risk: Silent package updates are enabled by default before ordinary Beatra commands.

Mitigation: Disable silent updates with `python3 scripts/mcp_client.py update --auto off` or run `python3 scripts/mcp_client.py update --check` before use when change control is required.

Risk: Video extension is paid work, and duplicate submissions can create duplicate chargeable tasks.

Mitigation: Use one stable client_request_id per approved request, submit the paid extension exactly once, and recover uncertain responses by polling or retrying only the identical frozen payload.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/beatra-ai/skills/ai-video-continuation)
- [Beatra Skill Homepage](https://beatra.ai/skills/ai-video-continuation)
- [Video continuation workflow](references/workflow.md)
- [Tasks and results](references/tasks-and-results.md)
- [Billing, errors, and recovery](references/billing-errors-and-recovery.md)
- [Automatic updates and safety](references/automatic-updates-and-safety.md)
- [Installation and authentication](references/installation-and-auth.md)
- [Bundled MCP Client diagnostics](references/mcp-connection.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell command snippets and JSON MCP payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include Beatra task IDs, returned video artifact links, resolved model details, usage, billing.net_charged_credits, and continuity review notes.]

## Skill Version(s):

0.1.6 (source: server evidence release.version and artifact manifest)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
