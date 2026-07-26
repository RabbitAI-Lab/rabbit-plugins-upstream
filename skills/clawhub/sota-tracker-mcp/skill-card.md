## Description: <br>
Provides daily updated authoritative data and APIs tracking state-of-the-art AI models across categories from LMArena, Artificial Analysis, and HuggingFace. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[romancircus](https://clawhub.ai/user/romancircus) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and agent users use this skill to query current AI model rankings, check whether model recommendations are outdated, compare models, and retrieve hardware-aware recommendations through MCP tools, a REST API, and exported data files. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The release can influence future agent behavior by updating CLAUDE.md or agents.md files and by configuring MCP usage. <br>
Mitigation: Run update scripts manually first, review generated diffs, and back up existing agent instruction files before enabling scheduled updates. <br>
Risk: Setup examples include recurring jobs and overwrite-style configuration for files such as .mcp.json, CLAUDE.md, and agents.md. <br>
Mitigation: Review scripts and target paths before use, avoid enabling cron or systemd timers until the behavior is understood, and keep a rollback copy of affected files. <br>
Risk: The REST and MCP server surfaces depend on Python dependencies and locally exposed services. <br>
Mitigation: Pin or update dependencies before running exposed servers and restrict network exposure for local deployments. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/romancircus/skills/sota-tracker-mcp) <br>
- [LMArena](https://lmarena.ai) <br>
- [Artificial Analysis](https://artificialanalysis.ai) <br>
- [HuggingFace](https://huggingface.co) <br>
- [Open LLM Leaderboard](https://huggingface.co/spaces/open-llm-leaderboard/open_llm_leaderboard) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown and JSON-like text returned by MCP tools or REST endpoints, plus generated agent configuration content when update scripts are run.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs depend on scraped and cached third-party benchmark data, local SQLite state, and optional hardware profile settings.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata, pyproject.toml, package.json) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
