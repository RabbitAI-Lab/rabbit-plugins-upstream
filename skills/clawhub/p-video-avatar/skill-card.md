## Description:

Use when someone wants a person on camera speaking a script: a lip-synced host, spokesperson, or narrated avatar from a portrait photo.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pruna-ai](https://clawhub.ai/user/pruna-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and creators use this skill to prepare and submit a single Pruna p-video-avatar job that turns a portrait plus either a script or uploaded narration into a talking-head avatar clip. It guides prompt drafting, user confirmation, portrait upload, prediction creation, polling, and download handoff.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uploads user-provided portraits, scripts, voice settings, and optional narration audio to Pruna's API.

Mitigation: Confirm the user is comfortable sharing those inputs with Pruna before installation or use.

Risk: Avatar generation can involve a person's likeness or voice.

Mitigation: Confirm the user has the right to use the person's likeness and voice before generating the clip.

Risk: The skill requires a PRUNA_API_KEY credential to create files and predictions.

Mitigation: Keep PRUNA_API_KEY scoped to the intended environment and avoid exposing it in shared logs or files.

Risk: The skill depends on related Pruna skills for prompt craft and API handling.

Mitigation: Pin referenced Pruna skill installs when stricter supply-chain control is required.

## Reference(s):

- [ClawHub p-video-avatar skill page](https://clawhub.ai/pruna-ai/skills/p-video-avatar)
- [Pruna AI publisher profile](https://clawhub.ai/user/pruna-ai)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, API calls, Configuration]

**Output Format:** [Markdown guidance with curl commands and JSON request payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires PRUNA_API_KEY and user confirmation before creating paid Pruna predictions; supports either voice_script or uploaded audio, with audio taking precedence when both are provided.]

## Skill Version(s):

1.0.11 (source: server release metadata and SKILL.md metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
