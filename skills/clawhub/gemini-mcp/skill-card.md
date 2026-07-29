## Description: <br>
Generate and edit images, video, and music with Google Gemini models through an MCP server. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[chrischall](https://clawhub.ai/user/chrischall) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent users use this skill to configure and call a Gemini MCP server for image generation and editing, consistent image sets, short video generation, and music or audio clip generation. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Prompts and selected media may be sent to Google/Gemini services. <br>
Mitigation: Use only media and prompts you are authorized to share, and avoid private, regulated, or proprietary inputs unless the applicable retention and billing terms are acceptable. <br>
Risk: Generated media can contain visual artifacts, incorrect details, or misrendered text. <br>
Mitigation: Review generated images, video, audio, and embedded text before publication or downstream use. <br>
Risk: The setup requires a Gemini API key and may use billing-enabled services. <br>
Mitigation: Store API keys outside committed files and confirm account billing expectations before enabling generation workflows. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/gemini-mcp) <br>
- [npm package @chrischall/gemini-mcp](https://www.npmjs.com/package/@chrischall/gemini-mcp) <br>
- [Google AI Studio API key setup](https://aistudio.google.com/apikey) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, configuration, API calls, files] <br>
**Output Format:** [Markdown guidance with JSON configuration snippets, shell commands, MCP tool calls, and generated media file paths] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Generated image, video, and audio outputs may be saved to disk or returned inline depending on tool parameters.] <br>

## Skill Version(s): <br>
1.1.0 (source: server-resolved release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
