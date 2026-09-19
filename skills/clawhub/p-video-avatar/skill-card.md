## Description:

Use when someone wants a person on camera speaking a script — lip-synced host, spokesperson, or narrated avatar from a portrait photo.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pruna-ai](https://clawhub.ai/user/pruna-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to prepare and submit one Pruna p-video-avatar prediction that turns a portrait plus a script or narration audio into a lip-synced talking-head avatar video.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may send portraits, scripts, and optional narration audio to Pruna's API.

Mitigation: Use it only when the user accepts sending those inputs to Pruna and avoid submitting sensitive personal media or scripts without permission.

Risk: The setup guidance can install changing external skill components through floating npx skills add commands.

Mitigation: Prefer pinned or pre-reviewed skill installs and install the optional full suite only when all included capabilities are intended.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/pruna-ai/skills/p-video-avatar)
- [Pruna file upload endpoint](https://api.pruna.ai/v1/files)
- [Pruna predictions endpoint](https://api.pruna.ai/v1/predictions)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with curl commands and JSON request bodies]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guides prompt drafting, input confirmation, API upload, prediction creation, polling, and download for a single avatar-video generation.]

## Skill Version(s):

1.0.13 (source: server release metadata and artifact metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
