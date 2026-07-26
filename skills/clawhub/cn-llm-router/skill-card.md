## Description: <br>
Routes prompts across 12 Chinese LLM providers through one command-line interface, with task-aware model selection, cost tracking, local caching, hardware-aware limits, streaming output, and offline mock routing. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[fyniujin](https://clawhub.ai/user/fyniujin) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and technical users use this skill to choose, call, and compare Chinese LLM providers from a single CLI while tracking cost and avoiding unnecessary local resource use. It supports route planning without API keys and real chat calls when users configure provider credentials. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Provider API keys are read from environment variables, and chat prompts are sent to the selected model provider during real calls. <br>
Mitigation: Configure only trusted providers, protect shell environments and terminal history, and avoid sending sensitive prompts unless the selected provider is approved for that data. <br>
Risk: Local semantic caching can retain prompt and response text and may return a stale or overly similar cached answer. <br>
Mitigation: Use --no-cache for sensitive, real-time, financial, code-generation, or other high-impact prompts, and clear the cache when retained local text is no longer needed. <br>
Risk: Optional webhook and update URLs can send data to user-configured destinations. <br>
Mitigation: Leave webhook and update URLs unset unless the destination is trusted and reviewed. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/fyniujin/skills/cn-llm-router) <br>
- [Routing rules](references/routing-rules.md) <br>
- [Model registry](references/models.yaml) <br>
- [Configuration example](config.example.json) <br>
- [Version metadata](version.json) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [CLI text, JSON, Markdown reports, shell commands, and configuration snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May stream model responses and may write local SQLite cost and cache data when used.] <br>

## Skill Version(s): <br>
2.1.0 (source: frontmatter, release evidence, version.json) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
