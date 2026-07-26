## Description: <br>
Generate images with Nano Banana Pro via OpenRouter when the user asks for image generation or mentions Nano Banana Pro, Gemini 3 Pro Image, or OpenRouter image generation. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[duffycoder](https://clawhub.ai/user/duffycoder) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users and developers use this skill to prompt Nano Banana Pro through OpenRouter, choose image resolution, and save generated PNG outputs for review or attachment in an agent response. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill handles OpenRouter API secrets from command arguments, environment variables, and .env files, including project-level .env files. <br>
Mitigation: Use a dedicated limited OpenRouter key, avoid running from directories with unrelated secrets in .env files, and keep API keys out of prompts and logs. <br>
Risk: An unintended OPENROUTER_BASE_URL can route prompts or credentials to the wrong endpoint. <br>
Mitigation: Verify OPENROUTER_BASE_URL is the intended OpenRouter chat completions endpoint before running the skill. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/duffycoder/skills/nano-banana-pro-openrouter) <br>
- [OpenRouter chat completions endpoint](https://openrouter.ai/api/v1/chat/completions) <br>


## Skill Output: <br>
**Output Type(s):** [shell commands, configuration, files, guidance] <br>
**Output Format:** [Markdown guidance with shell commands, generated PNG file paths, and MEDIA_URL values] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Generated images are saved under ~/.openclaw/workspace/outputs/nano-banana-pro-openrouter; the shell version supports generation only, not image editing.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
