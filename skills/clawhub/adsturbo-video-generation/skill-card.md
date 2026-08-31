## Description:

Create video from text, images, first/last frames, and references, and extend or locally edit existing videos through AdsTurbo.

This skill is ready for commercial/non-commercial use.

## Publisher:

[adsturbo](https://clawhub.ai/user/adsturbo)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to generate new AdsTurbo video clips from prompts or public media URLs, then extend, edit, upload assets for, and monitor asynchronous video tasks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts, uploaded media, and generated task data are sent to AdsTurbo, and uploaded assets become public-link resources.

Mitigation: Do not upload sensitive personal, regulated, confidential, or copyrighted material unless permission and disclosure risk are acceptable.

Risk: Video tasks are asynchronous; resubmitting after a timeout can create duplicate tasks or charges.

Mitigation: Resume polling with the workspace ID or use an idempotency key for retryable submissions.

Risk: Model-specific duration, resolution, ratio, and reference-asset limits can cause rejected requests.

Mitigation: Check the model comparison reference before building a request, and prefer server defaults when the user does not require a specific model.

Risk: Dependency posture depends on the installed requests package version.

Mitigation: Install in a locked or patched Python environment with a current requests version.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/adsturbo/skills/adsturbo-video-generation)
- [AdsTurbo publisher profile](https://clawhub.ai/user/adsturbo)
- [AdsTurbo API key signup](https://adsturbo.ai?channel=clawhub)
- [Video generation reference](references/video_generation.md)
- [Upload reference](references/upload.md)
- [Work status reference](references/work.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and returned JSON from AdsTurbo helper scripts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include public video result URLs, workspace IDs, upload URLs, status JSON, and user-facing wait guidance for asynchronous jobs.]

## Skill Version(s):

1.1.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
