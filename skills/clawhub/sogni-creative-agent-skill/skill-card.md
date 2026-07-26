## Description: <br>
Sogni Creative Agent Skill gives agents a CLI and skill surface for image, video, and music generation through Sogni AI's decentralized GPU network. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[krunkosaurus](https://clawhub.ai/user/krunkosaurus) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and agent users use this skill to plan and execute Sogni-powered creative workflows, including prompt-to-image, image editing, video generation, music generation, loop reels, personas, and durable multi-step media workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill uses a networked Sogni media-generation CLI with a Sogni API key and may spend account credits or use subscription entitlement. <br>
Mitigation: Install only for users who intend to use Sogni services, keep credentials in the documented credentials file or environment, and review balance or billing-mode guidance before paid generation. <br>
Risk: Hosted modes can upload selected local media to Sogni services for generation, editing, or multi-step workflows. <br>
Mitigation: Use direct CLI modes for private media that must stay local, and upload only media the user has approved for Sogni processing. <br>
Risk: Saved personas, memories, personality settings, face photos, and voice clips can persist locally and may represent sensitive people or preferences. <br>
Mitigation: Store persona and voice assets only with consent, remove saved personas or memories when no longer needed, and avoid using voice clips or likenesses without permission. <br>
Risk: The skill can update its installed code through self-update behavior. <br>
Mitigation: Run self-update only after explicit approval and review the version change or changelog before relying on the upgraded package. <br>


## Reference(s): <br>
- [ClawHub skill listing](https://clawhub.ai/krunkosaurus/skills/sogni-creative-agent-skill) <br>
- [Sogni AI homepage](https://sogni.ai) <br>
- [Hosted API guide](artifact/references/hosted-api.md) <br>
- [Model reference](artifact/references/models.md) <br>
- [Personas and memory guide](artifact/references/personas-memory.md) <br>
- [Video editing guide](artifact/references/video-editing.md) <br>
- [Video prompting guide](artifact/references/video-prompting.md) <br>
- [Loop maker guide](artifact/references/loop-maker.md) <br>
- [OpenClaw configuration guide](artifact/references/openclaw-config.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands, JSON examples, and configuration instructions] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May direct an agent to create local media files, inspect JSON command output, or call Sogni-hosted generation workflows.] <br>

## Skill Version(s): <br>
3.16.1 (source: frontmatter metadata, CHANGELOG, and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
