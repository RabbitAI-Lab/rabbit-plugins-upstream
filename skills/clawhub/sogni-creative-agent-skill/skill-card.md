## Description: <br>
Sogni Creative Agent Skill gives agents a CLI and hosted workflow surface for generating and editing images, videos, and music on Sogni AI's decentralized GPU network. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[krunkosaurus](https://clawhub.ai/user/krunkosaurus) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and agent users use this skill to connect agent runtimes to Sogni media generation, editing, hosted workflows, model discovery, personas, memories, and reusable creative session state. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can upload prompts and selected local media to Sogni API-backed services. <br>
Mitigation: Use hosted workflow or chat modes only when the user explicitly accepts the privacy tradeoff, and prefer direct CLI mode for media that should stay local. <br>
Risk: Persona photos, voice clips, memories, and last-render state may persist under ~/.config/sogni. <br>
Mitigation: Review stored Sogni configuration and avoid saving biometric references unless persistent identity or voice reuse is intentional. <br>
Risk: Mature or no-filter workflows and broad hosted modes can increase safety, privacy, and cost exposure. <br>
Mitigation: Require explicit user intent before mature --no-filter workflows or broad hosted workflow/chat modes, and review cost-relevant settings before execution. <br>
Risk: The skill includes self-update and reminder controls that can modify installed code or update state. <br>
Mitigation: Run self-update or --snooze-update only after an explicit user request and post-update verification. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/krunkosaurus/skills/sogni-creative-agent-skill) <br>
- [Publisher profile](https://clawhub.ai/user/krunkosaurus) <br>
- [Sogni homepage](https://sogni.ai) <br>
- [Sogni model catalog API](https://api.sogni.ai/v1/model-catalog) <br>
- [Hosted API reference](references/hosted-api.md) <br>
- [Loop maker reference](references/loop-maker.md) <br>
- [Models reference](references/models.md) <br>
- [OpenClaw configuration reference](references/openclaw-config.md) <br>
- [Personas and memory reference](references/personas-memory.md) <br>
- [Private mature video reference](references/private-mature-video.md) <br>
- [Seamless tiling reference](references/seamless-tiling.md) <br>
- [Video editing reference](references/video-editing.md) <br>
- [Video prompting reference](references/video-prompting.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell commands, JSON-capable command output, configuration snippets, and generated media file paths or URLs] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The skill can produce local image, video, and audio files through the Sogni CLI and can use hosted workflow APIs when explicitly requested.] <br>

## Skill Version(s): <br>
3.21.0 (source: server release metadata and artifact/version.mjs) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
