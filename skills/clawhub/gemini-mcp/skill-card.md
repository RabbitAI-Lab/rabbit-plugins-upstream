## Description: <br>
Generates and edits images, video, and music with Google Gemini models through an MCP server. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[chrischall](https://clawhub.ai/user/chrischall) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent users use this skill to configure and call a Gemini MCP server for image generation and editing, short video generation, music generation, file upload reuse, and iterative media refinement. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill requires a Gemini API key and uses it to call Google Gemini services. <br>
Mitigation: Install only in environments where the Gemini API key can be stored and scoped appropriately. <br>
Risk: Requested media inputs may be sent to Google Gemini or uploaded through the Gemini Files API. <br>
Mitigation: Provide clipboard, local file, URL, or upload inputs only when that content is intended for Gemini processing; delete Files API uploads when they are no longer needed. <br>
Risk: Generated media may be saved locally in the working directory or a configured output directory. <br>
Mitigation: Choose output_dir or inline behavior deliberately in shared environments and review saved files before sharing. <br>


## Reference(s): <br>
- [ClawHub skill listing](https://clawhub.ai/chrischall/skills/gemini-mcp) <br>
- [npm package @chrischall/gemini-mcp](https://www.npmjs.com/package/@chrischall/gemini-mcp) <br>
- [Google AI Studio API keys](https://aistudio.google.com/apikey) <br>


## Skill Output: <br>
**Output Type(s):** [API Calls, Files, Shell commands, Configuration, Guidance] <br>
**Output Format:** [MCP tool-call responses with file paths, metadata, optional inline media bytes, JSON configuration snippets, and shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May save generated images, videos, or audio to disk; may return inline media when requested.] <br>

## Skill Version(s): <br>
1.4.0 (source: release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
