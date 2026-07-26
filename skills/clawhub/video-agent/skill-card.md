## Description: <br>
Deprecated HeyGen video-generation skill for creating prompt-based and avatar videos through legacy v1/v2 HeyGen endpoints, with guidance to prefer the newer create-video or avatar-video skills. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[michaelwang11394](https://clawhub.ai/user/michaelwang11394) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, developers, and agents use this skill to plan and invoke HeyGen video-generation workflows, including prompt-based videos, avatar and voice selection, asset uploads, status polling, captions, templates, webhooks, and Remotion integration. Because the skill is deprecated, users should prefer replacement skills for current v3 workflows when possible. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill is deprecated and documents older HeyGen v1/v2 endpoints. <br>
Mitigation: Prefer the newer create-video or avatar-video skills for current v3 workflows, and install this legacy skill only when backward compatibility is required. <br>
Risk: Using the skill gives an agent access to HeyGen API capabilities and sends user-selected prompts, portraits, uploaded files, media URLs, and account actions to HeyGen. <br>
Mitigation: Review prompts, portraits, uploaded files, remote asset URLs, recipient data, generated requests, and delete actions before use, especially for confidential or regulated content. <br>
Risk: Webhook integrations can expose status events or accept spoofed callbacks if webhook destinations and signatures are not handled carefully. <br>
Mitigation: Use trusted webhook destinations and require webhook signature verification in real deployments. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/michaelwang11394/skills/video-agent) <br>
- [HeyGen Video Agent API documentation](https://docs.heygen.com/reference/generate-video-agent) <br>
- [SKILL.md](artifact/SKILL.md) <br>
- [Authentication](artifact/references/authentication.md) <br>
- [Video Agent API](artifact/references/video-agent.md) <br>
- [Video Generation](artifact/references/video-generation.md) <br>
- [Video Status and Polling](artifact/references/video-status.md) <br>
- [Webhooks](artifact/references/webhooks.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with API request examples, JSON payloads, code snippets, and shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires HEYGEN_API_KEY and may use HeyGen MCP tools or direct HTTP requests; generated media, prompts, uploaded files, account actions, webhook URLs, and download URLs are handled by HeyGen.] <br>

## Skill Version(s): <br>
2.23.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
