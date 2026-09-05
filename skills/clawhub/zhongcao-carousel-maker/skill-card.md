## Description:

Creates ordered 3:4 Xiaohongshu or REDnote carousel image sequences from outlines, product details, photo sets, or style references, with optional paid Xiaohongshu lookup for topic, note, comment, and account research.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, marketers, and agents use this skill to plan, generate, refine, and deliver connected Xiaohongshu or REDnote carousel posts with a hook cover and coherent supporting slides. It can also run user-approved paid Xiaohongshu lookups before generation when live platform evidence is needed.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requests broad shared Beatra account authority for media, billing, upload, model, and task operations.

Mitigation: Review the requested Beatra authorization before installing and authorize only if those shared capabilities are acceptable for the target environment.

Risk: The bundled client enables silent local package update checks by default.

Mitigation: Disable automatic updates with `python3 scripts/mcp_client.py update --auto off` when strict change control is required.

Risk: Image generation and optional Xiaohongshu lookups are paid operations and careless retries can create duplicate or changed billable work.

Mitigation: Require explicit confirmation before each paid call, preserve the original request identity during uncertain delivery, and use task lookup before retrying.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/beatra-ai/skills/zhongcao-carousel-maker)
- [Beatra skill homepage](https://beatra.ai/skills/zhongcao-carousel-maker)
- [Workflow](references/workflow.md)
- [Reading Xiaohongshu](references/note-lookup.md)
- [Installation and authentication](references/installation-and-auth.md)
- [MCP connection](references/mcp-connection.md)
- [Billing, errors, and recovery](references/billing-errors-and-recovery.md)
- [Tasks and results](references/tasks-and-results.md)
- [Automatic updates and safety](references/automatic-updates-and-safety.md)
- [Installation registration](references/installation-registration.md)
- [Uninstall and disconnect](references/uninstall-and-disconnect.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands, Beatra task status, artifact links, billing fields, and focused revision plans]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include ordered 3:4 carousel image artifact links and task metadata after explicit approval for paid Beatra calls.]

## Skill Version(s):

0.1.3 (source: server release evidence and manifest.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
