## Description: <br>
MiniMax Music 2.6 generation on PoYo / poyo.ai via `https://api.poyo.ai/api/generate/submit`; use for `minimax-music-2.6`, complete music tracks, lyrics, lyrics optimization, instrumental mode, audio output settings, callbacks, and status polling. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[coolhackboy](https://clawhub.ai/user/coolhackboy) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to prepare and optionally submit PoYo MiniMax Music 2.6 generation payloads for lyrics-based, lyrics-optimized, or instrumental music workflows, then capture task IDs for polling or callbacks. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: PoYo API keys could be exposed if used in browser code, public repositories, logs, screenshots, or chat output. <br>
Mitigation: Keep POYO_API_KEY server-side in environment variables or a backend secret manager and avoid echoing authorization headers. <br>
Risk: Music prompts, lyrics, callback URLs, task IDs, or generated audio links may contain private project or user information. <br>
Mitigation: Review payloads before submission and avoid sending or logging private data unless project policy allows it. <br>
Risk: Submitting a payload sends data to the PoYo API and creates an external asynchronous generation task. <br>
Mitigation: Make live API calls only after explicit user confirmation from a trusted shell with a prepared payload. <br>


## Reference(s): <br>
- [PoYo MiniMax Music 2.6 API Reference](references/api.md) <br>
- [PoYo MiniMax Music 2.6 Model Page](https://poyo.ai/models/minimax-music-2-6) <br>
- [PoYo MiniMax Music 2.6 API Docs](https://docs.poyo.ai/api-manual/music-series/minimax-music-2.6) <br>
- [PoYo MiniMax Music 2.6 OpenAPI JSON](https://docs.poyo.ai/api-manual/music-series/minimax-music-2.6.json) <br>
- [ClawHub Skill Page](https://clawhub.ai/coolhackboy/skills/poyo-minimax-music-2-6) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with JSON payloads and bash curl commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include a PoYo task_id when a request is submitted.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
