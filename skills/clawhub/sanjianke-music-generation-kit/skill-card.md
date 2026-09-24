## Description:

This skill helps agents call the a7w music_generation API to create songs and lyrics, process vocals, clone voices, and export audio, MIDI, MP4, WAV, and timing results using the user's own API key.

This skill is ready for commercial/non-commercial use.

## Publisher:

[2253128](https://clawhub.ai/user/2253128)

### License/Terms of Use:

MIT

## Use Case:

External developers, creators, and agent builders use this skill to integrate paid a7w music-generation workflows into agent sessions, including lyric generation, song creation, voice cloning, stem or vocal processing, and media export. Users must bring their own api.a7w.cn API key and are responsible for permissions, billing, and content compliance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The bundled client can use the user's API key beyond the advertised music scope through broad a7w client features.

Mitigation: Install only if you intend to trust a7w.cn with prompts, media URLs, generated results, and API-key-backed paid calls; avoid generic marketplace features unless broad access is intended.

Risk: A custom service host can redirect key-backed API traffic away from the default a7w endpoint.

Mitigation: Do not use --host or A7W_HOST unless you fully trust the endpoint.

Risk: Voice cloning and audio upload workflows can process sensitive or third-party audio.

Mitigation: Only clone or upload voices and audio that you own or have explicit permission to use.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/2253128/skills/sanjianke-music-generation-kit)
- [README](README.md)
- [Getting Started](references/getting-started.md)
- [General Notes](references/通用说明.md)
- [Create Music Task API](references/api-create.md)
- [Generate Lyrics API](references/api-lyrics.md)
- [Mashup Lyrics API](references/api-mashup_lyrics.md)
- [MIDI Export API](references/api-midi.md)
- [MP4 Export API](references/api-mp4.md)
- [Singer Persona API](references/api-persona.md)
- [Task Query API](references/api-query.md)
- [Style Optimization API](references/api-style.md)
- [Lyric Timing API](references/api-timing.md)
- [Upload Audio API](references/api-upload_audio.md)
- [Voice Clone API](references/api-voice_clone.md)
- [Vocal Processing API](references/api-vox.md)
- [WAV Export API](references/api-wav.md)
- [a7w API service](https://api.a7w.cn/)
- [a7w AI plugin market](https://aigc.a7w.cn/)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands, Python client usage, and JSON request examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May guide API calls that return task IDs, status JSON, generated media URLs, exported files, and account usage data from the third-party a7w service.]

## Skill Version(s):

1.0.6 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
