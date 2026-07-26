## Description: <br>
Search X/Twitter and the web, chat with Grok models for text and vision, and analyze X content using xAI's API. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[mischasigtermans](https://clawhub.ai/user/mischasigtermans) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers, researchers, and content teams use this skill to run xAI-backed X/web searches, Grok chat, model listing, and X content analysis from an agent workflow. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Prompts, images, URLs, account handles, and X content may be sent to xAI. <br>
Mitigation: Install and run this skill only when that data sharing is intended; avoid sensitive inputs unless approved for xAI processing. <br>
Risk: The skill can reuse xAI-related API keys from other skill configuration entries. <br>
Mitigation: Use a dedicated, revocable xAI API key for this skill and review local configuration before running it. <br>
Risk: Social-media analysis guidance could be misused to game platform ranking or evade enforcement. <br>
Mitigation: Use the analysis outputs for quality and compliance review, not to bypass X platform rules or moderation. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/mischasigtermans/skills/xai-plus) <br>
- [xAI Console](https://console.x.ai) <br>
- [API Reference](references/api-reference.md) <br>
- [Search Patterns](references/search-patterns.md) <br>
- [Models](references/models.md) <br>
- [Analysis Prompts](references/analysis-prompts.md) <br>
- [X Algorithm](references/x-algorithm.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, JSON, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell command examples and JSON outputs from scripts] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires Node.js and an xAI API key; supports X search, web search, chat, image analysis, content analysis, model listing, and optional raw API output.] <br>

## Skill Version(s): <br>
2.0.2 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
