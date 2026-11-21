## Description:

AI podcast: turn an article, notes or a dialogue script into a solo or two-host episode, with SRT subtitles, timestamped chapters and a transcript for show notes. Python stdlib only, no GPU.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yanghhu](https://clawhub.ai/user/yanghhu)

### License/Terms of Use:

MIT

## Use Case:

External authors, podcasters, educators, and developers can turn articles, notes, or dialogue scripts into solo or two-host podcast episodes with voiceover, subtitles, timestamped chapters, and show notes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Voice generation uses a cloud service and may involve account credentials, uploaded material, and usage charges.

Mitigation: Review the service permissions and privacy needs, keep the API key in an environment variable, and check current capabilities and pricing before generating audio.

Risk: The skill can use reference audio for voice cloning and can transform source articles or add music.

Mitigation: Use only voices and source materials you own or are authorized to use, and follow applicable AI-generated-content disclosure rules.

Risk: Security analysis is marked partial, and the guidance calls out environment, file, network, and shell capabilities as considerations.

Mitigation: Review the skill's requested capabilities and tool scope against your installation before use.

## Reference(s):

- [Miragea](https://miragea.ai)
- [Miragea API](https://miragea.ai/v1)
- [ClawHub skill page](https://clawhub.ai/yanghhu/skills/ai-podcast-voiceover)

## Skill Output:

**Output Type(s):** [Audio, Text, Markdown, JSON, Shell commands, Configuration instructions, Guidance]

**Output Format:** [WAV voiceover audio, SRT subtitles, JSON timing and chapter data, Markdown show notes and transcripts, plus shell-command instructions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Per-line audio can be reused when editing; chapter timestamps follow the generated audio. Cloud generation requires a Miragea API key; pricing and limits depend on live service capabilities.]

## Skill Version(s):

1.0.0 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
