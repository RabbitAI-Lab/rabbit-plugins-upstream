## Description:

Unified local memory infrastructure that gives an agent long-term memory, a knowledge graph, automatic knowledge capture, semantic and timeline retrieval, memory health auditing, backups, and retained root-cause analysis, predictive maintenance, and evolution-report features.

This skill is ready for commercial/non-commercial use.

## Publisher:

[fyniujin](https://clawhub.ai/user/fyniujin)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, agent operators, and advanced users use this skill to persist local agent memory, organize remembered information into a knowledge graph, retrieve context across sessions, audit memory quality, and export or back up the resulting memory store.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill creates persistent local memory, snapshots, and backups that may retain sensitive user or project data.

Mitigation: Install only when persistent memory is intended, avoid storing secrets, and treat the memory store, snapshots, and backups as sensitive data.

Risk: The setup flow can register recurring tasks through crontab or schtasks.

Mitigation: Review the exact scheduled task before enabling setup and remove or disable it when recurring memory processing is no longer desired.

Risk: The local web UI, MCP server, and retrieval tools can expose remembered content to local clients or connected agents.

Mitigation: Run these interfaces only when needed, keep them bound to local use, and limit machine access to trusted users and agents.

Risk: Some optional paths cross the local-only boundary, including update checks, CDN-hosted web assets, external LLM adapters, tokenizer loading, model downloads, and Baidu backup integration.

Mitigation: Review and explicitly configure any networked or external adapter path before use; keep defaults local when network transfer is not acceptable.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/fyniujin/skills/zwjh-skill)
- [Publisher profile](https://clawhub.ai/user/fyniujin)
- [BAAI bge-small-zh-v1.5 ONNX model](https://huggingface.co/BAAI/bge-small-zh-v1.5/resolve/main/onnx/model_quantized.onnx)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown, plain text, JSON, Mermaid graph text, CSV, Neo4j Cypher, Obsidian or Logseq exports, and CLI status output depending on the command.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Stores and retrieves local memory data; optional backup, web UI, MCP, and external adapter flows can produce files, local service responses, or integration configuration.]

## Skill Version(s):

2.5.0 (source: frontmatter, version.json, server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
