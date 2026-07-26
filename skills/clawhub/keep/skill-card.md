## Description: <br>
Reflective Memory gives agents persistent semantic memory, reflective prompts, and context retrieval across sessions. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[hughpyle](https://clawhub.ai/user/hughpyle) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent operators use this skill to give agents durable working memory, semantic search, current-intention tracking, and guided reflection before, during, and after work. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can persist conversation history and index workspace files. <br>
Mitigation: Install only when persistent agent memory is desired, review OpenClaw indexPaths and indexExclude settings, and scope watched paths to content intended for indexing. <br>
Risk: Configured remote model providers or keepnotes.ai may receive content used for embeddings, summarization, or hosted memory. <br>
Mitigation: Choose local providers when content should stay local, and configure API keys or hosted service access only for approved data. <br>
Risk: Automatic setup can add tool-configuration hooks to the workspace. <br>
Mitigation: Set KEEP_NO_SETUP when automatic tool configuration is not desired, and review generated workspace configuration before use. <br>
Risk: Dependency vulnerabilities can affect the memory system over time. <br>
Mitigation: Keep the package and dependencies updated before deployment. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/hughpyle/skills/keep) <br>
- [PyPI Package: keep-skill](https://pypi.org/project/keep-skill/) <br>
- [Keep Documentation](https://docs.keepnotes.ai/guides/) <br>
- [Quick Start](docs/QUICKSTART.md) <br>
- [MCP Integration](docs/KEEP-MCP.md) <br>
- [OpenClaw Integration](docs/OPENCLAW-INTEGRATION.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with tool-call examples, CLI commands, and structured retrieval output.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May reference locally persisted notes, indexed workspace files, and configured local or remote model providers.] <br>

## Skill Version(s): <br>
0.109.0 (source: SKILL.md frontmatter, pyproject.toml, ClawHub release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
