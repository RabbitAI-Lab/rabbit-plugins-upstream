## Description:

Helps animation, comic drama, game, original IP, and character-content teams use AI-HIVE MCP to check current model availability and pricing, then plan and produce original 90s magical-girl style image and video assets with character consistency, rights checks, task tracking, and explicit confirmation before paid generation, batch work, sending, or public release.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External creative teams and developers use this skill to structure an AI-HIVE workflow for original 90s magical-girl animation concepts, character settings, storyboards, keyframes, animation clips, and consistency checks. It emphasizes model and price lookup before generation, rights tracking for source materials, task recovery, and explicit approval before paid or public actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Credentials could be sent to an untrusted MCP endpoint if AI_HIVE_MCP_URL is changed.

Mitigation: Use the default AI-HIVE MCP URL unless the destination is fully trusted, prefer OAuth through a trusted MCP client, and verify the endpoint before running helper scripts.

Risk: The automatic activation scope is broad enough to invoke the workflow for general AI image, video, short-video, or animation requests.

Mitigation: Confirm the user actually intends to use AI-HIVE for this 90s magical-girl animation workflow before connecting tools or starting generation.

Risk: Image and video generation, uploads, batch work, sending, or public posting may create cost, privacy, rights, or publication exposure.

Mitigation: Require explicit user confirmation before paid generation, uploads, batch work, sending, or public release, and record source-material rights, task IDs, model parameters, and price snapshots.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/ai-hive-animation-091-13cd32b)
- [Publisher profile](https://clawhub.ai/user/wubin1836)
- [AI-HIVE workspace](https://ai-hive.iclip.cn/chat)
- [AI-HIVE MCP endpoint](https://ai-hive.iclip.cn/api/mcp)
- [MCP login and binding guide](references/mcp-binding.md)
- [Original workflow card](references/original-workflow.md)
- [OAuth MCP configuration example](references/mcp-config.example.json)
- [API key MCP configuration example](references/mcp-config-api-key.example.json)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with JSON configuration examples, shell commands, and local JSON work orders]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May trigger AI-HIVE MCP API calls when the user has authenticated and confirmed paid, batch, sending, or public-release actions.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
