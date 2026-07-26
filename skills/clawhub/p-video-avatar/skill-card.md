## Description: <br>
Use when someone wants a person on camera speaking a script: a lip-synced host, spokesperson, or narrated avatar from a portrait photo. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[pruna-ai](https://clawhub.ai/user/pruna-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and creative operators use this skill to prepare one Pruna p-video-avatar generation for a portrait-based talking-head clip, including prompt drafting, media upload, API request construction, and confirmation gates before a paid call. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The workflow sends portrait images, scripts or audio, prompts, voice settings, and language choices to Pruna's API and may incur paid generation costs. <br>
Mitigation: Confirm PRUNA_API_KEY availability, media inputs, script or audio, voice settings, language, resolution, and prompts with the user before making any API call. <br>
Risk: Using the skill for multi-scene continuity, silent B-roll, or motion transfer can produce the wrong workflow and mismatched expectations. <br>
Mitigation: Use this skill for one p-video-avatar prediction per invocation and redirect multi-scene, B-roll, and motion-transfer requests to the specialized Pruna skills named in the artifact. <br>
Risk: A weak or reused prompt can drift from the user's intended speaker, host beat, or approved wording. <br>
Mitigation: Draft a fresh, faithful video prompt for the clip, keep the portrait identity and script or audio fixed, and show the prompt and voice fields before posting when wording is not locked. <br>


## Reference(s): <br>
- [ClawHub p-video-avatar Skill Page](https://clawhub.ai/pruna-ai/skills/p-video-avatar) <br>
- [Pruna Files API Endpoint](https://api.pruna.ai/v1/files) <br>
- [Pruna Predictions API Endpoint](https://api.pruna.ai/v1/predictions) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, configuration] <br>
**Output Format:** [Markdown guidance with curl examples and JSON request bodies] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces a single-stream agent workflow for one Pruna p-video-avatar prediction; the generated video is produced by Pruna's API.] <br>

## Skill Version(s): <br>
1.0.7 (source: server release metadata and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
