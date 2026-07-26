## Description: <br>
Audiolla connects an agent to a user-deployed audiolla server for stem separation, mastering, MIR analysis, DSP transforms, loudness normalization, and related audio-production workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[psyb0t](https://clawhub.ai/user/psyb0t) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, audio engineers, and agent operators use this skill to call a running audiolla server for audio analysis, processing, generation, MIDI, and workflow automation after the user provides AUDIOLLA_URL. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: An exposed audiolla server without authentication can allow others to run audio processing or upload data to the staging area. <br>
Mitigation: Keep the server bound to localhost or require a strong AUDIOLLA_AUTH_TOKEN before exposing it. <br>
Risk: Remote file_url and output_url support can create server-side fetch or upload risk if enabled broadly. <br>
Mitigation: Leave remote URL fetch/upload disabled unless needed, and use AUDIOLLA_FETCH_MODE=allowlist with trusted hosts when enabling it. <br>
Risk: CPU/GPU-heavy audio processing can consume significant local compute when called repeatedly. <br>
Mitigation: Restrict network access, use authentication, and apply rate limiting for deployments reachable beyond localhost. <br>


## Reference(s): <br>
- [Audiolla setup guide](references/setup.md) <br>
- [ClawHub skill page](https://clawhub.ai/psyb0t/skills/audiolla) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, API calls, Configuration, Guidance] <br>
**Output Format:** [Markdown with curl commands and JSON request bodies] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Audio-producing endpoints return JSON locations for staged files or URLs; analysis endpoints return JSON data.] <br>

## Skill Version(s): <br>
1.4.2 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
