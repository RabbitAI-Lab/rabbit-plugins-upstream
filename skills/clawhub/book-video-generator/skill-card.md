## Description: <br>
Generates a three-minute book explainer video from a book title and author, including review copy, storyboard prompts, AI illustrations, TTS narration, subtitles, and a final MP4. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[chenjun198711](https://clawhub.ai/user/chenjun198711) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Creators, marketers, educators, and agent users use this skill to turn a book title and author into a narrated short-form reading video. Developers can also use it as a cross-platform workflow for generating scripts, images, audio, captions, cover art, and video assembly commands. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The security scan reports broad runtime authority during use. <br>
Mitigation: Review before installing, run in a virtual environment or container, and keep generated outputs inside a dedicated project directory. <br>
Risk: The security scan reports automatic installation of unpinned packages during use. <br>
Mitigation: Preinstall and pin dependencies before execution instead of allowing automatic package installation. <br>
Risk: The skill can use multiple external providers that require API credentials. <br>
Mitigation: Provide only the API keys needed for the selected image or TTS provider. <br>
Risk: The security guidance calls out SD_WEBUI_URL as a sensitive runtime endpoint. <br>
Mitigation: Set SD_WEBUI_URL only to a trusted local endpoint. <br>


## Reference(s): <br>
- [Skill prompts](references/prompts.md) <br>
- [Cross-platform guide](references/CROSS_PLATFORM.md) <br>
- [Original workflow reference](references/workflow-original.yaml) <br>
- [Optional media assets](assets/README.md) <br>
- [Agent Skills open standard](https://agentskills.io) <br>
- [Book video generator demo](https://chenjun198711.github.io/book-video-generator/) <br>
- [Volcengine image model setup](https://console.volcengine.com/ark/region:ark+cn-beijing/openManagement) <br>
- [Volcengine speech setup](https://console.volcengine.com/speech/new) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Files] <br>
**Output Format:** [Structured workflow guidance with JSON payloads and shell commands; generated artifacts include MP4 video, images, audio, captions, and configuration files.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Creates project-local output files and may call external image-generation and TTS providers depending on configuration.] <br>

## Skill Version(s): <br>
2.8.0 (source: frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
