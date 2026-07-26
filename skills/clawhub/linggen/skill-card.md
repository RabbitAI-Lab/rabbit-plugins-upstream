## Description: <br>
Linggen gives agents durable local memory across supported hosts and browser control through a local MCP server. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[linggen](https://clawhub.ai/user/linggen) <br>

### License/Terms of Use: <br>
Apache 2.0 <br>


## Use Case: <br>
Developers and external users use Linggen to give Claude Code, Codex, OpenClaw, Linggen, and standalone CLI workflows shared durable memory. The skill also guides controlled browser and X interactions through the user's local Linggen MCP server. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: First use may install remote binaries for the memory CLI and Linggen engine. <br>
Mitigation: Install only in environments where remote first-use installation is acceptable, and review update or install prompts before allowing the agent to proceed. <br>
Risk: Durable memory can persist personal or session-derived data across tools, and recalled memories can enter the configured LLM context. <br>
Mitigation: Avoid saving secrets, review stored memory regularly, and use delete or forget workflows for records that should not persist. <br>
Risk: Browser and X control surfaces can interact with the user's logged-in local sessions. <br>
Mitigation: Keep per-site permission prompts enabled and require explicit confirmation for payments, credentials, deletes, posting, and other sensitive actions. <br>
Risk: Backfill workflows can read local session logs before writing selected durable memories. <br>
Mitigation: Run scan and dream workflows only when intended, rely on the artifact's secret-filtering safeguards, and review resulting memory rows for sensitivity. <br>


## Reference(s): <br>
- [Linggen homepage](https://linggen.dev) <br>
- [ClawHub skill page](https://clawhub.ai/linggen/skills/linggen) <br>
- [Routing rules](references/routing-rules.md) <br>
- [Dream flow](references/dream-flow.md) <br>
- [Extractor prompt](references/extractor-prompt.md) <br>
- [Condense flow](references/condense-flow.md) <br>
- [Shared memory design](doc/shared-memory-design.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON CLI output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Local CLI and MCP workflows; list, search, and get outputs are expected to omit embedding vectors.] <br>

## Skill Version(s): <br>
2.1.0 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
