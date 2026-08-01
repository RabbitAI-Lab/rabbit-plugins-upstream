## Description: <br>
Linggen gives agents durable cross-host memory and browser control through a local MCP server, using a three-tier memory model and the same ling-mem store across Claude Code, Codex, and OpenClaw. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[linggen](https://clawhub.ai/user/linggen) <br>

### License/Terms of Use: <br>
Apache-2.0 <br>


## Use Case: <br>
Developers and external agent users use Linggen to give compatible agents persistent local memory, semantic recall, memory maintenance workflows, and controlled browser or X-session access across sessions and hosts. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill persists personal facts and session-derived memory that can later be injected into agent prompts. <br>
Mitigation: Review stored memory regularly and use the documented delete or forget controls for sensitive, stale, or unwanted rows. <br>
Risk: The skill can automatically install local binaries and run a daemon. <br>
Mitigation: Install only in environments where curl-to-bash dependency installation and local daemon execution are acceptable. <br>
Risk: Browser and X-session control can expose visible logged-in sessions to agent actions. <br>
Mitigation: Use per-site permission prompts and avoid enabling browser control around sensitive sites or accounts. <br>


## Reference(s): <br>
- [Linggen homepage](https://linggen.dev) <br>
- [ClawHub skill page](https://clawhub.ai/linggen/skills/linggen) <br>
- [README](README.md) <br>
- [Shared-memory design](doc/shared-memory-design.md) <br>
- [Dream flow](references/dream-flow.md) <br>
- [Routing rules](references/routing-rules.md) <br>
- [Condense flow](references/condense-flow.md) <br>
- [Extractor prompt](references/extractor-prompt.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell commands and JSON CLI output examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Guides agents to produce memory operations, recall summaries, status reports, and maintenance actions for a local memory store.] <br>

## Skill Version(s): <br>
2.2.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
