## Description:

Generate and edit images, video, and music with Google Gemini models via MCP.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to configure and operate a Gemini MCP server for generating or editing images, videos, and music from natural-language prompts and selected reference media.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected prompts and media may be sent to Google Gemini services.

Mitigation: Install and use the skill only when sending the selected content to Google is acceptable for the user's task and data policy.

Risk: The skill runs an external MCP package and requires a Gemini API key.

Mitigation: Pin the npm package version for reproducible installs and provide the API key through environment configuration rather than embedding it in prompts or shared files.

Risk: Local-file upload and file deletion operations can affect user-selected files or remote uploaded assets.

Mitigation: Use explicit file paths, review confirmation or dry-run previews before uploads or deletes, and avoid broad path patterns.

Risk: Using continue_last across tasks can continue the wrong prior Gemini interaction.

Mitigation: Use an explicit previous_interaction_id when switching tasks or when precise conversation continuity matters.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/gemini-mcp)
- [npm package @chrischall/gemini-mcp](https://www.npmjs.com/package/@chrischall/gemini-mcp)
- [Google AI Studio API keys](https://aistudio.google.com/apikey)

## Skill Output:

**Output Type(s):** [Files, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with JSON configuration snippets, shell commands, and generated media file paths or metadata.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated images may be saved as PNG or JPEG, videos as MP4, and music as MP3 or WAV; some tools can return inline bytes with metadata.]

## Skill Version(s):

1.7.0 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
