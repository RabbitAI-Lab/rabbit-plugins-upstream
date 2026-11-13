## Description:

Helps users choose a text-to-speech option and create voice-over audio with optional timed subtitles.

This skill is ready for commercial/non-commercial use.

## Publisher:

[maxouf](https://clawhub.ai/user/maxouf)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and content creators use this skill to select a speech provider based on voice needs, language, and budget, then turn one text or a batch into audio with optional captions and delivery metadata.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Text may be processed by external services.

Mitigation: Avoid submitting sensitive material unless you understand the service's handling of it.

Risk: The reported install command does not pin the CLI or source.

Mitigation: Review the installation source and skill instructions before installing.

Risk: The security scan evidence is incomplete because one local reference was unresolved.

Mitigation: Treat the scan as incomplete and review the skill instructions and referenced resources before installation.

## Reference(s):

- [ClawHub release](https://clawhub.ai/maxouf/skills/text-to-speech)
- [Skill homepage](https://github.com/maxouf/sherwood-skills/tree/main/skills/text-to-speech)
- [Apify text-to-speech MCP endpoint](https://mcp.apify.com/?tools=sherwood/text-to-speech-batch)
- [OpenAI audio speech endpoint](https://api.openai.com/v1/audio/speech)

## Skill Output:

**Output Type(s):** [Audio file URLs, Subtitle file URLs, CSV metadata, Provider guidance, Shell commands]

**Output Format:** [Markdown guidance and shell commands; audio is delivered by URL, with optional SRT/VTT subtitle URLs and CSV metadata.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Batch results can include language, voice, duration, character count, price tier, status, and output URLs.]

## Skill Version(s):

1.0.0 (source: frontmatter and server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
