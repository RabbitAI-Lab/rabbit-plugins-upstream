## Description:

Use when someone wants to swap a person, outfit, or product inside existing footage while keeping the camera move and audio.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pruna-ai](https://clawhub.ai/user/pruna-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and creators use this skill to guide an agent through replacing a person, outfit, or product in an existing video while preserving camera motion, timing, audio, and unrequested scene elements.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uploads user-provided videos and reference images to Pruna's API using a PRUNA_API_KEY.

Mitigation: Use only media approved for Pruna processing, protect the API key, and avoid submitting confidential or restricted assets unless the account terms permit it.

Risk: The skill supports identity, person, outfit, and product replacement in video.

Mitigation: Use it only with media and likenesses where the user has the rights and consent to modify and publish the result.

Risk: The optional disable_safety_checker parameter can weaken safety controls.

Mitigation: Keep safety checks enabled unless a documented, authorized workflow requires otherwise, and review outputs before distribution.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/pruna-ai/skills/p-video-replace)
- [Pruna file upload API endpoint](https://api.pruna.ai/v1/files)
- [Pruna predictions API endpoint](https://api.pruna.ai/v1/predictions)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, API Calls, Configuration]

**Output Format:** [Markdown guidance with curl examples and JSON request bodies]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a PRUNA_API_KEY and user-provided video plus one to four reference image URLs.]

## Skill Version(s):

1.0.10 (source: server release metadata and SKILL.md metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
