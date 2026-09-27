## Description:

Generate AI music using ACE-Step 1.5 via ACE Music's free API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[fspecii](https://clawhub.ai/user/fspecii)

### License/Terms of Use:


## Use Case:

External users and developers use this skill to generate songs, instrumentals, beats, covers, and edited audio from prompts, lyrics, style descriptions, and optional audio inputs through the ACE Music API.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The generation script has a filename-based code execution flaw.

Mitigation: Review the script before use and avoid user-supplied or unusual output filenames until the script is fixed.

Risk: The skill uses an API key and has weak credential handling guidance.

Mitigation: Store ACE_MUSIC_API_KEY in a proper secret store and do not place API keys in TOOLS.md or chat history.

Risk: Changing ACE_MUSIC_BASE_URL can redirect prompts, lyrics, credentials, and audio requests to a different endpoint.

Mitigation: Use the default API endpoint unless the alternate endpoint is fully trusted.

Risk: Prompts, lyrics, and audio inputs may be sent to the ACE Music hosted API.

Mitigation: Use the skill only with non-sensitive prompts, lyrics, and audio content.

## Reference(s):

- [ACE-Step OpenRouter API Reference](references/api-docs.md)
- [ACE Music API Key Page](https://acemusic.ai/playground/api-key)
- [ACE Music API Base URL](https://api.acemusic.ai)
- [ClawHub Skill Page](https://clawhub.ai/fspecii/skills/ace-music)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Files, Guidance]

**Output Format:** [Markdown guidance with shell commands and generated MP3 audio file paths]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The bundled script writes MP3 files decoded from API responses and prints saved file paths.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
