## Description: <br>
Search and execute dynamic tools via QVeris API. Use when needing to find and call external APIs/tools dynamically (weather, search, data retrieval, stock trading analysis, etc.). Requires QVERIS_API_KEY environment variable. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[hqman](https://clawhub.ai/user/hqman) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and agent users use Qveris to search for external API tools by capability, review the discovered tool metadata, and execute selected tools with JSON parameters. Typical tasks include weather lookup, stock market data retrieval, web search, currency exchange, and other data API calls through QVeris. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can route broad prompts into remote tool discovery and execution through QVeris, which may send user prompts, parameters, or selected task context to an external service. <br>
Mitigation: Use a dedicated QVeris API key, avoid sending secrets or regulated personal or business data, and review the selected tool ID, provider, and parameters before execution. <br>
Risk: Auto-invocation may cause accidental external tool searches or executions for prompts that match broad stock, trading, analysis, or market trigger patterns. <br>
Mitigation: Require confirmation before execution or disable auto-invoke in environments where unintended external calls are unacceptable. <br>


## Reference(s): <br>
- [QVeris](https://qveris.ai) <br>
- [uv installation guide](https://docs.astral.sh/uv/getting-started/installation/) <br>


## Skill Output: <br>
**Output Type(s):** [text, json, shell commands, guidance] <br>
**Output Format:** [Plain text or JSON from QVeris search and execution commands, with shell command guidance in Markdown examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires QVERIS_API_KEY; remote execution responses are capped by the CLI max response size, defaulting to 20480 bytes.] <br>

## Skill Version(s): <br>
0.1.0 (source: pyproject.toml and ClawHub release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
