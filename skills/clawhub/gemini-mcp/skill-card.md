## Description: <br>
Gemini MCP helps agents generate and edit images, video, and music with Google Gemini models through an MCP server. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[chrischall](https://clawhub.ai/user/chrischall) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent users use this skill to configure and operate a Gemini MCP server for image generation and editing, iterative media refinement, short video generation, and music or audio clip generation. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill requires a Gemini API key and can incur billing through media-generation calls. <br>
Mitigation: Install only trusted package/source versions, store GEMINI_API_KEY deliberately, and confirm billing expectations before running generation workflows. <br>
Risk: User-provided media, local paths, clipboard content, URLs, or prior interaction context may be sent to Gemini as part of requested workflows. <br>
Mitigation: Review inputs before use, choose local file paths and clipboard access intentionally, and avoid continue_last when prior context should not be reused. <br>
Risk: Generated outputs may be written to local directories selected by configuration or tool parameters. <br>
Mitigation: Set output directories intentionally and review saved media before sharing or reusing it. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/gemini-mcp) <br>
- [npm package referenced by the artifact](https://www.npmjs.com/package/@chrischall/gemini-mcp) <br>
- [Source repository referenced by the artifact](https://github.com/chrischall/gemini-mcp) <br>
- [Google AI Studio API key setup](https://aistudio.google.com/apikey) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with JSON configuration and shell command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May guide MCP calls that save generated images, video, or audio to disk when the Gemini server is installed and configured.] <br>

## Skill Version(s): <br>
1.0.3 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
