## Description: <br>
Generate and edit images, video, and music with Google Gemini models via MCP. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[chrischall](https://clawhub.ai/user/chrischall) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and creative agents use this skill to configure and call a Gemini MCP server for image generation, image editing, consistent image sets, short video generation, and music or audio clip generation. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill requires a Gemini API key and depends on a third-party npm package. <br>
Mitigation: Install only when the publisher and package are trusted, and provide only the minimum Gemini API access needed for the intended workflow. <br>
Risk: Media inputs can come from local paths, clipboard content, URLs, base64 values, or uploads, which may expose sensitive user files or media to Gemini or a hosted connector. <br>
Mitigation: Use explicit file paths, clipboard input, and uploads only for media intended for processing, and delete uploaded files when they are no longer needed. <br>
Risk: Generated image text, Roman numerals, and detailed edits may be inaccurate or over-preserve the source image. <br>
Mitigation: Review generated media before use, rerun with adjusted prompts or seeds when needed, and verify any text or factual details in outputs. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/gemini-mcp) <br>
- [npm package](https://www.npmjs.com/package/@chrischall/gemini-mcp) <br>
- [Google AI Studio API keys](https://aistudio.google.com/apikey) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, configuration, shell commands, text] <br>
**Output Format:** [Markdown with inline JSON and shell command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Guidance describes MCP tool calls that can save generated images, videos, music, and uploaded file references outside the conversation.] <br>

## Skill Version(s): <br>
1.3.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
