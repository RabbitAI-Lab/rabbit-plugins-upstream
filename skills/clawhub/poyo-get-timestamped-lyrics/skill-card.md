## Description: <br>
Retrieve timestamped lyrics on PoYo / poyo.ai via the PoYo generation API for synchronized lyrics, word timing, waveform data, callbacks, and music detail retrieval. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[coolhackboy](https://clawhub.ai/user/coolhackboy) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to prepare and submit PoYo Get Timestamped Lyrics requests for completed music tracks, then interpret task IDs, timing responses, waveform data, or webhook-driven follow-up steps. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: PoYo requests can send task IDs, audio IDs, optional callback URLs, request payloads, lyrics timing data, and waveform-related data to PoYo. <br>
Mitigation: Confirm that using PoYo fits the user's privacy needs before submission, and keep private lyrics, identifiers, callback URLs, and waveform data out of logs unless policy allows it. <br>
Risk: The included submission workflow requires a PoYo API key and can make live API requests. <br>
Mitigation: Store POYO_API_KEY only in server-side environment variables or a secret manager, and run the submission script only with trusted payload files after the user confirms the request should be sent. <br>


## Reference(s): <br>
- [PoYo Get Timestamped Lyrics model page](https://poyo.ai/models/get-timestamped-lyrics) <br>
- [PoYo Get Timestamped Lyrics API docs](https://docs.poyo.ai/api-manual/music-series/get-timestamped-lyrics) <br>
- [PoYo Get Timestamped Lyrics OpenAPI JSON](https://docs.poyo.ai/api-manual/music-series/get-timestamped-lyrics.json) <br>
- [Skill API reference](references/api.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with JSON payloads and curl command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include PoYo model identifiers, task and audio ID summaries, callback guidance, and returned task or timing response details.] <br>

## Skill Version(s): <br>
1.0.1 (source: server-resolved release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
