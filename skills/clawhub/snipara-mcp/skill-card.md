## Description: <br>
Snipara MCP connects AI assistants to Snipara documentation search, memory, shared context, and multi-agent coordination tools. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[alopez3006](https://clawhub.ai/user/alopez3006) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and agent users use the skill to query indexed project documentation, retrieve relevant context, store and recall working preferences or decisions, and coordinate shared agent work through Snipara-backed tools. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Selected queries, session context, memories, summaries, and uploaded documents may be sent to Snipara. <br>
Mitigation: Use a scoped project or API key and avoid sending secrets, regulated data, or unapproved proprietary content. <br>
Risk: Persistent memory and shared collections can retain sensitive or stale working context. <br>
Mitigation: Do not store secrets in memory or uploads, and periodically review and delete memories and shared documents. <br>
Risk: Document sync, summary deletion, memory deletion, and shared collection upload tools can change or remove stored context. <br>
Mitigation: Require explicit operator approval for delete or bulk sync actions, especially when delete_missing is enabled. <br>
Risk: Swarm tools can modify shared coordination state across agents. <br>
Mitigation: Limit swarm use to trusted projects and agents, and review shared state, tasks, and broadcasts before acting on them. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/alopez3006/skills/snipara-mcp) <br>
- [Snipara Documentation](https://docs.snipara.com) <br>
- [Snipara Website](https://snipara.com) <br>
- [PyPI Package](https://pypi.org/project/snipara-mcp/) <br>
- [Model Context Protocol](https://modelcontextprotocol.io/) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, configuration, guidance] <br>
**Output Format:** [Plain text or Markdown responses from MCP tool calls, with JSON-like tool input parameters.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires Snipara project credentials; outputs may include document excerpts, summaries, memory records, upload status, and swarm coordination status.] <br>

## Skill Version(s): <br>
0.1.0 (source: ClawHub release evidence; artifact pyproject.toml reports 2.2.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
