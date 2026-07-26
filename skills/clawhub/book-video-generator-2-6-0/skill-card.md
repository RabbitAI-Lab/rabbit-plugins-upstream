## Description: <br>
This skill helps agents generate a three-minute book explainer video from a book title and author, including a review script, storyboard, AI illustrations, TTS narration, subtitles, cover image, and final MP4 composition. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[chenjun198711](https://clawhub.ai/user/chenjun198711) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External creators and developers use this skill to turn a named book and author into a short narrated book-review video. The workflow uses web search, LLM prompts, image generation, TTS, and local video composition scripts, so users should configure trusted API keys and endpoints before running it. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Review before execution as proposals could introduce incorrect or misleading guidance into skills. <br>
Mitigation: Review and scan skill before deployment. <br>

## Reference(s): <br>
- [Prompt Reference](references/prompts.md) <br>
- [Cross-Platform Guide](references/CROSS_PLATFORM.md) <br>
- [Original Workflow YAML](references/workflow-original.yaml) <br>
- [Demo Page](https://chenjun198711.github.io/book-video-generator/) <br>
- [Agent Skills Open Standard](https://agentskills.io) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown instructions with JSON examples, shell commands, and generated local media files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces local MP4 video outputs and intermediate image, audio, subtitle, and JSON assets; may contact search, TTS, and image-generation services configured by the user.] <br>

## Skill Version(s): <br>
2.6.0 (source: SKILL.md frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
