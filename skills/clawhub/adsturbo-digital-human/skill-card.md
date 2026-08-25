## Description:

Turn a script into a talking avatar: choose a platform digital human, clone a custom one from a photo and voice sample, or lip-sync a single portrait to an audio track.

This skill is ready for commercial/non-commercial use.

## Publisher:

[adsturbo](https://clawhub.ai/user/adsturbo)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to create talking-avatar videos from scripts, stock actors, reusable custom personas, or one-off portrait lip-sync inputs. It is intended for digital-human speaking videos with TTS, voice cloning, upload, and async task-status workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Portraits and voice samples may be used for avatar creation, lip-sync, or voice cloning without adequate rights or consent.

Mitigation: Confirm the user has rights and consent before processing portraits, voice samples, reusable personas, or cloned voices.

Risk: Uploaded media may be sent to AdsTurbo and exposed through public URLs.

Mitigation: Warn users before uploading sensitive media and avoid uploading private or regulated content unless the user accepts that exposure.

Risk: Unpinned dependencies can change behavior after installation.

Mitigation: Pin and review Python dependencies before deployment.

Risk: Retrying asynchronous jobs after a timeout can duplicate work or costs.

Mitigation: Resume polling with the returned workspace ID instead of resubmitting unless the task status is explicitly failed.

## Reference(s):

- [Digital Human Reference](references/digital_human.md)
- [Upload Reference](references/upload.md)
- [Work Status Reference](references/work.md)
- [ClawHub Skill Page](https://clawhub.ai/adsturbo/skills/adsturbo-digital-human)
- [AdsTurbo](https://www.adsturbo.ai)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Concise user-facing text with generated media links and optional Markdown command snippets for agent execution.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May submit asynchronous generation jobs and return workspace IDs, status updates, or result URLs.]

## Skill Version(s):

1.0.4 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
