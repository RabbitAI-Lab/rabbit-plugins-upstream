## Description:

After a creator explicitly approves a preview, this skill runs image, video, voiceover, or timeline-music production jobs for a short-drama project and records the results.

This skill is ready for commercial/non-commercial use.

## Publisher:

[worldwonderer](https://clawhub.ai/user/worldwonderer)

### License/Terms of Use:

MIT

## Use Case:

External creators and production teams use this skill to run explicitly approved image, video, text-to-speech, and music jobs for short-drama projects. It saves generated media and concise run records back to the project.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The release security assessment reports recovery flaws that can bypass approval.

Mitigation: Prefer a version with corrected recovery handling before using live API keys or valuable media; reconcile active jobs before retrying or collecting results.

Risk: The release security assessment reports network handling that could expose API keys.

Mitigation: Prefer a version with corrected redirect handling, review which references reach each provider, use spending-limited keys, back up results, and keep overwrite disabled.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/worldwonderer/skills/short-drama-produce)
- [Adapter contract](references/adapter-contract.md)
- [GPT Image 2 provider guide](references/providers/gpt-image-2.md)
- [MiniMax H3 video provider guide](references/providers/minimax-h3-video.md)
- [MiniMax music provider guide](references/providers/minimax-music.md)
- [MiniMax speech provider guide](references/providers/minimax-speech.md)
- [Seedance provider guide](references/providers/seedance.md)
- [GPT Image 2 model documentation](https://developers.openai.com/api/docs/models/gpt-image-2)
- [OpenAI image generation API](https://developers.openai.com/api/reference/resources/images/methods/generate)
- [OpenAI image edits API](https://developers.openai.com/api/reference/resources/images/methods/edit)
- [MiniMax music generation API](https://platform.minimax.io/docs/api-reference/music-generation)
- [MiniMax text-to-speech API](https://platform.minimax.io/docs/api-reference/speech-t2a-http)

## Skill Output:

**Output Type(s):** [Image files, Video files, Audio files, JSON run records]

**Output Format:** [Generated media files with concise JSON run records]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Production outputs are saved in the project; run records summarize execution status and output details.]

## Skill Version(s):

1.0.3 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
