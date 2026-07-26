## Description: <br>
AI agent self-portrait generator. Create avatars, profile pictures, and visual identity using Gemini image generation. Supports mood-based generation, seasonal themes, and automatic style evolution. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[iisweetheartii](https://clawhub.ai/user/iisweetheartii) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and agent operators use this skill to generate avatar, banner, or full-body self-portrait images for an AI agent from a personality profile, mood, and theme. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Heartbeat guidance can lead an agent to update public avatars or profiles without clear approval for each action. <br>
Mitigation: Require explicit human approval before any avatar or account update, especially for Discord, Twitter/X, or AgentGram. <br>
Risk: Generated images, prompts, and personality details may be retained in the selected output directory or memory. <br>
Mitigation: Avoid sensitive personality files or prompts, choose an output directory suitable for retained media, and review generated assets before sharing. <br>
Risk: The skill depends on GEMINI_API_KEY for external image generation. <br>
Mitigation: Keep GEMINI_API_KEY secret, provide it only through the runtime environment, and do not commit prompts, logs, or generated files containing secrets. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/iisweetheartii/skills/agent-selfie) <br>
- [Project homepage](https://github.com/IISweetHeartII/agent-selfie) <br>
- [Google AI Studio API keys](https://aistudio.google.com/apikey) <br>
- [OpenClaw](https://openclaw.org) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Files] <br>
**Output Format:** [Markdown instructions with shell commands and generated PNG image files, prompts.json, and an HTML gallery] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires python3 and GEMINI_API_KEY; supports avatar, banner, and full portrait formats plus mood, theme, personality, count, and output directory options.] <br>

## Skill Version(s): <br>
1.2.1 (source: package.json and ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
