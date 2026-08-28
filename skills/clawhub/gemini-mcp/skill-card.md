## Description:

gemini-mcp helps agents generate and edit images, videos, and music with Google Gemini models through an MCP server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to configure and operate a Gemini MCP server for media generation workflows, including image creation, image editing, short video generation, and music or audio clip generation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected prompts and media references may be sent to Gemini.

Mitigation: Use the skill only with content appropriate for Gemini processing and review sensitive prompts or media before invoking generation tools.

Risk: Clipboard and input-directory features can expose unintended local media.

Mitigation: Copy only the intended asset and point GEMINI_INPUT_DIR and GEMINI_OUTPUT_DIR at narrow project folders.

Risk: Uploaded Files API assets may remain available after the immediate task.

Mitigation: Use file listing and deletion tools to remove uploaded items when they are no longer needed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/gemini-mcp)
- [npm package @chrischall/gemini-mcp](https://www.npmjs.com/package/@chrischall/gemini-mcp)
- [Google AI Studio API keys](https://aistudio.google.com/apikey)

## Skill Output:

**Output Type(s):** [Files, API calls, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown instructions with JSON and shell command examples; generated results are saved media files or inline media responses when the MCP server is used.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports optional model selection, file upload references, local input and output directories, asynchronous jobs, and idempotency keys.]

## Skill Version(s):

1.11.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
