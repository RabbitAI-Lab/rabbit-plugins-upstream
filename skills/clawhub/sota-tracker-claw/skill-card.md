## Description: <br>
Provides daily updated rankings and metadata for state-of-the-art AI models from public benchmark and model sources through static files, local queries, a REST API, or an optional MCP server. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[romancircus](https://clawhub.ai/user/romancircus) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and agent users use this skill to retrieve current AI model rankings, compare models, check whether models are outdated, and generate concise SOTA guidance for agent instruction files. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can persistently change local agent instruction files and MCP configuration files when its update scripts are enabled. <br>
Mitigation: Run update scripts manually first, back up agents.md, CLAUDE.md, and .mcp.json, and review diffs before enabling cron or systemd automation. <br>
Risk: The REST or MCP server can expose model-ranking data and local service behavior if made reachable beyond localhost. <br>
Mitigation: Pin or upgrade dependencies before deployment and keep REST or MCP access limited to localhost or trusted networks unless production controls are added. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/romancircus/skills/sota-tracker-claw) <br>
- [LMArena](https://lmarena.ai) <br>
- [Artificial Analysis](https://artificialanalysis.ai) <br>
- [Hugging Face](https://huggingface.co) <br>
- [Open LLM Leaderboard](https://huggingface.co/spaces/open-llm-leaderboard/open_llm_leaderboard) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown and plain text with JSON, CSV, SQLite, REST API, and MCP interaction patterns described in code and shell command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May write generated SOTA summaries into local agent instruction files when the update script is run.] <br>

## Skill Version(s): <br>
1.0.1 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
