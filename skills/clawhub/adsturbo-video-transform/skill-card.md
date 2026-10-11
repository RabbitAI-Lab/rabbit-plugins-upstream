## Description:

Transforms videos by replacing an on-screen person, animating a portrait with reference motion, or translating speech with lip sync.

This skill is ready for commercial/non-commercial use.

## Publisher:

[adsturbo](https://clawhub.ai/user/adsturbo)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and marketing teams use this skill to swap presenters, animate portraits, or re-dub existing videos in other languages through AdsTurbo.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Person swaps and lip-synced translations can create deceptive likeness media without built-in consent checks.

Mitigation: Use only with rights and consent for the people, voices, and footage involved; review the resulting video before sharing.

Risk: Local files uploaded for processing are sent to AdsTurbo and converted into accessible URLs.

Mitigation: Review media for private or customer content before upload, and avoid uploading material that cannot be shared with AdsTurbo.

Risk: Resubmitting an asynchronous task after a timeout may incur duplicate credit charges.

Mitigation: Resume polling the original workspace ID rather than submitting the same task again.

Risk: The requests dependency has no upper version bound, making installs less reproducible.

Mitigation: Pin and review the dependency version when reproducible installs are required.

## Reference(s):

- [AdsTurbo Video Transform on ClawHub](https://clawhub.ai/adsturbo/skills/adsturbo-video-transform)
- [Video transform reference](references/video_transform.md)
- [Asset upload reference](references/upload.md)
- [Async task reference](references/work.md)

## Skill Output:

**Output Type(s):** [Text, Markdown]

**Output Format:** [Markdown with a video link and brief status updates]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Completed-video URL; estimated processing time while awaiting results.]

## Skill Version(s):

1.2.2 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
