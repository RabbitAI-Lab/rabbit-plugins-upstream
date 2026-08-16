## Description:

Linggen gives agents durable cross-session memory and local browser/X control through ling-mem and Linggen services.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linggen](https://clawhub.ai/user/linggen)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use Linggen to let assistants recall durable user facts across sessions, manage memory records, and operate local browser/X integrations with user permissions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Remote installer scripts run on the user's machine during setup.

Mitigation: Review or manually pin installers before use, and install only from trusted Linggen release channels.

Risk: Durable local memories and recalled facts may be sent to the user's configured LLM as prompt context.

Mitigation: Avoid storing secrets or sensitive facts, review saved memories regularly, and delete records that should not be recalled.

Risk: Optional transcript backfill can read local agent session history into the memory workflow.

Mitigation: Disable scan/backfill workflows when transcript reuse is not desired and rely on explicit memory adds instead.

Risk: Browser and X controls can interact with logged-in sessions on the user's machine.

Mitigation: Use browser permission prompts, keep actions visible to the user, and disable browser/X integrations when not needed.

## Reference(s):

- [Linggen homepage](https://linggen.dev)
- [README](README.md)
- [Shared memory design](doc/shared-memory-design.md)
- [Routing rules](references/routing-rules.md)
- [Dream flow](references/dream-flow.md)
- [Condense flow](references/condense-flow.md)
- [Extractor prompt](references/extractor-prompt.md)
- [Linggen memory source and binary releases](https://github.com/linggen/linggen-memory)
- [Skill source](https://github.com/linggen/skills/tree/main/linggen)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON CLI output when listing or searching memory]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May invoke local CLI or MCP tools, write durable local memory rows, and surface recalled facts in agent responses.]

## Skill Version(s):

2.3.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
