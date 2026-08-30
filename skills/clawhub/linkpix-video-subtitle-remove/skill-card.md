## Description:

Automatically identifies and removes hard subtitles from videos, repairs the image, and produces clean subtitle-free footage for downstream editing or translation workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

Creators, localization teams, and agents use this skill to remove hard subtitles from video files before translation, remixing, or clean-material preparation. It guides setup, credential configuration, qhkit task submission, status polling, and final video delivery.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: API keys may be exposed if users paste credentials into ordinary chat.

Mitigation: Use a secure secret mechanism or QHKIT_TOKEN environment variable, and rotate any key that was already shared in chat.

Risk: Local videos passed to qhkit are uploaded to the vendor service for subtitle removal.

Mitigation: Confirm the user has rights to process the media and avoid sending sensitive or restricted videos unless the vendor service is approved for that data.

Risk: The generate action can consume credits and submitted video tasks may not be cancellable.

Mitigation: Confirm the key parameters and expected or actual charge with the user before task submission, then preserve the returned task ID for polling.

Risk: The workflow depends on installing and running the external qhkit npm package.

Mitigation: Review before installing, use trusted registries, and update qhkit when version or runtime guidance says the local CLI is stale.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/linkpix-video-subtitle-remove)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [LinkPix API key dashboard](https://www.iqinghu.com/workbench/dashboard/api-keys)
- [API key setup guide](https://xcnzsfe4uxrw.feishu.cn/wiki/KJ0Ywsyw8iAXmRkz5l4cddDbn6g)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline bash commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes qhkit installation guidance, credential setup steps, generate/status command examples, polling guidance, and user-facing error handling.]

## Skill Version(s):

0.1.4 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
