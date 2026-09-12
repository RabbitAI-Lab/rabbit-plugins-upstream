## Description:

Turns approved comic panels, manga frames, character sheets, or story beats into dynamic motion-comic shots using Beatra image and video generation workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External creators and agents use this skill to turn approved comic panels, character sheets, manga or webtoon frames, and frozen story beats into motion-comic video shots. The skill guides route selection, source-media inspection, user approval for paid work, task recovery, and review of returned Beatra artifacts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requests broad Beatra account and media privileges and stores a shared bearer token under ~/.beatra.

Mitigation: Install only in trusted agent environments, protect ~/.beatra as private user state, never expose the token in chat or logs, and revoke the Beatra device authorization when access is no longer needed.

Risk: The bundled client silently replaces package files during automatic updates by default.

Mitigation: Review before use in sensitive environments and disable silent updates with the documented update command when change control is required.

Risk: The workflow uploads user-selected media and can make billable generation calls.

Mitigation: Inspect media before upload, require an explicit admission and approval step before paid work, use stable request IDs for recovery, and report only returned billing facts.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/beatra-ai/skills/ai-comic-drama-shot-maker)
- [Beatra Skill Homepage](https://beatra.ai/skills/ai-comic-drama-shot-maker)
- [Beatra MCP Endpoint](https://mcp.beatra.ai/mcp)
- [Comic-drama shot workflow](references/workflow.md)
- [Installation and authentication](references/installation-and-auth.md)
- [Installation registration](references/installation-registration.md)
- [Tasks and results](references/tasks-and-results.md)
- [Billing, errors, and recovery](references/billing-errors-and-recovery.md)
- [Bundled MCP Client diagnostics](references/mcp-connection.md)
- [Automatic updates and safety](references/automatic-updates-and-safety.md)
- [Uninstall and disconnect](references/uninstall-and-disconnect.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can guide Beatra MCP calls that return task IDs, artifact links, usage, and billing details after user approval.]

## Skill Version(s):

0.1.6 (source: server release evidence and manifest.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
