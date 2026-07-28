## Description: <br>
Gemini MCP helps agents generate and edit images, video, and music with Google Gemini models through an MCP server. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[chrischall](https://clawhub.ai/user/chrischall) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent users use this skill to configure and operate a Gemini MCP server for image generation, image editing, iterative refinement, video generation, and music generation workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The MCP server requires a Gemini API key and can send prompts, reference files, clipboard images when explicitly requested, and selected local video files to Gemini. <br>
Mitigation: Install and use it only when that data sharing is acceptable, and avoid sending sensitive prompts or media unless approved. <br>
Risk: Generated media is written to an output directory selected by configuration or tool parameters. <br>
Mitigation: Choose output directories deliberately and clean up generated files when they are no longer needed. <br>
Risk: Using continue_last for an unrelated task can carry prior interaction context into a new request. <br>
Mitigation: Start a fresh interaction or pass an explicit previous_interaction_id only when continuing the same task. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/gemini-mcp) <br>
- [npm package](https://www.npmjs.com/package/@chrischall/gemini-mcp) <br>
- [Declared source repository](https://github.com/chrischall/gemini-mcp) <br>
- [Google AI Studio API keys](https://aistudio.google.com/apikey) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Configuration, Shell commands, API Calls, Files] <br>
**Output Format:** [Markdown guidance with JSON configuration examples, shell commands, and MCP tool call patterns] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Generated media may be written to local image, video, or audio files by the configured MCP server.] <br>

## Skill Version(s): <br>
1.0.4 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
