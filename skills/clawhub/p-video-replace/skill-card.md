## Description:

Use when someone wants to swap a person, outfit, or product inside existing footage while keeping the camera move and audio.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pruna-ai](https://clawhub.ai/user/pruna-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and creators use this skill to guide an agent through replacing a person, outfit, or product in an existing video with reference images while preserving camera motion, audio, and unrequested scene elements.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can enable identity swaps or impersonation in existing footage.

Mitigation: Use it only with media and likenesses the user owns or is authorized to edit, and reject unauthorized identity-swap requests.

Risk: Videos, reference images, and prompts are uploaded to Pruna as part of the workflow.

Mitigation: Confirm the user is comfortable sending those assets to Pruna before making API calls.

Risk: Disabling safety checks can reduce abuse protections.

Mitigation: Keep safety checks enabled unless there is a documented, reviewed reason to disable them.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/pruna-ai/skills/p-video-replace)
- [Pruna AI publisher profile](https://clawhub.ai/user/pruna-ai)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, API calls, Configuration]

**Output Format:** [Markdown with inline curl examples and JSON request bodies]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guides upload, prediction creation, polling, and download through the Pruna API; generated video duration follows the source video.]

## Skill Version(s):

1.0.13 (source: server release metadata and SKILL.md metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
